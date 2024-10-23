import random
import time  # Para implementar el delay

# Definir los palos y valores de la baraja de póker
PALOS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

class MaquinaPila:
    def __init__(self):
        self.mano_jugador = []
        self.mano_maquina = []
        self.baraja = self.crear_baraja()
        random.shuffle(self.baraja)
        self.apuesta_jugador = 0
        self.credito_jugador = 100  # El jugador empieza con 100 créditos

    def crear_baraja(self):
        """Crea una baraja de 48 cartas sin el 10."""
        return [(valor, palo) for valor in VALORES for palo in PALOS]

    def robar_carta(self):
        """Roba una carta de la baraja."""
        if self.baraja:
            return self.baraja.pop()
        else:
            return None

    def ejecutar_instruccion(self, instruccion):
        if instruccion == "ROBAR_JUGADOR":
            self.robar_cartas_jugador()
        elif instruccion == "ROBAR_MAQUINA":
            self.robar_cartas_maquina()
        elif instruccion == "MOSTRAR_MANOS":
            print(f"Mano del jugador: {self.mano_jugador}")
        elif instruccion == "APOSTAR":
            self.apostar()
        elif instruccion == "COMPARAR_MANOS":
            resultado = self.comparar_manos()
            print(resultado)
        elif instruccion == "DOBLE_O_NADA":
            self.doble_o_nada()
        elif instruccion == "TERCERA_CARTA":
            self.tercera_carta()
        elif instruccion == "CUARTA_CARTA":
            self.cuarta_carta()
        elif instruccion == "SEGUIR_JUGANDO":
            self.seguir_jugando()
        else:
            print(f"Instrucción desconocida: {instruccion}")


    def robar_cartas_jugador(self):
        """El jugador roba dos cartas y se muestran ambas."""
        primera_carta = self.robar_carta()
        segunda_carta = self.robar_carta()
        if primera_carta:
            self.mano_jugador.append(primera_carta)
            print(f"El jugador roba una carta: {primera_carta}")
            time.sleep(0.5)  # Delay de medio segundo
        if segunda_carta:
            self.mano_jugador.append(segunda_carta)
            print(f"El jugador roba una segunda carta: {segunda_carta}")
            time.sleep(0.5)  # Delay de medio segundo
    
    def robar_cartas_maquina(self):
        """La máquina roba dos cartas. Solo muestra la primera carta al jugador."""
        primera_carta = self.robar_carta()
        segunda_carta = self.robar_carta()
        if primera_carta:
            self.mano_maquina.append(primera_carta)
            print(f"La máquina roba una carta visible: {primera_carta}")
            time.sleep(0.5)  # Delay de medio segundo
        if segunda_carta:
            self.mano_maquina.append(segunda_carta)
            print(f"La máquina roba una segunda carta, pero permanece oculta.")
            time.sleep(0.5)  # Delay de medio segundo
    
    def apostar(self):
        """Permite al jugador hacer una apuesta."""
        while True:
            self.apuesta_jugador = int(input(f"Tienes {self.credito_jugador} créditos. ¿Cuánto deseas apostar?: "))
            if self.apuesta_jugador > self.credito_jugador:
                print("No tienes suficientes créditos. Intenta de nuevo.")
            else:
                break
        time.sleep(0.5)  # Delay de medio segundo
    
    def comparar_manos(self):
        """Compara las manos del jugador y la máquina y determina el ganador."""
        valor_jugador = self.calcular_valor_mano(self.mano_jugador)
        valor_maquina = self.calcular_valor_mano(self.mano_maquina)

        print(f"Mano del jugador: {self.mano_jugador}")
        time.sleep(0.5)  # Delay de medio segundo
        print(f"Mano de la máquina: {self.mano_maquina}")
        time.sleep(0.5)  # Delay de medio segundo

        print(f"Valor de la mano del jugador: {valor_jugador}")
        time.sleep(0.5)  # Delay de medio segundo
        print(f"Valor de la mano de la máquina: {valor_maquina}")
        time.sleep(0.5)  # Delay de medio segundo

        if valor_jugador > valor_maquina:
            self.credito_jugador += self.apuesta_jugador
            return "¡El jugador gana la apuesta!"
        elif valor_maquina > valor_jugador:
            self.credito_jugador -= self.apuesta_jugador
            return "¡La máquina gana la apuesta!"
        else:
            return "¡Es un empate!"

    def calcular_valor_mano(self, mano):
        """Calcula un valor básico para una mano. El As siempre vale 11."""
        total = 0
        for carta in mano:
            valor = carta[0]
            if valor in ['J', 'Q', 'K']:
                total += 10  # Las figuras valen 10
            elif valor == 'A':
                total += 11  # El As siempre vale 11
            else:
                total += int(valor)  # Para las cartas del 2 al 9
        return total

    def doble_o_nada(self):
        """Opción de doblar la apuesta o perder todo, solo si el jugador tiene suficientes créditos."""
        if self.apuesta_jugador * 2 > self.credito_jugador:
            print("No tienes suficientes créditos para doblar la apuesta.")
            return
        
        decision = input("¿Quieres doblar la apuesta? (si/no): ").lower()
        if decision == "si":
            self.apuesta_jugador *= 2
            print(f"¡Has doblado la apuesta a {self.apuesta_jugador} créditos!")
        else:
            print("Has decidido no doblar la apuesta.")
        time.sleep(0.5)  # Delay de medio segundo
    
    def tercera_carta(self):
        """Ambos jugadores roban una tercera carta. La tercera carta de la máquina también permanece oculta."""
        carta_jugador = self.robar_carta()
        carta_maquina = self.robar_carta()

        if carta_jugador:
            self.mano_jugador.append(carta_jugador)
            print(f"El jugador roba una tercera carta: {carta_jugador}")
            time.sleep(0.5)  # Delay de medio segundo
        
        if carta_maquina:
            self.mano_maquina.append(carta_maquina)
            print("La máquina roba una tercera carta, pero permanece oculta.")
            time.sleep(0.5)  # Delay de medio segundo
    
    def cuarta_carta(self):
        """Opción de coger una cuarta carta a coste del 30% extra de la apuesta total."""
        costo_extra = round(self.apuesta_jugador * 0.30)
        print(f"El coste de coger una cuarta carta será de {costo_extra} créditos adicionales.")
        
        # Verificar si el jugador tiene suficientes créditos para la cuarta carta
        if self.credito_jugador < costo_extra:
            print("No tienes suficientes créditos para coger una cuarta carta.")
            return
        
        decision = input("¿Quieres coger una cuarta carta pagando el 30% extra? (si/no): ").lower()
        if decision == "si":
            # Restar el coste extra al jugador
            self.credito_jugador -= costo_extra
            
            # Robar cuarta carta para ambos
            carta_jugador = self.robar_carta()
            carta_maquina = self.robar_carta()
            
            if carta_jugador:
                self.mano_jugador.append(carta_jugador)
                print(f"El jugador roba una cuarta carta: {carta_jugador}")
                time.sleep(0.5)
            
            if carta_maquina:
                self.mano_maquina.append(carta_maquina)
                print("La máquina roba una cuarta carta, pero permanece oculta.")
                time.sleep(0.5)
        else:
            print("Has decidido no coger la cuarta carta.")
    
    def seguir_jugando(self):
        """Pregunta si el jugador quiere seguir jugando o finalizar."""
        print(f"Tienes {self.credito_jugador} créditos.")  # Mostrar créditos actuales
        decision = input("¿Quieres seguir jugando? (si/no): ").lower()
        time.sleep(0.5)  # Delay de medio segundo
        if decision == "no":
            print("Gracias por jugar. ¡Hasta la próxima!")
            exit()
        else:
            # Se mantiene el estado de los créditos y se inicia una nueva partida
            self.mano_jugador = []
            self.mano_maquina = []
            self.baraja = self.crear_baraja()  # Rebarajar las cartas para una nueva partida
            random.shuffle(self.baraja)
            print("Nueva partida comenzando...")
            time.sleep(0.5)  # Delay de medio segundo
    
    def cargar_instrucciones_desde_archivo(self, nombre_archivo):
    # Asegúrate de que el archivo tenga la extensión correcta
        if not nombre_archivo.endswith('.lyp'):
            raise ValueError("Archivo no válido. Asegúrate de usar una extensión .vmcode")

        with open(nombre_archivo, "r") as f:
            instrucciones = f.readlines()
        return [instruccion.strip() for instruccion in instrucciones]


    def ejecutar(self, nombre_archivo):
        instrucciones = self.cargar_instrucciones_desde_archivo(nombre_archivo)
        while True:
            for instruccion in instrucciones:
                self.ejecutar_instruccion(instruccion)
                if self.credito_jugador <= 0:
                    print("¡El jugador se ha quedado sin créditos! La máquina gana el juego.")
                    return

if __name__ == "__main__":
    maquina = MaquinaPila()

    # Ejecutar el juego con el archivo de instrucciones
    maquina.ejecutar("instrucciones.lyp")