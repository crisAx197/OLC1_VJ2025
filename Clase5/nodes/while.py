## No implementado
class Nodo:
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

class While(Nodo):
    def __init__(self, intrucciones, condicion):
        self.instrucciones = intrucciones
        self.condicion = condicion

    def interpret(self):
        condicion = self.condicion.interpret() ## 5 > 0 == true
        while(condicion):
            if condicion:
                res = self.instrucciones.interpret()
        return 