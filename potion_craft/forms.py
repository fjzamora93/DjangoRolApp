# en forms.py
from django import forms

class PotionForm(forms.Form):
    subject = forms.CharField(max_length=100, 
                              label='Tu nombre', 
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    OPCIONES = [
        ('opcion1', 'Opción 1'),
        ('opcion2', 'Opción 2'),
        ('opcion3', 'Opción 3'),
    ]

    #message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    preparacion = forms.ChoiceField(choices=OPCIONES, 
                                 label="Método de preparación",
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    
    ingredientes = forms.ChoiceField(choices=OPCIONES, 
                                 label="Elige tus ingredientes",
                                 widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cambiar el mensaje de required
        for field in self.fields.values():
            field.error_messages['required'] = ''
