from django.shortcuts import render

# Create your views here.
def inicio(req):
  return render(req, 'index.html')


def contacto(req):
  return render(req, 'contact.html')
