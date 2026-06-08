# =============================================================================
# PROYECTO: Torres de Hanoi - Diplomado de Programación
# AUTOR: David Lanz
# FECHA DE CREACIÓN: Junio 2026
# DESCRIPCIÓN: Controlador principal de reglas matemáticas y flujo interno.
# =============================================================================

import elementosdeljuego

class motordeljuego:
    """Administra el estado actual de la partida, jugadas y restricciones."""
    def __init__(self):
        self.t1 =elementosdeljuego.Torre(1)
        self.t2 = elementosdeljuego.Torre(2)
        self.t3 = elementosdeljuego.Torre(3)
        self.jugador = ""
        self.cantidad_discos = 0
        self.errores = 0
        self.intentos = 5
        self.pasos = 0

    def configurar_partida(self, nombre_jugador: str, total_discos: int):
        """Inicializa los datos base exigidos por el sistema."""
        self.jugador = nombre_jugador
        self.cantidad_discos = total_discos
        self.errores = 0
        self.intentos = 5
        self.pasos = 0
        
        self.t1.vaciar()
        self.t2.vaciar()
        self.t3.vaciar()

        # Los discos se apilan desde los más grandes a los más pequeños (abajo hacia arriba)
        for i in range(self.cantidad_discos, 0, -1):
            self.t1.apilar(elementosdeljuego.Disco(i))

    def realizar_movimiento(self, origen: int, destino: int) -> bool:
        """
        Mueve un disco entre torres basándose en la POO. 
        Retorna True si el movimiento fue legal, False si es un error.
        """
        torres_map = {1: self.t1, 2: self.t2, 3: self.t3}
        t_origen = torres_map.get(origen)
        t_destino = torres_map.get(destino)

        if not t_origen or not t_destino or len(t_origen) <= 1:
            return False  # Movimiento inválido por origen vacío o incorrecto

        # Validación algorítmica: comparar las cimas
        if t_origen.mirar_cima() < t_destino.mirar_cima():
            disco_sacado = t_origen.desapilar()
            t_destino.apilar(disco_sacado)
            self.pasos += 1
            return True
        else:
            # Control estricto de variables cuando se equivoca colocando un disco grande sobre uno pequeño
            self.errores += 1
            self.intentos = 5 - self.errores
            return False

    def verificar_victoria(self) -> bool:
        """Determina si la torre 3 contiene todos los discos ordenados correctamente."""
        lista_c = self.t3.obtener_lista_valores()
        # Se espera que obtener_lista_valores devuelva una lista con un
        # elemento inicial y luego los discos: por eso +1 en la longitud.
        if len(lista_c) != self.cantidad_discos + 1:
            return False
        return all(lista_c[i + 1] == self.cantidad_discos - i for i in range(self.cantidad_discos))

    def reset_variables_a_cero(self):
        """Reinicializa estrictamente todos los registros a cero antes de salir."""
        self.jugador = 0
        self.cantidad_discos = 0
        self.errores = 0
        self.intentos = 0
        self.pasos = 0
        
        # Fin del módulo motor del juego