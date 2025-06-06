from nodes.ast_nodes import Nodo, Numero, Suma, Resta

class VisitorBase:
    """
    Visitor genérico que, en ausencia de un método específico `visit_<Clase>`,
    recorre automáticamente los atributos que sean nodos o listas de nodos.
    """
    def generic_visit(self, nodo):
        raise NotImplementedError(f"No existe método visit para {nodo.__class__.__name__}")

class VisitorEval(VisitorBase):
    """
    Visitor que **evalúa** la expresión aritmética y devuelve un entero.
    """
    def visit_Numero(self, nodo):
        return nodo.valor

    def visit_Suma(self, nodo):
        # evalúa recursivamente subárbol izquierdo y derecho
        izq = nodo.izquierda.accept(self)
        der = nodo.derecha.accept(self)
        return izq + der

    def visit_Resta(self, nodo):
        izq = nodo.izquierda.accept(self)
        der = nodo.derecha.accept(self)
        return izq - der
