import tkinter as tk
import random

class JuegoAdivinanza:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego Adivinar numero ")

       
        self.intentos_maximos = 10
        self.intentos_restantes = self.intentos_maximos
        self.numero_aleatorio = random.randint(1, 100)
        
       
        self.label_instrucciones = tk.Label(root, text="Adivina un número entre 1 y 100:")
        self.label_instrucciones.pack()

        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.boton_adivinar = tk.Button(root, text="Adivinar", command=self.adivinar)
        self.boton_adivinar.pack()

        self.label_feedback = tk.Label(root, text="", fg="blue")
        self.label_feedback.pack()

        self.label_intentos = tk.Label(root, text=f"Intentos restantes: {self.intentos_restantes}")
        self.label_intentos.pack()

        self.boton_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar, state=tk.DISABLED)
        self.boton_reiniciar.pack()

    def adivinar(self):
        try:
            intento = int(self.entry_usuario.get())
        except ValueError:
            self.label_feedback.config(text="Por favor, ingresa un número válido.", fg="red")
            return

        if intento < 1 or intento > 100:
            self.label_feedback.config(text="El número debe estar entre 1 y 100.", fg="red")
            return

        self.intentos_restantes -= 1
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos_restantes}")

        if intento == self.numero_aleatorio:
            self.label_feedback.config(text="¡Correcto! Has adivinado el número.", fg="green")
            self.finalizar_juego()
        elif intento > self.numero_aleatorio:
            self.label_feedback.config(text="Demasiado alto. Intenta con un número más bajo.", fg="blue")
        else:
            self.label_feedback.config(text="Demasiado bajo. Intenta con un número más alto.", fg="blue")

        if self.intentos_restantes == 0:
            self.label_feedback.config(text=f"Has perdido. El número era {self.numero_aleatorio}.", fg="red")
            self.finalizar_juego()

    def finalizar_juego(self):
        self.boton_adivinar.config(state=tk.DISABLED)
        self.boton_reiniciar.config(state=tk.NORMAL)

    def reiniciar(self):
        self.intentos_restantes = self.intentos_maximos
        self.numero_aleatorio = random.randint(1, 100)
        self.label_intentos.config(text=f"Intentos restantes: {self.intentos_restantes}")
        self.label_feedback.config(text="")
        self.entry_usuario.delete(0, tk.END)
        self.boton_adivinar.config(state=tk.NORMAL)
        self.boton_reiniciar.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivinanza(root)
    root.mainloop()
