class Expresion:
    """
    Clase base para los nodos del AST en el patrón Interpreter.
    Cada nodo debe implementar:
      - interpret() → devuelve el valor numérico de la subexpresión.
      - __str__()    → devuelve la representación infija de la subexpresión.
    """
    def interpret(self):
        raise NotImplementedError("interpret() no implementado en la subclase")

    def __str__(self):
        raise NotImplementedError("__str__() no implementado en la subclase")


class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def interpret(self):
        # Un número se interpreta a sí mismo
        return self.valor

    def __str__(self):
        # Para imprimir la expresión, basta con su propio valor
        return str(self.valor)

    def __repr__(self):
        return f"Numero({self.valor})"


class Suma(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda    
        self.derecha = derecha        

    def interpret(self):
        # Interpreta recursivamente ambos hijos y suma los resultados
        return self.izquierda.interpret() + self.derecha.interpret()

    def __str__(self):
        # Representación infija con paréntesis
        return f"({self.izquierda} + {self.derecha})"

    def __repr__(self):
        return f"Suma({self.izquierda!r}, {self.derecha!r})"


class Resta(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpret(self):
        # Interpreta recursivamente ambos hijos y resta
        return self.izquierda.interpret() - self.derecha.interpret()

    def __str__(self):
        # Representación infija con paréntesis
        return f"({self.izquierda} - {self.derecha})"

    def __repr__(self):
        return f"Resta({self.izquierda!r}, {self.derecha!r})"
