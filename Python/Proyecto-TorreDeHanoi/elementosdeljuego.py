# =============================================================================
# PROYECTO: Torres de Hanoi - Diplomado de Programación
# AUTOR: David Lanz
# FECHA DE CREACIÓN: Junio 2026
# DESCRIPCIÓN: Módulo lúdico que contiene las clases base utilizando POO.
# =============================================================================

class Disco:
    """Representa un disco del juego con su tamaño y su cadena visual."""
    def __init__(self, tamano: int):
        self.tamano = tamano
        # Estructura requerida: inicia con dos underscores (_) y añade uno por cada nivel
        self.cadena_visual = "_" * (1 + tamano)

    def __repr__(self):
        return f"Disco({self.tamano})"


class Torre:
    """Encapsula el comportamiento lógico de una torre utilizando una pila."""
    def __init__(self, identificador: int):
        self.identificador = identificador
        # Inicialización de la base con el valor centinela de la plantilla original
        self.discos = [99999]

    def vaciar(self):
        """Reinicializa la torre dejando solo el centinela."""
        self.discos = [99999]

    def apilar(self, disco: Disco):
        """Añade un disco a la parte superior."""
        self.discos.append(disco)

    def desapilar(self) -> 'Disco | None':
        """Remueve y retorna el disco en la cima."""
        return self.discos.pop() if len(self.discos) > 1 else None

    def mirar_cima(self):
        """Inspecciona el valor del disco superior sin removerlo."""
        elem = self.discos[-1]
        return elem.tamano if isinstance(elem, Disco) else elem  # Retorna el 99999 si está vacía

    def obtener_lista_valores(self):
        """Retorna una lista cruda de tamaños para compatibilidad con la lógica de dibujo."""
        valores = []
        for d in self.discos:
            if isinstance(d, Disco):
                valores.append(d.tamano)
            else:
                valores.append(d)
        return valores

    def __len__(self):
        return len(self.discos)
    
   # Fin del módulo de elementos del juego
   