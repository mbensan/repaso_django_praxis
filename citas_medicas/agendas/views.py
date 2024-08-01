from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from agendas.forms import AgendaModelForm

def es_administrador(user):
  if user.groups.filter(name='administradores').exists():
    return True
  else:
    return False

# Ejemplo de una ruta protegida por login
@login_required
def agendas(req):
  user = req.user
  es_un_administrador = es_administrador(user)
  context = {
    'es_administrador': es_un_administrador
  }
  return render(req, 'agendas.html', context)

class AgendaView(View):

  # el siguiente código protege tanto el GET como el POST
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

  # el GET carga el template
  def get(self, req):
    form = AgendaModelForm()
    context = {
      'form': form
    }
    return render(req, 'nueva_agenda.html', context)
  
  def post(self, req):
    form = AgendaModelForm(req.POST)
    nueva_agenda = form.save()
    messages.success(req, 'Agenda Creada')
    return redirect('/agendas')