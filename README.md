# MaquinaPila - Juego de Cartas

Este es un juego de cartas simple basado en una baraja de póker. El jugador compite contra una máquina, robando cartas y apostando créditos. El objetivo es comparar las manos y ver quién obtiene el valor más alto. El jugador empieza con 100 créditos y puede apostar, robar cartas adicionales, y decidir si doblar o no su apuesta.

## Instrucciones de uso

### Requisitos
- Python 3.x
- Archivo de instrucciones `.lyp` para ejecutar el juego

### Instalación
1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener Python 3 instalado.
3. Guarda las instrucciones del juego en un archivo llamado `instrucciones.lyp`.

### Ejecución
1. Corre el programa desde la terminal:

   ```bash
   python3 maquina_pila.py
### Instrucciones Disponibles
1. ROBAR_JUGADOR: El jugador roba dos cartas.
2. ROBAR_MAQUINA: La máquina roba dos cartas (solo muestra una al jugador).
3. MOSTRAR_MANOS: Muestra la mano actual del jugador.
4. APOSTAR: Permite al jugador hacer una apuesta.
5. COMPARAR_MANOS: Compara las manos del jugador y la máquina para determinar el ganador.
6. DOBLE_O_NADA: El jugador puede doblar su apuesta o perder todo.
7. TERCERA_CARTA: Ambos jugadores roban una tercera carta.
8. CUARTA_CARTA: El jugador puede robar una cuarta carta pagando un costo adicional.
9. SEGUIR_JUGANDO: Pregunta al jugador si desea continuar con una nueva ronda.

### Formato del archivo de instrucciones
```bash
APOSTAR
ROBAR_JUGADOR
ROBAR_MAQUINA
DOBLE_O_NADA
TERCERA_CARTA
CUARTA_CARTA
COMPARAR_MANOS
SEGUIR_JUGANDO
