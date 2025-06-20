import random


class Semaforo:
    def __init__(self, tiempoVerde, tiempoRojo, tiempoAmarillo, tiempoSemaforos=None , tipo=None):
        self.tV = tiempoVerde
        self.tR = tiempoRojo
        self.tA = tiempoAmarillo
        self.tSemaforos = tiempoSemaforos if tiempoSemaforos is not None else [0, 1, 2]
        self.tipo =tipo

    def calcularSemaforo(self):
        r = random.random()
        if r <= self.tV:
            return "V"
        if r <= self.tV + self.tR:
            return "R"
        return "A"

    def calcularTiempo(self):
     tiempo= self.tSemaforos[0]
     resultadoSemaforo = self.calcularSemaforo()

     if (resultadoSemaforo=="R"):
          tiempo = self.tSemaforos[1]
     if (resultadoSemaforo=="A"):
          r = random.random()
          tiempo=0
          if r<=0.5:
              tiempo=self.tSemaforos[2]
     return tiempo,resultadoSemaforo
    def mostrar(self):
     print("Semaforo Tipo"+ self.tipo)

class FabricaSemaforo():
 def crearSemaforoA(self):
     return Semaforo(0.4,0.5 ,0.1,"A")
 def crearSemaforoB(self):
     return Semaforo(0.3 , 0.6 ,0.1,"B")
 def crearSemaforoC(self):
     return Semaforo(0.6 , 0.3 ,0.1,"C")


class Ferrocarril():
 def __init__(self,probBarreraBaja,prob1,tiempo1,prob2,tiempo2,prob3,tiempo3):
      self.pBarrBaj= probBarreraBaja
      self.p1=prob1
      self.t1=tiempo1
      self.p2=prob2
      self.t2=tiempo2
      self.p3=prob3
      self.t3=tiempo3
 def calcularTiempo(self):
     r = random.random()
     tiempo = 0
     if r<=self.pBarrBaj:
         r = random.random()
         if r<=self.p1:
             tiempo=self.t1
         else:
             if r<=self.p1+self.p2:
                 tiempo=self.t2
             else:
                 tiempo=self.t3
     return tiempo
 def mostrar(self):
     print("Ferrocarril")

class FabricaFerrocarril():
 def crearFerrocarrilTipo1(self):
     return Ferrocarril(0.2,0.6,3,0.3,1.5,0.1,5)
 



class Tramo():
 def __init__(self,kmRecorrer, velocidadEsperada,velocidadMaxima,velocidadMinima,probEsperada,probMaxima,probMinima):
      self.kmRecorrer=kmRecorrer
      self.vE= velocidadEsperada
      self.vMax= velocidadMaxima
      self.vMin= velocidadMinima
      self.probE=probEsperada
      self.probMin=probMinima
      self.probMax=probMaxima



 def calcularTiempo(self):
     r = random.random()
     velocidad = 0
     if r<=self.probE:
         velocidad=self.vE
     else:
         if r<=self.probE+self.probMin:
             velocidad=self.vMin
         else:
             velocidad=self.t3
     tiempo= ( self.kmRecorrer / velocidad ) *60
     return tiempo 
 def mostrar(self):
     print("Tramo")





class Parada():
 def __init__(self,probNoSubaNadie,probNoBajaNadie,probBajenM3,probSubanM3, tNS ,tNB ,NM3 , SM3):
      self.pNb=probNoBajaNadie
      self.pNs=probNoSubaNadie
      self.pBM3=probBajenM3
      self.pSM3=probSubanM3

      self.tNb=tNB
      self.tNs=tNS
      self.tBM3=NM3
      self.tSM3=SM3

 def calcularTiempo(self):
     tiempo=0

     r = random.random()

     # No baje nadie o bajen mas de 3

     if r<= self.pNb:
         tiempo = self.tNb
     if r<= self.pNb+self.pBM3:
         tiempo=self.pBM3

     r = random.random()
     
     # No suba nadie o suba mas de 3
     if r<= self.pNs:
         tiempo += self.tNs
     if r<= self.pNs+self.pSM3:
         tiempo +=self.pSM3

     return tiempo


class Ruta:
    def __init__(self,paradas,semaforos,ferrocarril,orden):
     self.paradas= paradas
     self.semaforos=semaforos
     self.ferrocarril= ferrocarril
     self.orden= orden
    def obtenerCamino(self):
     indiceSemaforo=0
     indiceFerrocarril=0
     indiceParadas=0

     camino=[]

     for tramo in self.orden:
         t = tramo
         if "semaforo" in tramo:
              camino.append(self.semaforos[indiceSemaforo])
              indiceSemaforo+=1

         if "paradas" in tramo:
              camino.append(self.paradas[indiceParadas])
              indiceParadas+=1

         if "ferrocarril" in tramo:
              camino.append(self.ferrocarril[indiceFerrocarril])
              indiceFerrocarril+=1
     return camino
    def mostrarCamino(self):
     camino = self.obtenerCamino()
     for tramo in camino:
          tramo.mostrar() 