from django.shortcuts import render
from django.http import HttpResponse
from app_coder.models import Familiar

# Create your views here.

def familia(self):

    familia1 = Familiar(nombre = "Martin Alcaraz" , edad = "35" , nacimiento = "1987-02-23")
    familia1.save()

    familia2 = Familiar(nombre = "Alma Pedraza" , edad = "46" , nacimiento = "1976-07-10")
    familia2.save()

    familia3 = Familiar(nombre = "Juan Sevovia" , edad = "27" , nacimiento = "1995-01-16")
    familia3.save()

    documento = f"<section> <h1>Lista de familiares</h1> <article> <h2>Nombre: {familia1.nombre} </h2> <p>Edad: {familia1.edad} años</p> <p>Fecha de nacimiento:{familia1.nacimiento} </p> </article>  <article> <h2>Nombre: {familia2.nombre} </h2> <p>Edad: {familia2.edad} años</p> <p>Fecha de nacimiento:{familia2.nacimiento} </p> </article> <article> <h2>Nombre: {familia3.nombre} </h2> <p>Edad: {familia3.edad} años</p> <p>Fecha de nacimiento:{familia3.nacimiento} </p> </article>"

    return HttpResponse(documento)