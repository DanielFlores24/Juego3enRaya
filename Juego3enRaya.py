import tkinter as tk

# Configuración de colores
COLOR_FONDO = "#00387f"        # Azul oscuro como fondo
COLOR_BOTON = "#00cfff"        # Azul claro para los botones
COLOR_TEXTO = "#005cd5"        # Azul para el texto principal
COLOR_TEXTO_BOTON = "#FFFFFF"  # Texto blanco para los botones
COLOR_TEXTO_GANADOR = "#00fed9"  # Turquesa claro para el texto del ganador
COLOR_ETIQUETA = COLOR_BOTON   # Misma etiqueta que el color de botones
COLOR_CAJA_TEXTO = "#9bffad"   # Verde claro para las cajas de texto

ventanaRegistro = tk.Tk()
ventanaRegistro.geometry("400x200")
ventanaRegistro.title("Ingresa los nombres de usuario")
ventanaRegistro.configure(bg=COLOR_FONDO)

# Lista para almacenar las etiquetas de error
etiquetasFaltaUsuarios = [] 

def VentanaDeUsuarios():
    global etiqueta1, etiqueta2, cajaDeTexto1, cajaDeTexto2

    # Etiqueta y caja para el usuario 1
    etiqueta1 = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 1:", bg=COLOR_FONDO, fg=COLOR_TEXTO_BOTON)
    etiqueta1.pack()
    
    cajaDeTexto1 = tk.Entry(ventanaRegistro, font="Helvetica 10", bg=COLOR_CAJA_TEXTO, fg=COLOR_TEXTO)
    cajaDeTexto1.pack()

    # Etiqueta y caja para el usuario 2
    etiqueta2 = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 2:", bg=COLOR_FONDO, fg=COLOR_TEXTO_BOTON)
    etiqueta2.pack()
    
    cajaDeTexto2 = tk.Entry(ventanaRegistro, font="Helvetica 10", bg=COLOR_CAJA_TEXTO, fg=COLOR_TEXTO)
    cajaDeTexto2.pack()

def TextoDeLaCaja():
    global usuario1, usuario2

    # Obtener los nombres de usuario de las cajas de texto
    usuario1 = cajaDeTexto1.get()
    usuario2 = cajaDeTexto2.get()

    # Limpiar etiquetas de error anteriores
    for etiqueta in etiquetasFaltaUsuarios:
        etiqueta.destroy()
    etiquetasFaltaUsuarios.clear()

    # Comprobar si los nombres de usuario se han ingresado
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
                if self.turno >= 9:
                    ganador = "El juego a quedado en empate"
                    print(ganador)
                    VentanaDeFinal(ganador)
                self.verificarGanador()

            def verificarGanador(self):
                ganador = ""
                # Implementa la lógica para verificar si hay un ganador
                #Checa si gano el primer Jugador
                if botones[0]["text"] == "X":
                    if botones[1]["text"] == "X" and botones[2]["text"] == "X":
                        ganador = usuario1
                    if botones[3]["text"] == "X" and botones[6]["text"] == "X":
                        ganador = usuario1
                    if botones[4]["text"] == "X" and botones[8]["text"] == "X":
                        ganador = usuario1
                if botones[1]["text"] == "X" and botones[4]["text"] == "X" and botones[7]["text"] == "X":
                   ganador = usuario1
                if botones[2]["text"] == "X":
                    if botones[4]["text"] == "X" and botones[6]["text"] == "X":
                        ganador = usuario1
                    if botones[5]["text"] == "X" and botones[8]["text"] == "X":
                        ganador = usuario1
                if botones[3]["text"] == "X" and botones[4]["text"] == "X" and botones[5]["text"] == "X":
                   ganador = usuario1
                if botones[6]["text"] == "X" and botones[7]["text"] == "X" and botones[8]["text"] == "X":   
                   ganador = usuario1

                #Checa si gano el primer Jugador
                if botones[0]["text"] == "O":
                    if botones[1]["text"] == "O" and botones[2]["text"] == "O":
                        ganador = usuario2
                    if botones[3]["text"] == "O" and botones[6]["text"] == "O":
                        ganador = usuario2
                    if botones[4]["text"] == "O" and botones[8]["text"] == "O":
                        ganador = usuario2
                if botones[1]["text"] == "O" and botones[4]["text"] == "O" and botones[7]["text"] == "O":
                   ganador = usuario2
                if botones[2]["text"] == "O":
                    if botones[4]["text"] == "O" and botones[6]["text"] == "O":
                        ganador = usuario2
                    if botones[5]["text"] == "O" and botones[8]["text"] == "O":
                        ganador = usuario2
                if botones[3]["text"] == "O" and botones[4]["text"] == "O" and botones[5]["text"] == "O":
                   ganador = usuario2
                if botones[6]["text"] == "O" and botones[7]["text"] == "O" and botones[8]["text"] == "O":  
                   ganador = usuario2  
                
                if ganador == usuario1 or ganador == usuario2:
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
            if ganador == usuario1:
                textoFinal = f"Gano {usuario1}"
            elif ganador == usuario2:
                textoFinal = f"Gano {usuario2}"
            else:
                textoFinal = ganador
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
        # Etiqueta de error si falta el usuario 1
        etiquetaFaltaUsuarios = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 1 ")
        etiquetaFaltaUsuarios.pack()
        etiquetasFaltaUsuarios.append(etiquetaFaltaUsuarios)
    elif usuario1 != "" and usuario2 == "":
        # Etiqueta de error si falta el usuario 2
        etiquetaFaltaUsuarios = tk.Label(ventanaRegistro, text="Ingrese el nombre del usuario 2 ")
        etiquetaFaltaUsuarios.pack()
        etiquetasFaltaUsuarios.append(etiquetaFaltaUsuarios)
    else:
        # Etiqueta de error si faltan ambos nombres
        etiquetaFaltaUsuarios = tk.Label(ventanaRegistro, text="Ingrese ambos nombres ")
        etiquetaFaltaUsuarios.pack()
        etiquetasFaltaUsuarios.append(etiquetaFaltaUsuarios)

# Crear la interfaz de la ventana de registro
VentanaDeUsuarios()

# Botón para procesar los nombres de usuario
boton = tk.Button(ventanaRegistro, text="Ingresar", command=TextoDeLaCaja,bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON)
boton.pack()

# Iniciar el bucle de la ventana principal
ventanaRegistro.mainloop()


