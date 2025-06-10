from tabla_simbolos.instancia import symbol_table as st

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


class IdExp(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def interpret(self):
        return st.get_variable(self.valor)

    def __str__(self):
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

class Asignacion(Expresion):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor

    def __str__(self):
        return ""
    
    def interpret(self):
        valor = self.valor.interpret()
        st.update_variable(self.id, valor)
    
    def __repr__(self):
        return f"Asignacion de: {self.valor} en la variable: {self.id}"


class Declaracion(Expresion):
    def __init__(self, tipo, id, valor):
        print("Declaracion")
        self.tipo = tipo.lower()
        self.id = id
        self.valor = valor

    def __str__(self):
        return ""

    def interpret(self):
        valor = self.valor.interpret()
        st.add_variable(self.id, self.tipo, valor, 0 , 0)
        st.print_table()
    
    def __repr__(self):
        return f"Declaracion de: {self.valor} en la variable: {self.id}"

class Eval(Expresion):
    def __init__(self, expr):
        self.expr = expr
    
    def interpret(self):
        print(f"Resultado: {self.expr.interpret()}")
    
    def __str__(self):
        return f"{self.expr.interpret()}"

class Instruccion(Expresion):
    def __init__(self, instruccion):
        self.instruccion = instruccion

    def interpret(self):
        return self.instruccion.interpret()
    
    def __str__(self):
        print(self.instruccion)
        return f""
    
class Instrucciones(Expresion):
    def __init__(self, instruccion, instrucciones=None):
        if instrucciones is not None:
            self.instrucciones = instrucciones.instrucciones.copy()
        else:
            self.instrucciones = []
        self.instrucciones.append(instruccion)

    def interpret(self):
        results = []
        for instr in self.instrucciones:
            results.append(instr.interpret())
        return results

    def __str__(self):
        return "\n".join(str(instr) for instr in self.instrucciones)

    
class Init(Expresion):
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def interpret(self):
        instr = self.instrucciones.interpret()
        for i in instr: 
            if type(i).__name__ != "NoneType":
                print(type(i).__name__)
                i.interpret()
    
    def __str__(self):
        return f"{self.instrucciones}"