
from parser import parser
from visitor_imprimir import VisitorImprimir
from visitor_eval import VisitorEval

def main():
    # Entrada
    texto = "3 + 4 - 2 + 7 - 5"  

    # 2) Parsear y obtener el AST
    ast = parser.parse(texto)
    if ast is None:
        print("Hubo un error al parsear la expresión.")
        return

    # 3) Visitor para imprimir la expresión en notación infija
    v_imp = VisitorImprimir()
    ast.accept(v_imp)
    print("Representación infija:", v_imp.resultado)

    # 4) Visitor para evaluar numéricamente la expresión
    v_eval = VisitorEval()
    resultado = ast.accept(v_eval)
    print("Resultado numérico:", resultado)

if __name__ == "__main__":
    main()
