<h1>🎯 Aimbot Project</h1>

<p>Aimbot configurable y simple de usar, con control total sobre el movimiento del mouse, disparo y visualización.
Pensado para ser preciso, ajustable y fácil de modificar desde el código.</p>

📦 Requisitos

Python 3.x

Dependencias necesarias (ver requirements.txt si aplica)

🚀 Instalación y Ejecución

Cloná el repositorio y ejecutá el archivo principal:

python aimbot.py

🎮 Controles

Durante la ejecución del programa, podés usar las siguientes teclas:

Tecla	Función
1	Iniciar aimbot
2	Pausar temporalmente
3	Cerrar el programa
⌨️ Configuración de Teclas

Las teclas se pueden modificar directamente desde el código:

STARTING_KEY = "1"   # Inicia el aimbot
SLEEPING_KEY = "2"   # Pausa temporal
STOP_KEY     = "3"   # Finaliza el programa

👁️ Preview (Vista previa)
PREVIEW = False

Valor	Descripción
True	Muestra en pantalla lo que el programa detecta
False	No muestra ninguna ventana
⚙️ Configuración del Aimbot
🎯 DEADZONE

Define el área central del objetivo donde el puntero debe llegar para permitir el disparo.

Menor valor → mayor precisión

Mayor valor → más tolerancia

🔧 FACTOR

Controla la fuerza del movimiento del mouse hacia el objetivo.

Evita que el aimbot se pase del target

Permite movimientos más naturales

🔫 SHOOT
SHOOT = True

Valor	Función
True	Disparo automático
False	Disparo manual
🧲 AIM
AIM = True


Activa o desactiva el movimiento automático de la mira hacia el objetivo

🖱️ MAX_MOVE_PER_FRAME
MAX_MOVE_PER_FRAME = 10


Cantidad máxima de píxeles que el mouse puede moverse por frame

Valores bajos → movimiento más suave y humano

Valores altos → movimiento más rápido y agresivo

🧠 Notas

Todos los valores son totalmente personalizables

Ajustar los parámetros mejora la precisión y naturalidad

Recomendado probar valores bajos e ir ajustando
