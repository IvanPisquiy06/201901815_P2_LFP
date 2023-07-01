from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import time

file_content = None

def carga_window():
    carga = Tk()
    carga.title("File Selection")

    def select_file():
        global file_content
        file_path = entry.get()  # Get the file path from the entry box
        
        # Check if the file path has the .glc extension
        if file_path.endswith('.glc'):
            try:
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    carga.destroy()
            except FileNotFoundError:
                messagebox.showinfo("¡Error!", "Archivo no encontrado")
        else:
            messagebox.showinfo("¡Error!", "Extensión inválida, selccione un archivo .glc")

    window = ttk.Frame(carga, padding=50)
    window.grid()
    
    label = ttk.Label(window, text="Enter the path of a file:")
    label.pack()
    
    entry = ttk.Entry(window)
    entry.pack()
    
    button = ttk.Button(window, text="Select", command=select_file)
    button.pack()

def general_info():
    global file_content

    lineas = file_content.splitlines()
    nombres = []

    grupos = []
    grupo_actual = []

    for elemento in lineas:
        if elemento == "%":
            grupos.append(grupo_actual)
            grupo_actual = []
        else:
            grupo_actual.append(elemento)

    for i in range(len(grupos)):
        nombres.append(grupos[i][0])

    def show_info():
        gramatica = combobox.current()

        nombre = grupos[gramatica][0]
        no_terminales = grupos[gramatica][1].split(',')
        terminales = grupos[gramatica][2].split(',')
        inicial = grupos[gramatica][3]
        producciones = grupos[gramatica][4:]

        info_sub = Tk()
        info_sub.title("Información General")

        window = ttk.Frame(info_sub, padding=50)
        window.grid()

        ttk.Label(window, text="Nombre:").grid(column=0, row=0)
        ttk.Label(window, text=nombre).grid(column=1, row=0)
        ttk.Label(window, text="No terminales:").grid(column=0, row=1)
        ttk.Label(window, text=no_terminales).grid(column=1, row=1)
        ttk.Label(window, text="Terminales:").grid(column=0, row=2)
        ttk.Label(window, text=terminales).grid(column=1, row=2)
        ttk.Label(window, text="No terminal inicial").grid(column=0, row=3)
        ttk.Label(window, text=inicial).grid(column=1, row=3)
        ttk.Label(window, text="Producciones:").grid(column=0, row=4)
        for i in range(len(producciones)):
            ttk.Label(window, text=producciones[i]).grid(column=1, row=i+4)

        info_main.destroy()

    info_main = Tk()
    info_main.title("Información General")

    window = ttk.Frame(info_main, padding=50)
    window.grid()

    ttk.Label(window, text="Elija una gramática")

    combobox = ttk.Combobox(window, values=nombres)
    combobox.current(0)
    combobox.grid()

    ttk.Button(window, text="Siguiente", command=show_info).grid()

def gramatica_window():
    gramatica = Tk()
    gramatica.title("Módulo gramáticas")

    window = ttk.Frame(gramatica, padding=50)
    window.grid()

    ttk.Button(window, text="Cargar Archivo", command=carga_window).grid(pady=10)
    ttk.Button(window, text="Información General", command=general_info).grid(pady=10)
    ttk.Button(window, text="Árbol de Derivación").grid(pady=10)
    ttk.Button(window, text="Cerrar", command=gramatica.destroy).grid(pady=10)

def automatas_window():
    automatas = Tk()
    automatas.title("Módulo Autómatas")

    window = ttk.Frame(automatas, padding=50)
    window.grid()

    ttk.Button(window, text="Cargar Archivo").grid(pady=10)
    ttk.Button(window, text="Información General").grid(pady=10)
    ttk.Button(window, text="Validar Cadena").grid(pady=10)
    ttk.Button(window, text="Ruta de Validación").grid(pady=10)
    ttk.Button(window, text="Paso a Paso").grid(pady=10)
    ttk.Button(window, text="Una pasado").grid(pady=10)
    ttk.Button(window, text="Cerrar", command=automatas.destroy).grid(pady=10)

def main_window():
    main = Tk()
    main.title("Spark Stack")

    window = ttk.Frame(main, padding=50)
    window.grid()

    ttk.Label(window, text="Seleccione una opción:").grid(pady=20)

    ttk.Button(window, text="Gramática Libre de contexto", command=gramatica_window).grid(pady=10)
    ttk.Button(window, text="Autómatas de Pila", command=automatas_window).grid(pady=10)
    ttk.Button(window, text="Cerrar", command=main.quit).grid(pady=10)

def info_window():
    info = Tk()
    info.title("Spark Stack")

    window = ttk.Frame(info, padding=50)
    window.grid()

    ttk.Label(window, text="Lenguajes formales y de Programación").grid(column=0, row=0)
    ttk.Label(window, text="Sección: A").grid(column=1, row=0)
    ttk.Label(window, text="Carné: 201901815").grid(column=0, row=1)
    ttk.Label(window, text="Ivan de Jesus Pisquiy Escobar").grid(column=1, row=1)

    def close_window():
        info.destroy()  # Close the current window
        main_window()  # Open a new window

    def countdown(seconds):
        label.configure(text=seconds)
        if seconds > 0:
            info.after(1000, countdown, seconds - 1)
        else:
            close_window()

    label = ttk.Label(info, font=("Arial", 24))
    label.grid(pady=20)

    countdown(5)  # Start the countdown
    info.mainloop()

print("Hola")
info_window()
print("Adios")