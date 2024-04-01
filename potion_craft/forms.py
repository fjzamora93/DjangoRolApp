# en forms.py
from django import forms
import random
from .models import Personaje


class ReadOnlyIntegerField(forms.IntegerField):
    def __init__(self, initial=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial = random.randint(1,20)
    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['readonly'] = True
        return attrs


#!VERIFICAR QUE ESTÁ BIEN ESTRUCTURADO
class CharacterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({
            'placeholder': 'Escribe el nombre de tu pesonaje'
        })

    CLASES = [
        ('Guerrero', 'Guerrero'),
        ('Mago', 'Mago'),
        ('Explorador', 'Explorador'),
        ('Clérigo', 'Clérigo'),
        ('Bardo', 'Bardo'),
    ]
    IMAGENES = [
    ('potion_craft/img/portraits/Eric.png', 'Imagen 1'),
    ('potion_craft/img/portraits/humano-bardo-3.png', 'Imagen 2'),
    ('potion_craft/img/portraits/humano-clerigo-3.png', 'Imagen 3'),
    # Agrega más imágenes aquí según sea necesario
]

    nombre = forms.CharField(label='Nombre')
    clase = forms.ChoiceField(choices=CLASES, label="¿Qué clase eres?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    portrait = forms.ChoiceField(choices=IMAGENES, label='Foto', widget=forms.Select(attrs={'class': 'form-control'}))
   

    class Meta:
        model = Personaje
        fields = ['nombre', 'clase', 'portrait']


class PotionForm(forms.Form):
    ESENCIAS = [
        #('0', 'Ninguna'),
        ('1', 'Esencia volátil'),
        ('2', 'Esencia acuosa'),
        ('3', 'Esencia terrosa'),
        ('4', 'Esencia ígnea'),
    ]
    BASE = [
        ('0', 'Agua'),
        ('2', 'Agua destilada'),
        ('4', 'Aceite'), 
        ('6', 'Aceite esencial'),
        ('8', 'Agua bendita'),
        ('-2', 'Agua sucia'), 
        ('-4', 'Agua contaminada'),
        ('-6', 'Agua maldita'), 
    ]
    POTENCIADOR = [
        ('0', 'Sin alteraciones'), 
        ('1', 'Ingrediente corrupto'), 
        ('2', 'Ingrediente sospechoso'), 
    ]
    UTILES = [
        ('-5', 'Sin herramientas'), 
        ('-3', 'Kit de alquimia desgastado'), 
        ('0', 'Kit de alquimia básico'), 
        ('2', 'Kit de alquimia completo'), 
        ('4', 'Kit de maestro alquimista'),
        ('6', 'Laboratorio'),
    ]
    CONOCIMIENTOS = [
        ('-5', 'De memoria'), 
        ('0', 'Alquimia para principiantes'), 
        ('2', 'Manual de alquimia avanzado'), 
        ('4', 'Ars Alquimica'), 
        ('6', 'Gran grimorio de El Alquimista'), 
    ]
    CANTIDAD = [
        ('1', '1 esencia'), 
        ('2', '2 esencias'), 
        ('3', '3 esencias'), 
    ]
    esencias = forms.MultipleChoiceField(choices=ESENCIAS,
                                         label="Elige tu esencia",
                                         widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

    base = forms.ChoiceField(choices=BASE, 
                                 label="¿Qué base líquida vas a usar para tu poción?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    alter = forms.ChoiceField(choices=POTENCIADOR, 
                                 label="¿Vas a alterar tu poción?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    conocimiento = forms.ChoiceField(choices=CONOCIMIENTOS, 
                                 label="¿Vas a alterar tu poción?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    util = forms.ChoiceField(choices=UTILES, 
                                 label="¿Vas a alterar tu poción?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    dado = forms.IntegerField(min_value = 0, initial=11)
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        for field in self.fields.values():
            field.error_messages['required'] = 'Acuérdate de elegir!'





class IngredienteForm(forms.Form):

    INGREDIENTES = [
        ('1', 'Raíz'),
        ('2', 'Hoja'),
        ('3', 'Tallo'),
        ('4', 'Flor'),
        ('5', 'Semilla'),
        ('6', 'Corteza'),
        ('7', 'Vulbo'),
        ('8', 'Micelio'),
    ]

    COLOR = [
        ('aire-fuego', 'Violeta'),
        ('aire', 'Azul'),
        ('agua-aire', 'Turquesa'),
        ('agua', 'Verde'),
        ('tierra-agua', 'Amarillo'),
        ('tierra', 'Marrón'),
        ('fuego-tierra', 'Naranja'),
        ('fuego', 'Rojo'),
    ]

    """
    A partir de aquí se podría hacer una condición:
    if "value del color" not in "value del procesamiento"... ¡Fail!
    else --- if 'aire' in 'valor del color' ... esencia obtenida += la qu ecorresponda.
    Es importante tener en cuenta que puedan salir hasta dos.
    """
    PROCESO = [
        ('aire', 'Fermentar'),
        ('fuego', 'Prender'),
        ('tierra', 'Secar'),
        ('agua', 'Destilar'),
    ]

    HERRAMIENTAS = [
        ('0', 'Cuchillo oxidado'),
        ('1', 'Manuscrito desfasado'),    
        ('2', 'Mortero'),                
        ('3', 'Cuchillo afilado'),        
        ('4', 'Libro de plantas'),         
    ]

    ingr = forms.ChoiceField(choices=INGREDIENTES, 
                                 label="Elige tus ingredientes",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    color = forms.ChoiceField(choices=COLOR, 
                                 label="¿Cómo es el ingrediente?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    proceso = forms.ChoiceField(choices=PROCESO, 
                                 label="¿Cómo vas a procesar el ingrediente?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    herramienta = forms.ChoiceField(choices=HERRAMIENTAS, 
                                 label="¿Qué herramientas tienes?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cambiar el mensaje de required
        for field in self.fields.values():
            field.error_messages['required'] = ''