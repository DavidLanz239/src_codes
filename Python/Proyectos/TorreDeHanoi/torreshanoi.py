# =============================================================================
# PROYECTO: Torres de Hanoi - Diplomado de Programación
# AUTOR: David Lanz
# FECHA DE CREACIÓN: Junio 2026
# DESCRIPCIÓN: Interfaz de usuario estilizada de alta fidelidad y bucle principal.
# =============================================================================

import os
from time import time
import Python.Proyectos.TorreDeHanoi.motordeljuego as motordeljuego

class InterfazGraficaTerm:
    """Clase especializada en el renderizado estético de la matriz del juego."""
    def __init__(self, motor: motordeljuego.motordeljuego):
        self.motor = motor
        self.matriz = []

    def limpiar_consola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def construir_matriz_grafica(self):
        """Reconstruye y proyecta la matriz bidimensional de 20x100."""
        self.matriz = [[' '] * 100 for _ in range(20)]

        # Renderizar las bases de las 3 torres en la fila 18
        for i in range(2, 26):
            self.matriz[18][i] = '\u268c'
        for i in range(36, 60):
            self.matriz[18][i] = '\u268c'
        for i in range(70, 94):
            self.matriz[18][i] = '\u268c'

        # Renderizar los ejes verticales en la columna central de cada torre
        for i in range(5, 18):
            self.matriz[i][14] = '\u2503'
        for i in range(5, 18):
            self.matriz[i][48] = '\u2503'
        for i in range(5, 18):
            self.matriz[i][82] = '\u2503'

        # Inyección de los bloques de discos usando el algoritmo posicional
        self._colocar_discos_en_matriz(self.motor.t1.obtener_lista_valores(), 12, 16)
        self._colocar_discos_en_matriz(self.motor.t2.obtener_lista_valores(), 46, 50)
        self._colocar_discos_en_matriz(self.motor.t3.obtener_lista_valores(), 80, 84)

    def _colocar_discos_en_matriz(self, lista_torre, c, b):
        fila = 17
        for x in range(1, len(lista_torre)):
            val = lista_torre[x]
            if val == 1:
                t, q = c, b
            elif val == 2:
                t, q = c - 1, b + 1
            elif val == 3:
                t, q = c - 2, b + 2
            elif val == 4:
                t, q = c - 3, b + 3
            elif val == 5:
                t, q = c - 4, b + 4
            elif val == 6:
                t, q = c - 5, b + 5
            elif val == 7:
                t, q = c - 6, b + 6
            elif val == 8:
                t, q = c - 7, b + 7
            elif val == 9:
                t, q = c - 8, b + 8
            else:
                t, q = c - 9, b + 9

            for i in range(t, q + 1):
                self.matriz[fila][i] = '\u25A0'
            fila -= 1

    def _imprimir_recuadro(self, lineas, ancho=90):
        print(" ┌" + "─" * ancho + "┐")
        for linea in lineas:
            print(linea)
        print(" └" + "─" * ancho + "┘")

    def _imprimir_banner(self, lineas, ancho=90):
        print(f" ╔{'═' * ancho}╗")
        for linea in lineas:
            print(f" ║{linea.center(ancho)}║")
        print(f" ╚{'═' * ancho}╝")

    def mostrar_pantalla_juego(self):
        """Imprime la matriz en pantalla añadiendo marcos de interfaz llamativos."""
        self.construir_matriz_grafica()
        for x in range(20):
            linea = "".join(self.matriz[x])
            print(linea)
        
        self._imprimir_recuadro([
            f"   Movimientos Realizados: {self.motor.pasos}   |   Errores: {self.motor.errores}/5   |   Intentos Libres: {self.motor.intentos}"
        ])

    def mostrar_banner_bienvenida(self):
        self.limpiar_consola()
        self._imprimir_banner([
            "TORRES DE HANOI",
            "Diplomado de Programación"
        ])
        print("\n")

    def inicializar_bucle(self):
        """Administra el flujo de control, menús interactivos y estados booleanos."""
        while True:
            self.mostrar_banner_bienvenida()
            jugador = self._solicitar_nombre()
            discos = self._solicitar_numero_discos(jugador)
            self.motor.configurar_partida(jugador, discos)

            tiempo_inicio = time()
            partida_activa = True

            while self.motor.errores < 5 and partida_activa:
                self.limpiar_consola()
                print(f" JUGADOR: {self.motor.jugador.upper()} ┌────────────────────────────────────────────────────────┐")
                self.mostrar_pantalla_juego()
                print(" ────────────────────────────────────────────────────────────────────────────────────")
                print(" 2026, Desarrollado por David Lanz - Diplomado de Programación")
                print(" ────────────────────────────────────────────────────────────────────────────────────")

                if self.motor.verificar_victoria():
                    self._mostrar_victoria(tiempo_inicio)
                    partida_activa = False
                    break

                print("\n Comandos de acción: Escriba el número de torre origen y destino unidos (Ej: 12 = Torre 1 a Torre 2)")
                print(" Opciones de Torres: 12, 13, 23, 21, 31, 32  |  Escriba '0' para Abandonar.")
                jugada = input(" ──> Seleccione su jugada: ").strip()

                if jugada == '0':
                    partida_activa = False
                    break

                if not self._procesar_jugada(jugada):
                    input(" Presione Enter para continuar...")

            if self.motor.errores >= 5:
                if not self._manejar_derrota():
                    self.motor.reset_variables_a_cero()
                    break
            elif not partida_activa:
                break

    def _solicitar_nombre(self):
        nombre = input(" ──> Por favor ingrese el nombre del jugador: ").strip()
        return nombre or "Invitado"

    def _solicitar_numero_discos(self, jugador):
        while True:
            try:
                discos = int(input(f" ──> Hola {jugador}, indique el número de discos con los que desea jugar (2-10): "))
                if 2 <= discos <= 10:
                    return discos
                print("     [!] Por favor ingrese un número igual o mayor que 2, y menor o igual a 10")
            except ValueError:
                print("     [!] Entrada inválida. Ingrese un valor numérico entero.")

    def _mostrar_victoria(self, tiempo_inicio):
        tiempo_total = time() - tiempo_inicio
        print(f"\n 🎉 ¡Felicidades {self.motor.jugador}, lo has logrado de forma correcta!")
        print(f" ⏱️ Su tiempo total de resolución fue de: {tiempo_total:.2f} segundos.")
        input("\n Presione Enter para regresar al menú...")

    def _procesar_jugada(self, jugada):
        mapeo_jugadas = {
            "12": (1, 2), "13": (1, 3), "23": (2, 3),
            "21": (2, 1), "31": (3, 1), "32": (3, 2)
        }

        if jugada not in mapeo_jugadas:
            print("\n [!] Código de comando inválido.")
            return False

        origen, destino = mapeo_jugadas[jugada]
        if self.motor.realizar_movimiento(origen, destino):
            return True

        print(f"\n ❌ '{self.motor.jugador}' este disco es más grande que el anterior quedan '{self.motor.intentos}' intentos")
        return False

    def _pedir_confirmacion(self, mensaje):
        while True:
            respuesta = input(mensaje).strip().lower()
            if respuesta in ['si', 'no']:
                return respuesta
            print(" [!] Selección incorrecta. Responda estrictamente 'si' o 'no'.")

    def _manejar_derrota(self):
        self.limpiar_consola()
        self._imprimir_recuadro([
            f"   Lo siento '{self.motor.jugador}' esta vez no lo lograste, deseas intentar de nuevo"
        ])
        respuesta = self._pedir_confirmacion(" -> Ingrese su respuesta (si/no): ")
        if respuesta != 'si':
            print(f"\n '{self.motor.jugador}' gracias por jugar con nosotros, te esperamos para que lo intentes en otra ocasión")
            return False
        return True


if __name__ == "__main__":
    # Instanciación y orquestación del programa por objetos
    motor_hanoi = motordeljuego.motordeljuego()
    ui_sistema = InterfazGraficaTerm(motor_hanoi)
    ui_sistema.inicializar_bucle()
    
    
# Fin del modulo principal del juego Torres de Hanoi    