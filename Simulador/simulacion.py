from clases import *
from datetime import time, datetime, timedelta
from collections import Counter






def simularUnViaje(horaInicial,tramos,paradas,semaforos,ferrocarril,recorrido):
  tiempo=0

  tiempoCuarto=0
  tiempoMitad=0
  tiempoTresCuarto=0


  r=Ruta(tramos,paradas,semaforos,ferrocarril,recorrido)
  
  c = r.obtenerCamino()
  total= len(c)

  cuarto = round(total*0.25)
  mitad = round(total*0.5)
  tres_cuartos = round(total*0.75)

  for i in range(0,total):
     tiempo+= c[i].calcularTiempo()
     if i==cuarto:
        Mcuarto=tiempo
     if i==mitad:
        Mmitad=tiempo
     if i==cuarto:
        Mtres_cuartos=tiempo
 
  horaFinal = (datetime.combine(datetime.today(), horaInicial) + timedelta(minutes=int(tiempo))).time()
  horaCuarto = (datetime.combine(datetime.today(), horaInicial) + timedelta(minutes=int(Mcuarto))).time()
  horaMitad = (datetime.combine(datetime.today(), horaInicial) + timedelta(minutes=int(Mmitad))).time()
  horaTresCuartos = (datetime.combine(datetime.today(), horaInicial) + timedelta(minutes=int(Mtres_cuartos))).time()
  return horaFinal,horaCuarto,horaMitad,horaFinal




def simularNViajes(horaInicial,recorrido,paradas,tramos,semaforos,ferrocarril,cantidadIteraciones):
  tiemposFinales=[]
  for i in range(0,cantidadIteraciones):
    horaFinal,_,_,_ = simularUnViaje(horaInicial,tramos,paradas,semaforos,ferrocarril,recorrido)

    tiemposFinales.append(horaFinal)
    
  return tiemposFinales






