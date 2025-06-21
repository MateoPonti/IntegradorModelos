from clases import *
from datetime import time, datetime, timedelta
from collections import Counter
from conversionExcel import *
from simulacion import *


def getParametrosViaje():  
    alpha=0.05
    cantidadIteraciones=1000
    horaInicial=time(13, 26)

    fabricaSemaforos =  FabricaSemaforo()
    semaforoA = fabricaSemaforos.crearSemaforoA()
    semaforoB = fabricaSemaforos.crearSemaforoB()
    semaforoC = fabricaSemaforos.crearSemaforoC()

    fabricaFerrocarril = FabricaFerrocarril()
    ferrocarril= fabricaFerrocarril.crearFerrocarrilTipo1()

    recorrido = [
        "tramo1", "semaforo1", "tramo2", "semaforo2", "tramo3", "parada1", "tramo4", "semaforo3",
        "tramo5", "parada2", "tramo6", "semaforo4",
        "tramo7", "semaforo5", "tramo8", "parada3", "tramo9", "semaforo6", "tramo10", "semaforo7",
        "ferrocarril", "tramo11", "semaforo8", "tramo12", "parada4", "tramo13"]
    semaforos=[semaforoA,semaforoA,semaforoA,semaforoB,semaforoC,semaforoB,semaforoC,semaforoB]
    f=[ferrocarril]

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
    return semaforos,f,tramos,paradas,alpha,horaInicial,recorrido,cantidadIteraciones




#tiempoUnViaje= simularUnViaje(Ruta(tramos,paradas,semaforos,[ferrocarril],recorrido))
#print("Tiempo 1 solo viaje : " + str(tiempoUnViaje))


def main():
 semaforos,ferrocarril,tramos,paradas,alpha,horaInicial,recorrido,cantidadIteraciones= getParametrosViaje()

 horariosFinales= sorted(simularNViajes(horaInicial,recorrido,paradas,tramos,semaforos,ferrocarril,cantidadIteraciones))


 horasYfrecuencias = Counter(horariosFinales)
 horas, frecuencias = zip(*horasYfrecuencias.items())
 
 
 porcentajeHoraMin= alpha*100
 porcentajeHoraMax= (1 - alpha)*100

 cantidadHorasDiferentes= len(horas)

 horaMax=horas[int((porcentajeHoraMax*cantidadHorasDiferentes)/100)]
 horaMin=horas[int((porcentajeHoraMin*cantidadHorasDiferentes)/100)]
 


 convertirAExcel(list(horas),list(frecuencias),horaInicial,horaMax,horaMin,alpha)


if __name__ == "__main__":
    main()