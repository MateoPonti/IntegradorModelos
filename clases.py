import random


class Semaforo:
    def __init__(self, tiempoVerde, tiempoRojo, tiempoAmarillo, tiempoSemaforos=None , tipo=None):
        self.tV = tiempoVerde
        self.tR = tiempoRojo
        self.tA = tiempoAmarillo
        self.tSemaforos = tiempoSemaforos if tiempoSemaforos is not None else [0, 1, 2]
        self.tipo= tipo if tipo is not None else "Indefinido"

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
     return tiempo
    def mostrar(self):
     return "Semaforo Tipo "+ self.tipo

class FabricaSemaforo():
 def crearSemaforoA(self):
     return Semaforo(0.4,0.5 ,0.1,None,"A")
 def crearSemaforoB(self):
     return Semaforo(0.3 , 0.6 ,0.1,None,"B")
 def crearSemaforoC(self):
     return Semaforo(0.6 , 0.3 ,0.1,None,"C")


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
     return "Ferrocarril"

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
             velocidad=self.vMax
     tiempo= ( self.kmRecorrer / velocidad ) *60

     return tiempo 
 def mostrar(self):
     return "Tramo"





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
 def mostrar(self):
     return "Parada"


class Ruta:
    def __init__(self,tramos,paradas,semaforos,ferrocarril,orden):
     self.tramos= tramos
     self.paradas= paradas
     self.semaforos=semaforos

     self.ferrocarril= ferrocarril
     self.orden= orden
     self.caminoStr=None



    def obtenerCamino(self):
     indiceSemaforo=0
     indiceFerrocarril=0
     indiceParadas=0
     indiceTramos=0

  
     camino=[]
     caminoStr=[]
     orden = self.orden
    
     for pos in orden:
         if "tramo" in pos:
              tramo=self.tramos[indiceTramos]
              camino.append(tramo)
              caminoStr.append(tramo.mostrar() + " "+ str(indiceTramos+1))
              indiceTramos+=1

         if "semaforo" in pos:
              semaforo = self.semaforos[indiceSemaforo]
              camino.append(semaforo)
              caminoStr.append(semaforo.mostrar()+" "+ str(indiceSemaforo+1))
              indiceSemaforo+=1

         if "parada" in pos:
              parada=self.paradas[indiceParadas]
              camino.append(parada)
              caminoStr.append(parada.mostrar()+" "+str(indiceParadas+1))
              indiceParadas+=1

         if "ferrocarril" in pos:
              ferrocarril=self.ferrocarril[indiceFerrocarril]
              camino.append(ferrocarril)
              caminoStr.append(ferrocarril.mostrar()+" "+str(indiceFerrocarril+1))
              indiceFerrocarril+=1
     self.caminoStr=caminoStr

     return camino
    

    def mostrarCamino(self):
     if self.caminoStr==None:
          self.obtenerCamino()
     camino = self.caminoStr
     indice=1
     for posicion in camino:
         print(str(indice) + " )    " + posicion)
         indice+=1
        
     