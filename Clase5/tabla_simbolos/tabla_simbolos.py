from tabla_simbolos.simbolo import Symbol

class SingletonMeta(type):
    """Metaclase para implementar Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SymbolTable(metaclass=SingletonMeta):
    def __init__(self):
        if not hasattr(self, 'scopes'):
            self.scopes = ['global']   
            self.symbols = []          

    @property
    def current_scope(self):
        return self.scopes[-1]

    def new_scope(self, name=None):
        """Crear un nuevo scope."""
        name = name or f"scope_{len(self.scopes)}"
        self.scopes.append(name)
        return name

    def exit_scope(self):
        """Salir del scope actual."""
        if len(self.scopes) > 1:
            return self.scopes.pop()
        raise RuntimeError("No se puede eliminar el scope global")

    def add_variable(self, name, data_type, value=None, line=None, column=None):
        """Agregar una variable al scope actual."""
        sym = Symbol(name=name, entity_type='variable', data_type=data_type,
                     value=value, scope=self.current_scope,
                     line=line, column=column)
        self.symbols.append(sym)
        return sym

    def add_function(self, name, return_type, params=None, line=None, column=None):
        """Agregar una función al scope actual."""
        sym = Symbol(name=name, entity_type='function', data_type=return_type,
                     value={'params': params or []}, scope=self.current_scope,
                     line=line, column=column)
        self.symbols.append(sym)
        return sym



    def get_variable(self, name, scope=None):
        """Recuperar valor buscando desde el scope dado hacia global."""
        scope = scope or self.current_scope
        # buscar en el scope actual
        for sym in reversed(self.symbols):
            if sym.entity_type == 'variable' and sym.name == name and sym.scope == scope:
                return sym.value
        # luego en scopes anteriores
        idx = self.scopes.index(scope)
        for prev in reversed(self.scopes[:idx]):
            for sym in reversed(self.symbols):
                if sym.entity_type == 'variable' and sym.name == name and sym.scope == prev:
                    return sym.value
        raise KeyError(f"Variable '{name}' no encontrada")

    def update_variable(self, name, new_value, scope=None):
        """Actualizar el valor de la variable más reciente con ese nombre."""
        scope = scope or self.current_scope
        for sym in reversed(self.symbols):
            if sym.entity_type == 'variable' and sym.name == name and sym.scope == scope:
                sym.value = new_value
                return sym
        raise KeyError(f"Variable '{name}' no encontrada en scope '{scope}'")

    def print_table(self):
        """Imprimir la tabla de símbolos."""
        headers = ['id', 'name', 'entity_type', 'data_type', 'value', 'scope', 'line', 'column']
        print(" | ".join(headers))
        print("-" * (len(headers) * 15))
        for sym in self.symbols:
            d = sym.to_dict()
            row = [str(d[h]) for h in headers]
            print(" | ".join(row))
