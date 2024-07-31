from django.forms import ModelForm
from main.models import Contacto

class ContactoModelForm(ModelForm):

  class Meta:
    model = Contacto
    fields = ['nombre', 'email', 'mensaje']
