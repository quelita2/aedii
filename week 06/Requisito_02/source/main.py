import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Função para carregar a rede a partir de um arquivo CSV
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

# Função para calcular a assortatividade de grau
def calculate_assortativity(G):
    return nx.degree_assortativity_coefficient(G)

# Função para plotar a relação entre o grau dos nós e o grau médio dos seus vizinhos
def plot_degree_correlation(G, title, ax):
    degree = dict(G.degree())
    avg_neighbor_degree = nx.average_neighbor_degree(G)

    degrees = []
    avg_degrees = []

    for node in G.nodes():
        degrees.append(degree[node])
        avg_degrees.append(avg_neighbor_degree[node])

    df = pd.DataFrame({
        'Node Degree': degrees,
        'Average Neighbor Degree': avg_degrees
    })

    sns.regplot(x='Node Degree', y='Average Neighbor Degree', data=df, ax=ax)
    ax.set_title(f"{title}\nAssortatividade: {calculate_assortativity(G):.2f}")
    ax.grid(True)

# Caminhos dos arquivos CSV no Google Drive
ods_files = {
    4: '../docs/ods_4.csv',
    6: '../docs/ods_6.csv',
    12: '/docs/ods_12.csv',
    16: '/docs/ods_16.csv'
}

# Carregar as redes e calcular a assortatividade
networks = {}
assortativities = {}

for ods, file_path in ods_files.items():
    G = load_network(file_path)
    networks[ods] = G
    assortativities[ods] = calculate_assortativity(G)

# Plotar as redes e mostrar a assortatividade
fig, axs = plt.subplots(2, 2, figsize=(20, 20))

ods_list = [4, 6, 12, 16]

for i, (ods, ax) in enumerate(zip(ods_list, axs.flatten())):
    G = networks[ods]
    plot_degree_correlation(G, f'ODS {ods}', ax)

plt.tight_layout()
plt.show()
