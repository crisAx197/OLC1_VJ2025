class Symbol:
    _id_counter = 0

    def __init__(self, name, entity_type, data_type, value, scope, line, column):
        Symbol._id_counter += 1
        self.id = Symbol._id_counter
        self.name = name
        self.entity_type = entity_type  
        self.data_type = data_type      
        self.value = value
        self.scope = scope              
        self.line = line
        self.column = column

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'entity_type': self.entity_type,
            'data_type': self.data_type,
            'value': self.value,
            'scope': self.scope,
            'line': self.line,
            'column': self.column
        }

    def __repr__(self):
        return (
            f"Symbol(id={self.id}, name={self.name}, entity_type={self.entity_type}, "
            f"data_type={self.data_type}, value={self.value}, scope={self.scope}, "
            f"line={self.line}, column={self.column})"
        )
