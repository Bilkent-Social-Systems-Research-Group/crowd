import json
from crowd.models import network as netw
import networkx as nx

class EdgeSimNetwork(netw.Network):
    def __init__(self, conf_dict, project_dir):
        # create network by calling parent's constructor
        super().__init__(conf_dict, project_dir)
        self.update_method = None

    def run(self, epochs, visualizers = None, snapshot_period = 1, agility = 1, egress = None):
        # Iteration data dictionary
        simulation_data = {}

        for epoch in range(0, epochs):
            if (epoch % snapshot_period) == 0 or (epoch == epochs-1):
                print("Epoch:", epoch)
                if visualizers is not None:
                    for visualizer in visualizers:
                        visualizer.draw(self, epoch)

                if egress is not None:
                    egress.save_graph(str(epoch), self.G, 'graph.json')
                    

            added_links = self.update_method(self)
            simulation_data[str(epoch)] = added_links

        egress.save(json.dumps(simulation_data), 'new_addition.json')    
                
                
