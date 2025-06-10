from parser import parser

def main():
    texto = '''
    INT a = 1;
    a = 5;
    EVAL[a+1];
    '''
    print(texto)

    # 1) Parsear y obtener el AST
    raiz = parser.parse(texto)
    if raiz is None:
        print("Hubo un error al parsear la expresión.")
        return

    # 3) Interpretar (evalúa numéricamente)
    raiz.interpret()

if __name__ == "__main__":
    main()
