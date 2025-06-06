from parser import parser

def main():
    texto = "3 + 4 - 2 + 7 - 5"

    # 1) Parsear y obtener el AST
    raiz = parser.parse(texto)
    if raiz is None:
        print("Hubo un error al parsear la expresión.")
        return

    # 2) Mostrar representación infija (invoca __str__() de cada nodo)
    print("Representación infija (con paréntesis):", raiz)

    # 3) Interpretar (evalúa numéricamente)
    valor = raiz.interpret()
    print("Resultado numérico:", valor)

if __name__ == "__main__":
    main()
