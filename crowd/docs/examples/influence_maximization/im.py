from crowd.project_management.project import Project

# Step 1: Create or load project

project_name = "influencemax"

my_project = Project()
#creation_date = "07/09/2024"
#info = "Influence maximization with Crowd"

# Create new project
# my_project.create_project(project_name, creation_date, info, "node")
# conf_path = os.path.join(os.path.dirname(__file__), 'im_conf.yaml')
# my_project.update_conf_with_path(conf_path)

# Or load the project
my_project.load_project(project_name)

# Step 2: Set the edge parameter using in degree of nodes
# Using weighted cascade for probability assignment where
    # p(u, v) = 1/in_degree(v) or treshold/in_degree(v)
treshold = 1  
graph = my_project.netw.G
for u, v in graph.edges():
    graph[u][v]["activation_prob"] = treshold/graph.degree[v]


# Returns the sum of active_spreader and active node counts
# Will be saved to file automatically
def calculate_total_active(network):
    return (network.node_count[0] + network.node_count[1])

my_project.lib_run_simulation(epochs=20, snapshot_period=1, curr_batch=1, after_iteration_methods=[calculate_total_active])
# my_project.lib_run_simulation(20, 1, 1, [], [calculate_total_active], [], [])