from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User, Group
from main.forms import ContactoModelForm


# Create your views here.
def inicio(req):
  return render(req, 'index.html')


class RegistroView(View):

  def get(self, req):
    return render(req, 'registration/registro.html')
  
  def post(self, req):
    # 1. Recuperamos los datos del formulario
    email = req.POST['email']
    password = req.POST['password']
    pass_repeat = req.POST['pass_repeat']
    # 2. Validamos que contraseñas concidan
    if password != pass_repeat:
      messages.error(req, 'Contraseñas no coinciden')
      return redirect('/registro')
    # 3. Creamos al usuario
    user = User.objects.create_user(username=email, email=email, password=password)
    # 4. Creamos (si es que no existe) el grupo
    group, creado_en = Group.objects.get_or_create(name='pacientes')
    # 5. Le asignamos el grupo al usuario
    user.groups.add(group)
    # 6. Feedback y redirigimos
    messages.success(req, 'Usuario creado')
    return redirect('/')

  
class ContactoView(View):

  def get(self, req):
    form = ContactoModelForm()
    context = {
      'form': form
    }
    return render(req, 'contact.html', context)
  
  def post(self, req):
    # 1. Recuperamos los datos del formulario
    form = ContactoModelForm(req.POST)
    # 2. Guardamos en la BBDD
    form.save()
    # 3. Le damos feedback al usuario
    messages.success(req, 'Contacto enviado!')
    # 4. Redirigimos
    return redirect('/')
  

  
