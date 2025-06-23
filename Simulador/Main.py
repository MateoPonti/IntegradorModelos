from clases import *
from datetime import time, datetime, timedelta
from collections import Counter
from conversionExcel import *
from simulacion import *
import tkinter as tk
from tkinter import messagebox


def getParametrosViaje():  
    alpha=0.05
    horaInicial=time(23, 26)

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
    return semaforos,f,tramos,paradas,alpha,horaInicial,recorrido


def simularViajes(cantidadIteraciones):
    semaforos,ferrocarril,tramos,paradas,alpha,horaInicial,recorrido= getParametrosViaje()

    horariosFinales= sorted(simularNViajes(horaInicial,recorrido,paradas,tramos,semaforos,ferrocarril,cantidadIteraciones))


    horasYfrecuencias = Counter(horariosFinales)
    horas, frecuencias = zip(*horasYfrecuencias.items())
    
    mitadAlpha=alpha/2
    porcentajeHoraMin= mitadAlpha*100
    porcentajeHoraMax= (1 - mitadAlpha)*100


    cantidadHorasDiferentes= len(horas)


    posicionHMax = round((porcentajeHoraMax*cantidadHorasDiferentes)/100)-1
    posicionHMin= round((porcentajeHoraMin*cantidadHorasDiferentes)/100)  



    horaMax=horas[posicionHMax]
    horaMin=horas[posicionHMin]


    vfinal,cuarto,mitad,tres_cuartos = simularUnViaje(  horaInicial,tramos,paradas,semaforos,ferrocarril,recorrido)
    convertirAExcel(cantidadIteraciones,list(horas),list(frecuencias),horaInicial,horaMax,horaMin,alpha,cuarto,mitad,tres_cuartos,vfinal) 
    




def ejecutarFuncion(entrada):
    try:
        iteraciones = int(entrada.get())
        iterMax=10000
        simulOk=True
        if (iteraciones>10000):
            messagebox.showinfo("Advertencia", "Ingrese un valor menor igual a "+str(iterMax))
            simulOk=False
        simularViajes(int(iteraciones))
        if simulOk : messagebox.showinfo("Éxito", "Simulación Terminada")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido")
    except Exception:
        messagebox.showerror("Error", "Ocurrió un problema durante la simulación")

def main():
    ventana = tk.Tk()
    ventana.title("Simulador de Viajes")
    ventana.geometry("700x400")
    ventana.configure(bg="#E0F7FA")

    frame_principal = tk.Frame(ventana, bg="#E0F7FA")
    frame_principal.place(relx=0.5, rely=0.5, anchor="center")

    etiqueta = tk.Label(frame_principal, text="Simular N Viajes", bg="#E0F7FA", fg="#00796B", font=("Helvetica", 24, "bold"))
    etiqueta.pack(pady=30)

    entrada = tk.Entry(frame_principal, font=("Helvetica", 14), width=10, justify="center")
    entrada.pack(pady=10)

    boton_simulacion = tk.Button(
        frame_principal,
        text="Iniciar Simulación",
        command=lambda: ejecutarFuncion(entrada),
        width=25,
        height=2,
        bg="#4CAF50",
        fg="white",
        font=("Helvetica", 14, "bold"),
        activebackground="#388E3C",
        bd=0,
        relief="flat",
        cursor="hand2"
    )
    boton_simulacion.pack(pady=10)

    ventana.mainloop()





if __name__ == "__main__":
    main()
    