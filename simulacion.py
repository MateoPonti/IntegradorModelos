from clases import *
from datetime import time, datetime, timedelta
from collections import Counter



fabricaSemaforos =  FabricaSemaforo()
semaforoA = fabricaSemaforos.crearSemaforoA()
semaforoB = fabricaSemaforos.crearSemaforoB()
semaforoC = fabricaSemaforos.crearSemaforoC()





fabricaFerrocarril = FabricaFerrocarril()
ferrocarril= fabricaFerrocarril.crearFerrocarrilTipo1()







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




horaInicial=time(13, 26)
recorrido = [
    "tramo1", "semaforo1", "tramo2", "semaforo2", "tramo3", "parada1", "tramo4", "semaforo3",
    "tramo5", "parada2", "tramo6", "semaforo4",
    "tramo7", "semaforo5", "tramo8", "parada3", "tramo9", "semaforo6", "tramo10", "semaforo7",
    "ferrocarril", "tramo11", "semaforo8", "tramo12", "parada4", "tramo13"]
semaforos=[semaforoA,semaforoA,semaforoA,semaforoB,semaforoC,semaforoB,semaforoC,semaforoB]
f=[ferrocarril]

cantidadIteraciones=1000



datos_tramos = [
    [3, 30, 40, 20],
    [5, 40, 45, 30],
    [5, 40, 50, 40],
    [1, 30, 40, 10],
    [4, 40, 40, 40],
    [2, 10, 30, 40],
    [5, 40, 45, 30],
    [10, 30, 40, 60],
    [20, 50, 55, 40],
    [5, 30, 30, 30],
    [1, 30, 35, 30],
    [1, 30, 35, 20],
    [1, 30, 35, 10]
]
probVelocidades = [0.7, 0.2, 0.1]

tramos = [Tramo(*datos, *probVelocidades) for datos in datos_tramos]





probParadas = [0.4, 0.3, 0.2,0.2]
datos_paradas = [
    [1, 2, 3, 4],
    [0.5, 2, 3, 4],
    [0, 1, 2, 3],
    [3, 4, 5, 6]
]
paradas = [Parada(*tiempos, *probParadas) for tiempos in datos_paradas]




#tiempoUnViaje= simularUnViaje(Ruta(tramos,paradas,semaforos,[ferrocarril],recorrido))
#print("Tiempo 1 solo viaje : " + str(tiempoUnViaje))


horariosFinales= sorted(simularNViajes(horaInicial,recorrido,paradas,tramos,semaforos,f,cantidadIteraciones))

print(horariosFinales)

frecuencias = Counter(horariosFinales)

for h in sorted(frecuencias):
    print(h.strftime("%H:%M"), "→", frecuencias[h])
