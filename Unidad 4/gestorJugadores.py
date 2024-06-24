import json
from pathlib import Path
from tkinter import *
from tkinter import ttk
from jugador import Jugador

class GestorJugadores:
    __lista:list
    def __init__(self):
        self.__lista = []

    def agregar_jugador(self, nom, puntos, fecha, hora):
        xhora = str(hora)[:8]
        xjugador = Jugador(nom, puntos, fecha, xhora)
        self.__lista.append(xjugador)
        self.ordenar()

    def agregar_jugador_json(self, xjugador):
        self.__lista.append(xjugador)

    def ordenar(self):
        self.__lista.sort(reverse=True)

    def mostrar_posiciones(self, xvent):
        encoder = ObjectEncoder()
        diccionario = encoder.leerJSONarchivo("puntajes.json")
        xgestor = encoder.decodificador_diccionario(diccionario)
        self.__lista = xgestor.__lista
        tabla = ttk.Treeview(xvent, columns=("nombre", "puntos", "fecha", "hora"), show='headings')
        tabla.heading("nombre", text="Jugador")
        tabla.heading("puntos", text="Puntaje")
        tabla.heading("fecha", text="Fecha")
        tabla.heading("hora", text="Hora")

        tabla.column("nombre", anchor="center", width=100)
        tabla.column("fecha", anchor="center", width=100)
        tabla.column("hora", anchor="center", width=100)
        tabla.column("puntos", anchor="center", width=50)
        tabla.pack(fill=BOTH, expand=True)
        i = 1
        for xjugador in self.__lista:
            tabla.insert("", "end", text=f"{i}°", values=xjugador.getDatos())
            i += 1

    def toJSON(self):
        return {
            '__class__': self.__class__.__name__,
            'jugadores': [xjugador.toJSON() for xjugador in self.__lista]
        }

class ObjectEncoder:
    def decodificador_diccionario(self,d):
        if "__class__" not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'GestorJugadores':
                jugadores = d["jugadores"]
                xgestor = class_()
                for i in range(len(jugadores)):
                    djugador = jugadores[i]
                    class_name = djugador.pop("__class__")
                    class_ = eval(class_name)
                    atributos = djugador['__atributos__']
                    xjugador = class_(atributos["nombre"],atributos["puntos"],atributos["fecha"],atributos["hora"])
                    xgestor.agregar_jugador_json(xjugador)
                return xgestor
            else:
                raise ValueError(f"Unsupported class: {class_name}")

    def guardarJSONarchivo(self, diccionario, archi):
        with Path(archi).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONarchivo(self, archi):
        with Path(archi).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
