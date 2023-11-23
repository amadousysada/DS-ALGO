
class Graph:
    def __init__(self, gdict):
        if gdict:
            self.gdict = gdict
        else:
            self.gdict = {}

    def list_edges(self):
        edges = []
        for key in self.gdict:
            for node in self.gdict[key]:
                edges.append((key, node))
        print(edges)


g =  {
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}

graph = Graph(gdict=g)

graph.list_edges()