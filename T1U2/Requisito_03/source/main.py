import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_network(file_path):
    df = pd.read_csv(file_path)

    # Processar os dados para extrair arestas baseadas na coautoria
    edges = []
    for _, row in df.iterrows():
        authors = str(row["Author(s) ID"]).split("; ")
        for i in range(len(authors)):
            for j in range(i + 1, len(authors)):
                edges.append((authors[i], authors[j]))

    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# Extrair métricas da rede
def extract_network_metrics(G):
    num_vertices = G.number_of_nodes()
    num_edges = G.number_of_edges()
    assortativity_coefficient = nx.degree_assortativity_coefficient(G)
    num_connected_components = nx.number_connected_components(G)
    largest_cc = max(nx.connected_components(G), key=len)
    size_largest_cc = len(largest_cc)
    avg_clustering = nx.average_clustering(G)

    return {
        'num_vertices': num_vertices,
        'num_edges': num_edges,
        'assortativity_coefficient': assortativity_coefficient,
        'num_connected_components': num_connected_components,
        'size_largest_cc': size_largest_cc,
        'avg_clustering': avg_clustering
    }

ods_files = {
    4: '../docs/ods_4.csv',
    6: '../docs/ods_6.csv',
    12: '../docs/ods_12.csv',
    16: '../docs/ods_16.csv'
}

# Carregar as redes e extrair as métricas
network_metrics = {}

for ods, file_path in ods_files.items():
    G = load_network(file_path)
    metrics = extract_network_metrics(G)
    network_metrics[ods] = metrics

# Criar um DataFrame com as métricas
metrics_df = pd.DataFrame(network_metrics).T
metrics_df.columns = [
    'Qtd_Vértices', 'Qtd_Arestas', 'Coef_Assortatividade',
    'Qtd_Comp_Conectados', 'Tamanho_Comp_Gigante', 'Coef_Clustering'
]

metrics_df.to_csv('../docs/network_metrics.csv')
print(metrics_df)