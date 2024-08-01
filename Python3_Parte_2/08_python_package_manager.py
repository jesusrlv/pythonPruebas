### package manager ###

## pip es el gestor de paqueterías 

#https://pypi.org/

#se usa en la mac pip3 para ejecutar cosas

#viendo numpy #####
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35,24,62,52,30,30,17])
print(type(numpy_array))
print(numpy_array * 2)

#viendo pandas #####

import pandas

# pip list ##### muestra el listado en terminal de lo que se ha instalado en pip
# pip uninstall pandas ### para desinstalar algún paquete en este caso pandas
# pip show numpy ### muestra los datos generales de la aplicación numpy o cualquiera

#pip install requests ### es para hacer peticiones a backend
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
print(response) #responde 200 que es OK
print(response.status_code) #responde 200 que es OK
print(response.json()) #json

### arithmetics package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))

from myotherpackage import otherarithmetics
print(otherarithmetics.sum_two_values(1, 4))

#no me dejaba