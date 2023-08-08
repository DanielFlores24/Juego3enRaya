import tkinter as tk

# Configuración de colores
COLOR_FONDO = "#00387f"
COLOR_BOTON = "#00cfff"
COLOR_TEXTO = "#005cd5"
COLOR_TEXTO_BOTON = "#FFFFFF"
COLOR_TEXTO_GANADOR = "#00fed9"
COLOR_ETIQUETA = COLOR_BOTON
COLOR_CAJA_TEXTO = "#9bffad"

ventanaRegistro = tk.Tk()
ventanaRegistro.geometry("400x200")
ventanaRegistro.title("Ingresa los nombres de usuario")
ventanaRegistro.configure(bg=COLOR_FONDO)

etiquetasFaltaUsuarios = []

def VentanaDeUsuarios():
    global etiqueta1, etiqueta2, cajaDeTexto1, cajaDeTexto2

    etiqueta1 = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 1:", bg=COLOR_FONDO, fg=COLOR_TEXTO_BOTON)
    etiqueta1.pack()

    cajaDeTexto1 = tk.Entry(ventanaRegistro, font="Helvetica 10", bg=COLOR_CAJA_TEXTO, fg=COLOR_TEXTO)
    cajaDeTexto1.pack()

    etiqueta2 = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 2:", bg=COLOR_FONDO, fg=COLOR_TEXTO_BOTON)
    etiqueta2.pack()

    cajaDeTexto2 = tk.Entry(ventanaRegistro, font="Helvetica 10", bg=COLOR_CAJA_TEXTO, fg=COLOR_TEXTO)
    cajaDeTexto2.pack()

