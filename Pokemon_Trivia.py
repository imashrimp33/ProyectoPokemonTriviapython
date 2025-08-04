import tkinter as tk
from tkinter import ttk, messagebox
import random

class PokemonTrivia:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Trivia Pokémon Interactiva")
        self.root.geometry("700x650")
        self.root.configure(bg="#FF6B6B")
        
        # Usuarios válidos (almacenados en memoria)
        self.usuarios = {
            "ash": "pikachu",
            "misty": "starmie",
            "brock": "onix",
            "admin": "pokemon"
        }
        
        # Variables del juego
        self.usuario_actual = ""
        self.pregunta_actual = 0
        self.puntaje = 0
        self.preguntas_respondidas = []
        
        # Banco de preguntas de Pokémon
        self.preguntas = [
            {
                "pregunta": "¿Cuál es el Pokémon #001 en la Pokédex Nacional?",
                "opciones": ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"],
                "respuesta": 1
            },
            {
                "pregunta": "¿Qué tipo de Pokémon es Pikachu?",
                "opciones": ["Fuego", "Agua", "Eléctrico", "Planta"],
                "respuesta": 2
            },
            {
                "pregunta": "¿Cuál es la evolución de Charmander?",
                "opciones": ["Charizard", "Charmeleon", "Wartortle", "Ivysaur"],
                "respuesta": 1
            },
            {
                "pregunta": "¿En qué región comienza la aventura de Ash Ketchum?",
                "opciones": ["Johto", "Hoenn", "Kanto", "Sinnoh"],
                "respuesta": 2
            },
            {
                "pregunta": "¿Cuál es el Pokémon legendario de tipo Psíquico más famoso?",
                "opciones": ["Mew", "Mewtwo", "Alakazam", "Espeon"],
                "respuesta": 1
            },
            {
                "pregunta": "¿Qué Pokémon es conocido como el 'Pokémon Ratón'?",
                "opciones": ["Rattata", "Pikachu", "Raichu", "Sandshrew"],
                "respuesta": 1
            },
            {
                "pregunta": "¿Cuántos tipos de Pokémon existen actualmente?",
                "opciones": ["16", "17", "18", "19"],
                "respuesta": 2
            },
            {
                "pregunta": "¿Cuál es la debilidad principal del tipo Fuego?",
                "opciones": ["Planta", "Eléctrico", "Agua", "Tierra"],
                "respuesta": 2
            },
            {
                "pregunta": "¿Cómo se llama el profesor Pokémon de la región de Kanto?",
                "opciones": ["Prof. Elm", "Prof. Oak", "Prof. Birch", "Prof. Rowan"],
                "respuesta": 1
            },
            {
                "pregunta": "¿Cuál es el Pokémon más pesado conocido?",
                "opciones": ["Snorlax", "Wailord", "Groudon", "Celesteela"],
                "respuesta": 3
            }
        ]
        
        self.mostrar_bienvenida()
    
    def limpiar_pantalla(self):
        """Limpia todos los widgets de la pantalla"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def mostrar_bienvenida(self):
        """Muestra la pantalla de bienvenida"""
        self.limpiar_pantalla()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#FF6B6B")
        main_frame.pack(expand=True, fill="both")
        
        
        titulo = tk.Label(
            main_frame,
            text="🎮 TRIVIA POKÉMON 🎮",
            font=("Arial", 32, "bold"),
            fg="#FFD700",
            bg="#FF6B6B"
        )
        titulo.pack(pady=50)
        
      
        subtitulo = tk.Label(
            main_frame,
            text="¡Demuestra cuánto sabes sobre el mundo Pokémon!",
            font=("Arial", 16),
            fg="white",
            bg="#FF6B6B"
        )
        subtitulo.pack(pady=10)
        
        # Imagen de Pokéball
       
        imagen = tk.PhotoImage(file="pokeball2.png")  # Cambia por la ruta de tu imagen
        label_imagen = tk.Label(main_frame, image=imagen, bg="#FF6B6B")
        label_imagen.image = imagen  # Evita que la imagen se elimine por el recolector de basura
        label_imagen.pack(pady=30)
      
        instrucciones = tk.Label(
            main_frame,
            text="¡Responde un total de 10 preguntas y Averigua que nivel de maestro eres!",
            font=("Arial", 16),
            fg="white",
            bg="#FF6B6B"
        )
        instrucciones.pack(pady=10)
        
        # Botón para continuar
        btn_continuar = tk.Button(
            main_frame,
            text="¡COMENZAR AVENTURA!",
            font=("Arial", 16, "bold"),
            bg="#4ECDC4",
            fg="white",
            padx=30,
            pady=15,
            command=self.mostrar_login
        )
        btn_continuar.pack(pady=30)

        creditos = tk.Label(
            main_frame,
            text="¡Desarrollado por Jose Segura C.I. 30252304 Electiva 3!",
            font=("Arial", 16),
            fg="white",
            bg="#FF6B6B"
        )
        creditos.pack(pady=10)
    
    def mostrar_login(self):
        """Muestra la pantalla de login"""
        self.limpiar_pantalla()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#FF6B6B")
        main_frame.pack(expand=True, fill="both")
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="🔐 ACCESO DE ENTRENADOR",
            font=("Arial", 24, "bold"),
            fg="#FFD700",
            bg="#FF6B6B"
        )
        titulo.pack(pady=50)
        
        # Frame para el formulario
        form_frame = tk.Frame(main_frame, bg="#FF6B6B")
        form_frame.pack(pady=30)
        
        # Campo usuario
        tk.Label(
            form_frame,
            text="Nombre de Entrenador:",
            font=("Arial", 14),
            fg="white",
            bg="#FF6B6B"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.entry_usuario = tk.Entry(
            form_frame,
            font=("Arial", 14),
            width=20
        )
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)
        
        # Campo contraseña
        tk.Label(
            form_frame,
            text="Pokémon Favorito:",
            font=("Arial", 14),
            fg="white",
            bg="#FF6B6B"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.entry_password = tk.Entry(
            form_frame,
            font=("Arial", 14),
            width=20,
            show="*"
        )
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        
        # Botones
        btn_frame = tk.Frame(main_frame, bg="#FF6B6B")
        btn_frame.pack(pady=30)
        
        btn_login = tk.Button(
            btn_frame,
            text="INICIAR SESIÓN",
            font=("Arial", 14, "bold"),
            bg="#4ECDC4",
            fg="white",
            padx=20,
            pady=10,
            command=self.validar_login
        )
        btn_login.pack(side="left", padx=10)
        
        btn_volver = tk.Button(
            btn_frame,
            text="VOLVER",
            font=("Arial", 14),
            bg="#95A5A6",
            fg="white",
            padx=20,
            pady=10,
            command=self.mostrar_bienvenida
        )
        btn_volver.pack(side="left", padx=10)
        
        # Información de usuarios de prueba
        info_frame = tk.Frame(main_frame, bg="#FF6B6B")
        info_frame.pack(pady=20)
        
        tk.Label(
            info_frame,
            text="👤 Usuarios de prueba:",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#FF6B6B"
        ).pack()
        
        usuarios_info = "ash/pikachu | misty/starmie | brock/onix | admin/pokemon"
        tk.Label(
            info_frame,
            text=usuarios_info,
            font=("Arial", 10),
            fg="#FFD700",
            bg="#FF6B6B"
        ).pack()
    
    def validar_login(self):
        """Valida las credenciales del usuario"""
        usuario = self.entry_usuario.get().lower().strip()
        password = self.entry_password.get().lower().strip()
        
        if not usuario or not password:
            messagebox.showerror("Error", "Por favor, completa todos los campos")
            return
        
        if usuario in self.usuarios and self.usuarios[usuario] == password:
            self.usuario_actual = usuario.title()
            messagebox.showinfo("¡Bienvenido!", f"¡Hola {self.usuario_actual}! ¡Listo para la trivia!")
            self.iniciar_trivia()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. ¡Inténtalo de nuevo!")
    
    def iniciar_trivia(self):
        """Inicia la trivia mezclando las preguntas"""
        self.pregunta_actual = 0
        self.puntaje = 0
        self.preguntas_respondidas = []
        
        # Mezclar preguntas para mayor variedad
        random.shuffle(self.preguntas)
        
        self.mostrar_pregunta()
    
    def mostrar_pregunta(self):
        """Muestra la pregunta actual"""
        if self.pregunta_actual >= len(self.preguntas):
            self.mostrar_resultados()
            return
        
        self.limpiar_pantalla()
        
        pregunta_data = self.preguntas[self.pregunta_actual]
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#FF6B6B")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Header con información del usuario y progreso
        header_frame = tk.Frame(main_frame, bg="#FF6B6B")
        header_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(
            header_frame,
            text=f"Entrenador: {self.usuario_actual}",
            font=("Arial", 12),
            fg="white",
            bg="#FF6B6B"
        ).pack(side="left")
        
        tk.Label(
            header_frame,
            text=f"Pregunta {self.pregunta_actual + 1}/{len(self.preguntas)}",
            font=("Arial", 12),
            fg="white",
            bg="#FF6B6B"
        ).pack(side="right")
        
        # Barra de progreso
        progress_frame = tk.Frame(main_frame, bg="#FF6B6B")
        progress_frame.pack(fill="x", pady=(0, 30))
        
        progress = ttk.Progressbar(
            progress_frame,
            length=400,
            mode='determinate'
        )
        progress.pack()
        progress['value'] = (self.pregunta_actual / len(self.preguntas)) * 100
        
        # Pregunta
        pregunta_frame = tk.Frame(main_frame, bg="white", relief="raised", bd=2)
        pregunta_frame.pack(fill="x", pady=20, padx=20)
        
        tk.Label(
            pregunta_frame,
            text=pregunta_data["pregunta"],
            font=("Arial", 16, "bold"),
            fg="#2C3E50",
            bg="white",
            wraplength=700,
            justify="center"
        ).pack(pady=20)
        
        # Opciones
        self.var_respuesta = tk.IntVar()
        opciones_frame = tk.Frame(main_frame, bg="#FF6B6B")
        opciones_frame.pack(pady=30)
        
        for i, opcion in enumerate(pregunta_data["opciones"]):
            rb = tk.Radiobutton(
                opciones_frame,
                text=f"{chr(65+i)}. {opcion}",
                variable=self.var_respuesta,
                value=i,
                font=("Arial", 14),
                fg="white",
                bg="#FF6B6B",
                selectcolor="#4ECDC4",
                activebackground="#FF6B6B",
                activeforeground="white"
            )
            rb.pack(anchor="w", pady=5, padx=50)
        
        # Botones
        btn_frame = tk.Frame(main_frame, bg="#FF6B6B")
        btn_frame.pack(pady=30)
        
        btn_responder = tk.Button(
            btn_frame,
            text="RESPONDER",
            font=("Arial", 14, "bold"),
            bg="#4ECDC4",
            fg="white",
            padx=30,
            pady=10,
            command=self.verificar_respuesta
        )
        btn_responder.pack(side="left", padx=10)
        
        btn_salir = tk.Button(
            btn_frame,
            text="SALIR",
            font=("Arial", 14),
            bg="#E74C3C",
            fg="white",
            padx=30,
            pady=10,
            command=self.confirmar_salida
        )
        btn_salir.pack(side="left", padx=10)
    
    def verificar_respuesta(self):
        """Verifica si la respuesta es correcta"""
        pregunta_data = self.preguntas[self.pregunta_actual]
        respuesta_usuario = self.var_respuesta.get()
        respuesta_correcta = pregunta_data["respuesta"]
        
        # Guardar información de la respuesta
        self.preguntas_respondidas.append({
            "pregunta": pregunta_data["pregunta"],
            "respuesta_usuario": respuesta_usuario,
            "respuesta_correcta": respuesta_correcta,
            "correcta": respuesta_usuario == respuesta_correcta
        })
        
        if respuesta_usuario == respuesta_correcta:
            self.puntaje += 1
            messagebox.showinfo("¡Correcto! 🎉", "¡Excelente! ¡Esa es la respuesta correcta!")
        else:
            opcion_correcta = pregunta_data["opciones"][respuesta_correcta]
            messagebox.showinfo(
                "Incorrecto 😔", 
                f"La respuesta correcta era: {chr(65+respuesta_correcta)}. {opcion_correcta}"
            )
        
        self.pregunta_actual += 1
        self.mostrar_pregunta()
    
    def mostrar_resultados(self):
        """Muestra los resultados finales"""
        self.limpiar_pantalla()
        
        # Calcular porcentaje
        porcentaje = (self.puntaje / len(self.preguntas)) * 100
        
        # Determinar mensaje según rendimiento
        if porcentaje >= 90:
            mensaje = "¡MAESTRO POKÉMON! 🏆"
            descripcion = "¡Increíble! Eres un verdadero experto en Pokémon."
            color_mensaje = "#FFD700"
        elif porcentaje >= 70:
            mensaje = "¡ENTRENADOR EXPERTO! 🥇"
            descripcion = "¡Muy bien! Tienes un gran conocimiento sobre Pokémon."
            color_mensaje = "#4ECDC4"
        elif porcentaje >= 50:
            mensaje = "¡ENTRENADOR EN PROGRESO! 🥈"
            descripcion = "¡Bien hecho! Sigues aprendiendo sobre el mundo Pokémon."
            color_mensaje = "#F39C12"
        else:
            mensaje = "¡ENTRENADOR NOVATO! 🥉"
            descripcion = "¡No te rindas! Sigue estudiando y mejorando."
            color_mensaje = "#E74C3C"
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#FF6B6B")
        main_frame.pack(expand=True, fill="both")
        
        # Título de resultados
        tk.Label(
            main_frame,
            text="🎯 RESULTADOS FINALES",
            font=("Arial", 28, "bold"),
            fg="#FFD700",
            bg="#FF6B6B"
        ).pack(pady=30)
        
        # Información del usuario
        tk.Label(
            main_frame,
            text=f"Entrenador: {self.usuario_actual}",
            font=("Arial", 16),
            fg="white",
            bg="#FF6B6B"
        ).pack(pady=10)
        
        # Puntaje
        puntaje_frame = tk.Frame(main_frame, bg="white", relief="raised", bd=3)
        puntaje_frame.pack(pady=20, padx=50)
        
        tk.Label(
            puntaje_frame,
            text=f"{self.puntaje}/{len(self.preguntas)}",
            font=("Arial", 48, "bold"),
            fg="#2C3E50",
            bg="white"
        ).pack(pady=20)
        
        tk.Label(
            puntaje_frame,
            text=f"{porcentaje:.1f}% de aciertos",
            font=("Arial", 18),
            fg="#7F8C8D",
            bg="white"
        ).pack(pady=(0, 20))
        
        # Mensaje de rendimiento
        tk.Label(
            main_frame,
            text=mensaje,
            font=("Arial", 24, "bold"),
            fg=color_mensaje,
            bg="#FF6B6B"
        ).pack(pady=20)
        
        tk.Label(
            main_frame,
            text=descripcion,
            font=("Arial", 14),
            fg="white",
            bg="#FF6B6B"
        ).pack(pady=10)
        
        # Botones finales
        btn_frame = tk.Frame(main_frame, bg="#FF6B6B")
        btn_frame.pack(pady=30)
        
        btn_reiniciar = tk.Button(
            btn_frame,
            text="JUGAR DE NUEVO",
            font=("Arial", 14, "bold"),
            bg="#4ECDC4",
            fg="white",
            padx=20,
            pady=10,
            command=self.iniciar_trivia
        )
        btn_reiniciar.pack(side="left", padx=10)
        
        btn_menu = tk.Button(
            btn_frame,
            text="MENÚ PRINCIPAL",
            font=("Arial", 14),
            bg="#95A5A6",
            fg="white",
            padx=20,
            pady=10,
            command=self.mostrar_bienvenida
        )
        btn_menu.pack(side="left", padx=10)
        
        btn_salir = tk.Button(
            btn_frame,
            text="SALIR",
            font=("Arial", 14),
            bg="#E74C3C",
            fg="white",
            padx=20,
            pady=10,
            command=self.root.quit
        )
        btn_salir.pack(side="left", padx=10)
    
    def confirmar_salida(self):
        """Confirma si el usuario quiere salir"""
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres salir de la trivia?"):
            self.root.quit()
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = PokemonTrivia()
    app.ejecutar()