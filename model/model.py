from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.listaConstructors = []
        self.lista = None
        self.anni = DAO.getAllYears()
        self.graph = nx.Graph()
        self.dizionario = {}

    def aggiungi_menu(self):
        return self.anni

    def prendi_constructors(self, year1, year2):
        self.lista = DAO.getAllConstructors(year1, year2)
        for collegamenti in self.lista:
            if collegamenti.driverId not in self.dizionario:
                self.dizionario[collegamenti.driverId] = set()
            self.dizionario[collegamenti.driverId].add(collegamenti.constructorId)

        for i in self.dizionario.values():
            lista = list(i)
            n = len(lista)
            for p in range(n):
                for j in range(p+1,n):
                    nodo1 = lista[p]
                    nodo2 = lista[j]
                    if self.graph.has_edge(nodo1,nodo2):
                        self.graph[nodo1][nodo2]['weight'] += 1
                    else:
                        self.graph.add_edge(nodo1, nodo2, weight=1)

        for i in self.lista:
            self.listaConstructors.append(i.constructorId)

        return self.listaConstructors

    def handle_grafo(self):
        self.graph.add_nodes_from(self.listaConstructors)
        print(self.graph.nodes)
        return self.graph

