import sys
import math

def num_palabra(num):

  primeros15 = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco',
    'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce',
    'trece', 'catorce', 'quince']
  
  if num <= 15:
    return primeros15[num]
  # dieci-algo
  elif num <= 19:
    unidades = num - 10
    return 'dieci' + num_palabra(unidades)
  # veinte
  elif num == 20:
    return 'veinte'
  # veinti-algo  23 veintitres
  elif num <= 29:
    unidades = num - 20
    return 'veinti' + num_palabra(unidades)
  # algo y algo
  elif num <= 99: # num = 83   decenas = 8
    decenas = math.floor(num / 10)
    unidades = num - (decenas * 10)

    decenas_palabra = ['', '', '', 'treinta', 'cuarenta', 'cincuenta',
      'sesenta', 'setenta', 'ochenta', 'noventa']
    
    if unidades == 0:
      return decenas_palabra[decenas]
    
    return decenas_palabra[decenas] + ' y ' + num_palabra(unidades)
  elif num == 100:
    return 'cien'
  # ciento algo
  elif num <= 199:
    resto = num - 100
    return 'ciento ' + num_palabra(resto)
  
  elif num <= 999:
    centenas_palabras = ['', '', 'doscientos', 'trescientos', 'cuatrocientos', 
      'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
    centenas = math.floor(num / 100)
    resto = num - (centenas * 100)
    if resto == 0:
      return centenas_palabras[centenas]
    return centenas_palabras[centenas] + ' ' + num_palabra(resto)
  else: 
    return 'no implementado'

print(num_palabra(int(sys.argv[1])))
