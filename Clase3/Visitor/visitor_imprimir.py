from nodes.ast_nodes import Nodo, Numero, Suma, Resta

class VisitorBase:
    """
    Visitor genérico que, en ausencia de un método específico `visit_<Clase>`,
    recorre automáticamente los atributos que sean nodos o listas de nodos.
    """
    def generic_visit(self, nodo):
        for atributo, valor in vars(nodo).items():
            if isinstance(valor, Nodo):
                valor.accept(self)
            elif isinstance(valor, list):
                for item in valor:
                    if isinstance(item, Nodo):
                        item.accept(self)


class VisitorImprimir(VisitorBase):
    """
    Visitor que genera una representación **infija** de la expresión.
    """
    def __init__(self):
        self.resultado = ""

    def visit_Numero(self, nodo):
        self.resultado += str(nodo.valor)

    def visit_Suma(self, nodo):
        self.resultado += "("
        nodo.izquierda.accept(self)
        self.resultado += " + "
        nodo.derecha.accept(self)
        self.resultado += ")"

    def visit_Resta(self, nodo):
        self.resultado += "("
        nodo.izquierda.accept(self)
        self.resultado += " - "
        nodo.derecha.accept(self)
        self.resultado += ")"
