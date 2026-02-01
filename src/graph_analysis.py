import networkx as nx
graph = nx.Graph()
def add_review_node(text,sentiment):
    graph.add.node(text,sentiment=sentiment)
def buildrelation(text1,text2):
    graph.add_edge(text1,text2)    