def TextoDeLaCaja():
    global usuario1, usuario2

    usuario1 = cajaDeTexto1.get()
    usuario2 = cajaDeTexto2.get()

    for etiqueta in etiquetasFaltaUsuarios:
        etiqueta.destroy()
    etiquetasFaltaUsuarios.clear()

    if usuario1 != "" and usuario2 != "":
        ventanaRegistro.destroy()
        """------------------------------------------------------------------------------------------------------------------------------------------------------------"""

                            # Agregar elementos a la ventana de juego
        ventanaJuego = tk.Tk()
        ventanaJuego.geometry("400x400")
        ventanaJuego.title("Ventana de Juego")
        ventanaJuego.configure(bg=COLOR_FONDO)


        #Valor de lo ancho y de lo Alto dsel Gato
        ancho = 20
        alto = 10

        #Lista de los botones
        botones = []
        #Creamos los botones
        def creacionDelGato(botones):
            for fila in range(3):
                for columna in range(3):
                    #Esta parte de aqui es clave ya que el indice te dice en que parte del gato estas 
                    indice = fila * 3 + columna
                    #Comandos para que el boton accione 
                    boton = tk.Button(ventanaJuego, text=" ", width=ancho, height=alto, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda index=indice: juego.turnoJuego(index))
                    boton.grid(row=fila, column=columna, sticky="nsew")
                    botones.append(boton)

            for i in range(3):
                ventanaJuego.grid_rowconfigure(i, weight=1)
                ventanaJuego.grid_columnconfigure(i, weight=1)

        creacionDelGato(botones)

        class JuegoGato():
            global ganador
            
            def __init__(self):
                self.turno = 1
                self.ganador = None
                self.victorias_jugador1 = 0
                self.victorias_jugador2 = 0
                self.empate = 0
                
            def turnoJuego(self, indice):
                if self.turno % 2 != 0:
                    if botones[indice]["text"] == "X" or botones[indice]["text"] == "O":
                        pass
                    else:
                        botones[indice]["text"] = "X"
                        self.turno += 1
                else:
                    if botones[indice]["text"] == "X" or botones[indice]["text"] == "O":
                        pass
                    else:
                        botones[indice]["text"] = "O"
                        self.turno += 1
                
                self.verificarGanador()

            def verificarGanador(self):
                ganador = ""
    
                # Filas
                for i in range(0, 9, 3):
                    if botones[i]["text"] == botones[i + 1]["text"] == botones[i + 2]["text"] != " ":
                        ganador = botones[i]["text"]
                        
                # Columnas
                for i in range(3):
                    if botones[i]["text"] == botones[i + 3]["text"] == botones[i + 6]["text"] != " ":
                        ganador = botones[i]["text"]

                # Diagonales
                if botones[0]["text"] == botones[4]["text"] == botones[8]["text"] != " ":
                    ganador = botones[0]["text"]
                elif botones[2]["text"] == botones[4]["text"] == botones[6]["text"] != " ":
                    ganador = botones[2]["text"]

                 #Puntuaciones
                if ganador == usuario1:
                    juego.victorias_jugador1 += 1
                elif ganador == usuario2:
                    juego.victorias_jugador2 += 1

                #Comprueba si alguien ya gano
                if ganador != "":
                    VentanaDeFinal(ganador)

                #Si nadie gano
                if self.turno >= 10 and ganador == "":
                    ganador = "El juego a quedado en empate"
                    self.empate += 1
                    VentanaDeFinal(ganador)


            def reiniciar(self):
                for boton in botones:
                    boton["text"] = " "
                self.turno = 1
                self.ganador = None
                
        #Ventana cuando se termina el juego
        def VentanaDeFinal(ganador):
            x = 0
            ventanaFinal = tk.Tk()
            ventanaFinal.geometry("300x200")
            ventanaFinal.title("Ventana Final")
            ventanaFinal.configure(bg=COLOR_FONDO)
            ventanaJuego.withdraw()  # Ocultar ventanaJuego
            #Adjunta a la variable textoFinal el texto a mostrar en pantalla 
            if ganador == "El juego a quedado en empate":
                textoFinal = ganador
            else:
                textoFinal = f"{ganador} a ganado"
            etiquetaFinal = tk.Label(ventanaFinal, text=textoFinal, bg=COLOR_ETIQUETA, fg=COLOR_TEXTO_BOTON)
            etiquetaFinal.pack()
            etiquetaVolveraJugar = tk.Label(ventanaFinal, text="Quieren volver a jugar?", bg=COLOR_FONDO, fg=COLOR_TEXTO_BOTON)
            etiquetaVolveraJugar.pack()

            def VolverJugar():
                juego.reiniciar()
                ventanaFinal.destroy()
                ventanaJuego.deiconify()  # Mostrar ventanaJuego

            #Boton para seguir jugando
            botonJugarSi = tk.Button(ventanaFinal, text="Si", command = VolverJugar)
            botonJugarSi.pack()

            def seAcabo():
                etiquetaDeAgradecimiento = tk.Label(ventanaFinal, text = "Gracias por jugar\nMi GitHub es: DanielFlores24\nAhi encontraras mis proyectos", bg=COLOR_FONDO, fg=COLOR_TEXTO_BOTON)
                etiquetaDeAgradecimiento.pack()
                botonJugarSi.config(state="disabled")  # Deshabilitar el botón "Sí"
                botonJugarNo.config(state="disabled")  # Deshabilitar el botón "No"
                ventanaFinal.after(5000, ventanaFinal.destroy)
                ventanaJuego.destroy()

            #Boton para ya no jugar
            botonJugarNo = tk.Button(ventanaFinal, text="No", command=seAcabo)
            botonJugarNo.pack()

        juego = JuegoGato()
        ventanaJuego.mainloop()

        """---------------------------------------------------------------------------------------------------------------------------------------------------------------"""

    elif usuario1 == "" and usuario2 != "":
        etiquetaFaltaUsuarios = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 1")
        etiquetaFaltaUsuarios.pack()
        etiquetasFaltaUsuarios.append(etiquetaFaltaUsuarios)
    elif usuario1 != "" and usuario2 == "":
        etiquetaFaltaUsuarios = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 2")
        etiquetaFaltaUsuarios.pack()
        etiquetasFaltaUsuarios.append(etiquetaFaltaUsuarios)
    else:
        etiquetaFaltaUsuarios = tk.Label(ventanaRegistro, text="Ingrese ambos nombres")
        etiquetaFaltaUsuarios.pack()
        etiquetasFaltaUsuarios.append(etiquetaFaltaUsuarios)

VentanaDeUsuarios()

boton = tk.Button(ventanaRegistro, text="Ingresar", command=TextoDeLaCaja, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON)
boton.pack()

ventanaRegistro.mainloop()


