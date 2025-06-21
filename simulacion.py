from clases import *
from datetime import time, datetime, timedelta
from collections import Counter






def simularUnViajeHastaNSitio(ruta,n):
  tiempo=0
  c = ruta.obtenerCamino()
  if n>=1 and n<=len(c):
     for p in c:
       tiempo+= p.calcularTiempo()
  return tiempo

def simularUnViaje(ruta):
  return simularUnViajeHastaNSitio(ruta,len(ruta.obtenerCamino()))




def simularNViajes(horaInicial,recorrido,paradas,tramos,semaforos,ferrocarril,cantidadIteraciones):
  tiemposFinales=[]
  for i in range(0,cantidadIteraciones):
    minutos = simularUnViaje(Ruta(tramos,paradas,semaforos,ferrocarril,recorrido))


    horaFinal = (datetime.combine(datetime.today(), horaInicial) + timedelta(minutes=int(minutos))).time()

    tiemposFinales.append(horaFinal)
    
  return tiemposFinales






