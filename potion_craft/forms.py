# en forms.py
from django import forms

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
    
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cambiar el mensaje de required
        for field in self.fields.values():
            field.error_messages['required'] = 'Selecciona'




class IngredienteForm(forms.Form):



    INGREDIENTES = [
        ('opcion1', 'Raíz'),
        ('opcion2', 'Hoja'),
        ('opcion3', 'Tallo'),
        ('opcion3', 'Flor'),
        ('opcion3', 'Semilla'),
        ('opcion3', 'Corteza'),
        ('opcion3', 'Vulbo'),
        ('opcion3', 'Seta'),
    ]

    COLOR = [
        ('opcion1', 'Violeta'),
        ('opcion2', 'Azul'),
        ('opcion3', 'Turquesa'),
        ('opcion3', 'Verde'),
        ('opcion1', 'Amarillo'),
        ('opcion2', 'Marrón'),
        ('opcion3', 'Naranja'),
        ('opcion3', 'Rojo'),
    ]

    """
    El procesamiento solo tiene en cuenta el color.
    -Azul, violeta: fermentar
    -verde, turquesa: destilar
    -amarillo, marrón: secar
    -naranja, rojo: prender

    El nombre del ingrediente no sirve de nada, solo es para el juego.
    Si un ingrediente se procesa de forma adecuada, el ingrediente se perderá.
    
    DE otra forma, el ingrediente dará la esencia correspondiente.
    """
    PROCESAMIENTO = [
        ('opcion1', 'Fermentar'),
        ('opcion2', 'Prender'),
        ('opcion3', 'Secar'),
        ('opcion3', 'Destilar'),
    ]

    HERRAMIENTAS = [
        ('opcion1', 'Mortero'),                 #value +1
        ('opcion2', 'Cuchillo afilado'),        #value +2
        ('opcion3', 'Tomo de alquimia'),        #value +3
        ('opcion4', 'Manuscrito desfasado'),    #value -2 (0 esencias)
        ('opcion5', 'Cuchillo oxidado'),        #value -1 (solo 1 esencia)
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