# en forms.py
from django import forms
import random


class ReadOnlyIntegerField(forms.IntegerField):

    def __init__(self, initial=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial = random.randint(1,20)

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs['readonly'] = True
        return attrs

class PotionForm(forms.Form):
    subject = forms.CharField(max_length=100, 
                              label='Tu nombre', 
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    ESENCIAS = [
        ('opcion1', 'Esencia acuosa'),
        ('opcion2', 'Esencia ígnea'),
        ('opcion3', 'Esencia terrosa'),
        ('opcion3', 'Esencia volátil'),
    
    ]

    BASE = [
        ('opcion1', 'Agua'),
        ('opcion2', 'Agua destilada'), # +2 de probabilidad éxito
        ('opcion3', 'Agua sucia'), # -2 de probabilidad de éxito
        ('opcion3', 'Agua bendita'), # +5 de probabilidad de éxito
        ('opcion3', 'Agua corrupta'), #-5 de probabilidad de éxito
        ('opcion3', 'Aceite'), #+3 de probabilidad de éxito
        ('opcion3', 'Aceite esencial'), # +4 de probabilidad de éxito
    ]


    POTENCIADOR = [
        ('opcion1', 'Lirio Rojo'), #Corrompe la poción y da el efecto negativo
        ('opcion2', 'Potenciador puro'), # Da el efecto beneficioso
    ]



    #message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    esencias = forms.ChoiceField(choices=ESENCIAS, 
                                 label="Elige tu esencia",
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    base = forms.ChoiceField(choices=BASE, 
                                 label="¿Qué base líquida vas a usar para tu poción?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    potenciador = forms.ChoiceField(choices=POTENCIADOR, 
                                 label="¿Cómo vas a potenciar tu poción?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    dado = ReadOnlyIntegerField()
    
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cambiar el mensaje de required
        for field in self.fields.values():
            field.error_messages['required'] = 'Selecciona'




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
    PROCESAMIENTO = [
        ('aire', 'Fermentar'),
        ('fuego', 'Prender'),
        ('tierra', 'Secar'),
        ('agua', 'Destilar'),
    ]

    HERRAMIENTAS = [
        ('1', 'Mortero'),                
        ('2', 'Cuchillo afilado'),        
        ('3', 'Tomo de alquimia'),        
        ('-2', 'Manuscrito desfasado'),    
        ('-1', 'Cuchillo oxidado'),        
    ]

    planta = forms.ChoiceField(choices=INGREDIENTES, 
                                 label="Elige tus ingredientes",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    color = forms.ChoiceField(choices=COLOR, 
                                 label="¿Cómo es el ingrediente?",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    procesamiento = forms.ChoiceField(choices=PROCESAMIENTO, 
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