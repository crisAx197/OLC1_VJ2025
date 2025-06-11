from parser import parser
from tabla_simbolos.instancia import symbol_table as st

def main():
    texto = '''
    INT a = 1 ;
    While ( a > 0 ){
        Eval[a];
        a = a - 1 ; 
        INT b = 1 ;
    }
    a = 5;
    While ( a > 0 ){
        Eval[a];
        a = a - 1 ; 
        INT b = 1 ;
    }
    '''
    print(texto)

    # 1) Parsear y obtener el AST
    raiz = parser.parse(texto)
    if raiz is None:
        print("Hubo un error al parsear la expresión.")
        return

    # 3) Interpretar (evalúa numéricamente)
    raiz.interpret()

    st.print_table()

if __name__ == "__main__":
    main()
