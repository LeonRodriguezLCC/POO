import tkinter as tk
from tkinter import ttk, messagebox, StringVar, Entry, Label, Button, Menu, Menubutton, Toplevel
import datetime
import random
from gestorJugadores import GestorJugadores, ObjectEncoder


class App:
    def __init__(self):
        self.__ventanaJuego = tk.Tk()
        self.__ventanaJuego.title("PySimon-Game")
        self.__ventanaJuego.iconbitmap("static/simon.ico")
        self.__colores = ["green", "red", "yellow", "blue"]
        self.__secuencia = []
        self.__secuenciaUsuario = []
        self.__botones = []
        self.__puntaje = 0
        self.__jugador = StringVar()
        self.__gestorJugadores = GestorJugadores()
        self.__objectEncoder = ObjectEncoder()
        self.inicio()
        self.__ventanaJuego.mainloop()

    def inicio(self):
        self.__ventanaJuego.withdraw()
        self.__ventanaInicio = tk.Toplevel()
        self.__ventanaInicio.title("Hola!")
        self.__ventanaInicio.resizable(0, 0)
        self.__ventanaInicio.grab_set()
        self.__ventanaInicio.focus_force()
        self.__ventanaInicio.lift()
        self.__ventanaInicio.geometry("200x100")
        datos = Label(self.__ventanaInicio, text="Datos del jugador")
        datos.grid(row=0, column=0, columnspan=2, sticky='w', pady=5)
        textoJugador = Label(self.__ventanaInicio, text="Jugador")
        textoJugador.grid(row=1, column=0, sticky='w', pady=5)
        entryJugador = Entry(self.__ventanaInicio, textvariable=self.__jugador)
        entryJugador.grid(row=1, column=1, sticky='w', pady=5)
        botonIniciar = Button(self.__ventanaInicio, text="Iniciar Juego", command=self.iniciarJuego)
        botonIniciar.grid(row=2, column=0, columnspan=2, sticky='s', pady=5)



    def iniciarJuego(self):
        self.__ventanaInicio.destroy()
        self.__ventanaJuego.deiconify()
        self.crearMenu()
        self.crearJuego()
        self.siguienteRonda()

    def crearMenu(self):
        menuJuego=Menu(self.__ventanaJuego)
        self.__ventanaJuego.config(menu=menuJuego)

        archivo_menu =Menu(menuJuego, tearoff=0)
        menuJuego.add_cascade(label="Puntajes", menu=archivo_menu)
        archivo_menu.add_command(label="Ver puntajes", command=self.verPuntajes)
        archivo_menu.add_command(label="Salir", command=self.salir)

    def verPuntajes(self):
        ventana_puntajes = Toplevel()
        ventana_puntajes.title("Puntajes")
        ventana_puntajes.geometry("400x300")
        self.__gestorJugadores.mostrar_posiciones(ventana_puntajes)

    def salir(self):
        self.__ventanaJuego.destroy()

    def crearJuego(self):
        self.__ventanaJuego.resizable(0, 0)
        self.marcadorPuntos = tk.Label(self.__ventanaJuego, text=f"Jugador: {self.__jugador.get()}    Puntaje: 0")
        self.marcadorPuntos.pack(anchor='n')
        self.canvasFrame = tk.Frame(self.__ventanaJuego, width=500, height=500)
        self.canvasFrame.pack()
        self.crearBoton(self.canvasFrame, "green", 0, 1)
        self.crearBoton(self.canvasFrame, "red", 0, 0)
        self.crearBoton(self.canvasFrame, "yellow", 1, 1)
        self.crearBoton(self.canvasFrame, "blue", 1, 0)

    def crearBoton(self, frame, color, row, column):
        canvas = tk.Canvas(frame, width=200, height=200, bg=color, relief="raised", bd=10)
        canvas.grid(row=row, column=column, padx=10, pady=10)
        canvas.bind("<Button-1>", self.onClick)
        self.__botones.append(canvas)
        return canvas

    def onClick(self, event):
        boton = event.widget
        color = boton.cget("bg")
        self.cambiarBoton(boton)
        self.__secuenciaUsuario.append(color)
        self.comparar()

    def cambiarBoton(self, boton):
        boton.config(relief="sunken")
        self.__ventanaJuego.update()
        brillo = ""
        reset = boton.cget("bg")
        if boton.cget("bg") == "red":
            brillo = "#FF4B4B"
        elif boton.cget("bg") == "green":
            brillo = "#3FDC00"
        elif boton.cget("bg") == "yellow":
            brillo = "#FFFD8D"
        else:
            brillo = "#496AFF"
        self.__ventanaJuego.after(0, lambda: boton.config(bg=brillo))
        self.__ventanaJuego.after(200, lambda: boton.config(relief="raised"))
        self.__ventanaJuego.after(200, lambda: boton.config(bg=reset))

    def comparar(self):
        if self.__secuenciaUsuario == self.__secuencia[:len(self.__secuenciaUsuario)]:
            if len(self.__secuenciaUsuario) == len(self.__secuencia):
                self.__puntaje += 1
                self.siguienteRonda()
        else:
            self.finalizar()

    def siguienteRonda(self):
        self.marcadorPuntos.config(text=f"Jugador: {self.__jugador.get()}    Puntaje: {self.__puntaje}")
        self.__ventanaJuego.after(500, lambda: self.__secuencia.append(random.choice(self.__colores)))
        self.__ventanaJuego.after(1000, self.recorrerSecuencia)
        self.__secuenciaUsuario = []

    def recorrerSecuencia(self):
        i = 0
        while i < len(self.__secuencia):
            color = self.__secuencia[i]
            self.__ventanaJuego.after(i * 500, lambda color=color: self.parpadear(color))
            i += 1
        self.__ventanaJuego.update()

    def parpadear(self, color):
        for b in self.__botones:
            if b.cget("bg") == color:
                self.cambiarBoton(b)

    def finalizar(self):
        fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.__gestorJugadores.agregar_jugador(self.__jugador.get(), self.__puntaje, fecha_actual, hora_actual)
        self.guardar_puntajes()
        messagebox.showinfo("Game Over", f"Puntaje Final: {self.__puntaje}")
        self.__secuencia = []
        self.__secuenciaUsuario = []
        self.__puntaje = 0
        self.__ventanaJuego.after(3000, self.siguienteRonda)

    def guardar_puntajes(self):
        datos = self.__gestorJugadores.toJSON()
        self.__objectEncoder.guardarJSONarchivo(datos, 'puntajes.json')

if __name__ == "__main__":
    app = App()