import random


class Semaforo():
 def __init__(self,tiempoVerde,tiempoRojo,tiempoAmarillo):
      self.tV=tiempoVerde
      self.tR = tiempoRojo
      self.tA=tiempoAmarillo
 def calcularSemaforo(self):
      r = random.random()
      if (r<=self.tV):
         return "V"
      if (r<= self.tR+self.tV):
         return "R"
      return "A"


class ConstructorSemaforo():
 def crearSemaforoA():
     return Semaforo(0.4,0.5 ,0.1)
 def crearSemaforoB():
     return Semaforo(0.3 , 0.6 ,0.1)
 def crearSemaforoC():
     return Semaforo(0.6 , 0.3 ,0.1)


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
 

class ConstructorFerrocarril():
 def crearFerrocarrilTipo1():
     return Ferrocarril(0.2,0.6,3,0.3,1.5,0.1,5)
 



class Tramo():
 def __init__(self,kmRecorrer, velocidadEsperada,velocidadMaxima,velocidadMinima,probEsperada,probMaxima,probMinima,semaforo):
      self.kmRecorrer=kmRecorrer
      self.vE= velocidadEsperada
      self.vMax= velocidadMaxima
      self.vMin= velocidadMinima
      self.probE=probEsperada
      self.probMin=probMinima
      self.probMax=probMaxima
      self.semaforo = semaforo
      self.tSemaforos=[0,1,2]

 def __init__(self,kmRecorrer, velocidadEsperada,velocidadMaxima,velocidadMinima,probEsperada,probMaxima,probMinima,semaforo,tiemposSemaforos,ferrocarril):
      super(self,kmRecorrer,velocidadEsperada,velocidadMaxima,velocidadMinima,probEsperada,probMaxima,probMinima,semaforo)
      self.tSemaforos=tiemposSemaforos

 def __init__(self,kmRecorrer, velocidadEsperada,velocidadMaxima,velocidadMinima,probEsperada,probMaxima,probMinima,semaforo,ferrocarril):
      super(self,kmRecorrer,velocidadEsperada,velocidadMaxima,velocidadMinima,probEsperada,probMaxima,probMinima,semaforo)
      self.ferr=ferrocarril




 def _calcularRecorrido(self):
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
 

 def _calcularTiempoEnSemaforo(self):
     tiempo= self.tSemaforos[0]
     resultadoSemaforo = self.semaforo.calcularTiempo(self.tSemaforos)

     if (resultadoSemaforo=="R"):
          tiempo = self.tSemaforos[1]
     if (resultadoSemaforo=="A"):
          r = random.random()
          tiempo=0
          if r<=0.5:
              tiempo=self.tSemaforos[2]
     return tiempo
 def calcularTiempo(self):
     tiempo=0
     if (self.ferr != None):
         tiempo+= Ferrocarril.calcularTiempo()
     tiempo+= self._calcularRecorrido()
     tiempo+=self._calcularTiempoEnSemaforo()
     return tiempo

