class Nodo:
    """
    Clase base para todos los nodos del AST. 
    Proporciona el método `accept(visitor)` que realizará dispatch
    dinámico al método adecuado en el Visitor (visit_<ClaseNodo>).
    """
    def accept(self, visitor):
        nombre_método = 'visit_' + self.__class__.__name__
        visita = getattr(visitor, nombre_método, None)
        if visita is None:
            # Si no existe un método específico, llama a generic_visit
            visita = visitor.generic_visit
        return visita(self)


class Numero(Nodo):
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Numero({self.valor})"


class Suma(Nodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def __repr__(self):
        return f"Suma({self.izquierda!r}, {self.derecha!r})"


class Resta(Nodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def __repr__(self):
        return f"Resta({self.izquierda!r}, {self.derecha!r})"
