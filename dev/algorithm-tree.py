import networkx as nx
import matplotlib.pyplot as plt

# Define main categories and subcategories
ml_tree = {
    "Machine Learning": {
        "Supervised Learning": [
            "Linear Models", "Tree-Based", "Neural Networks", "Support Vector Machines",
            "Instance-Based", "Probabilistic Models"
        ],
        "Unsupervised Learning": [
            "Clustering", "Dimensionality Reduction", "Matrix Factorization"
        ],
        "Reinforcement Learning": [
            "Value-Based", "Policy-Based", "Model-Based"
        ],
        "Self-Supervised Learning": [
            "Contrastive Learning", "Masked Modeling", "Pretrained Embeddings"
        ],
        "Semi-Supervised Learning": [
            "Pseudo-labeling", "Consistency Regularization"
        ],
        "Ensemble Methods": [
            "Bagging", "Boosting", "Stacking"
        ],
        "Evolutionary / Heuristic": [
            "Genetic Algorithms", "Swarm Intelligence", "Neuroevolution"
        ],
        "Graph-Based": [
            "GCN", "GAT", "GraphSAGE"
        ],
        "Anomaly Detection": [
            "Isolation Forest", "One-Class SVM", "Autoencoders"
        ],
        "Bayesian ML": [
            "Gaussian Processes", "Bayesian Nets", "Bayesian Deep Learning"
        ],
        "Time Series": [
            "ARIMA", "Prophet", "Transformers for Time Series"
        ]
    }
}

# Create graph
G = nx.DiGraph()

# Recursively add nodes and edges
def add_nodes_edges(parent, children):
    if isinstance(children, dict):
        for child, sub_children in children.items():
            G.add_edge(parent, child)
            add_nodes_edges(child, sub_children)
    elif isinstance(children, list):
        for child in children:
            G.add_edge(parent, child)

add_nodes_edges("Root", ml_tree)

# Plot
plt.figure(figsize=(18, 12))
pos = nx.spring_layout(G, k=0.5, iterations=100)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2500, font_size=10, font_weight='bold', edge_color="gray")
plt.title("Graph-style Taxonomy of Machine Learning Algorithms", fontsize=16)
plt.axis("off")
plt.show()
