from graphviz import Digraph
from nodes.ast_nodes import *

class ASTGraph:
    def __init__(self):
        self.graph = Digraph('AST', format='svg')
        self.counter = 0

    def _get_id(self):
        self.counter += 1
        return f"node{self.counter}"

    def agregar_nodo(self, label, color="black", style="filled", fillcolor="white"):
        node_id = self._get_id()
        self.graph.node(node_id, label, color=color, style=style, fillcolor=fillcolor)
        return node_id

    def agregar_arista(self, padre_id, hijo_id):
        self.graph.edge(padre_id, hijo_id)

    def renderizar(self, nombre_archivo='ast'):
        self.graph.render(nombre_archivo, view=True)


def graficar_ast(nodo_raiz, nombre_archivo='ast'):
    grafo = ASTGraph()
    nodo_raiz.graficar(grafo)
    grafo.renderizar(nombre_archivo)
