import networkx as nx
import importlib
import random
from .preprocessing import preprocessor as p
from .preprocessing import communitydetection as com
from .structure.file import File
from .structure.random import Random
from .structure.barabasi_albert import BarabasiAlbert
from .structure.watts_strogatz import WattsStrogatz


class NetworkCreator:

    def __init__(self, conf):
        print("Initializing network creator object")
        self.conf = conf

    def get_degree_count(self):
        try:
            return self.conf["structure"]["random"]["degree"]
        except Exception as ex:
            return 4

    def create_network(self):
        structure = self.conf["structure"]
        structure_creator = None
        for key in structure:
            if key == "random":
                structure_creator = Random(structure[key], self.conf)
            elif key =="file":
                structure_creator = File(structure[key], self.conf)
            elif key == "barabasi-albert":
                structure_creator = BarabasiAlbert(structure[key], self.conf)
            elif key == "watts-strogatz":
                structure_creator = WattsStrogatz(structure[key], self.conf)

        return structure_creator.create()        
        
    
    def _create_network(self):
        
        structure = self.conf["structure"]
        print(structure)
        if "random" in structure:
            return self.create_random_network(None)
        else:
            return self.create_random_network(structure)  
        return

    def create_network_from_file(self, file):
        return nx.read_edgelist(file, create_using = nx.Graph(), nodetype=int)
    
    