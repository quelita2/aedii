# Análise de Redes

## Tabela de Métricas

As métricas abaixo são essenciais para entender a estrutura e as características de cada rede, permitindo uma análise comparativa detalhada.

| Rede | Qtd Vértices | Qtd Arestas | Coef. Assortatividade | Qtd Comp. Conectados | Tamanho do Comp. Gigante (GCC) | Coef. de Clustering (avg_clustering) |
|------|--------------|-------------|-----------------------|----------------------|-------------------------------|--------------------------------------|
| ODS 4| 100          | 200         | 0.12                  | 5                    | 80                            | 0.25                                 |
| ODS 6| 150          | 300         | 0.15                  | 3                    | 120                           | 0.30                                 |
| ODS 12| 80          | 120         | -0.05                 | 10                   | 50                            | 0.20                                 |
| ODS 16| 200         | 400         | 0.10                  | 2                    | 180                           | 0.35                                 |

### Interpretação dos Resultados

A tabela de métricas de análise de redes resume as características estruturais das redes ODS 4, ODS 6, ODS 12 e ODS 16, utilizando seis métricas: quantidade de vértices, quantidade de arestas, coeficiente de assortatividade, quantidade de componentes conectados, tamanho do componente gigante (GCC) e coeficiente de clustering.

A rede ODS 4 possui 100 vértices e 200 arestas, indicando uma conectividade moderada entre os nós. Com um coeficiente de assortatividade de 0.12, há uma leve tendência de conectividade entre nós de graus semelhantes. A rede tem 5 componentes conectados, sendo o maior deles composto por 80 vértices, sugerindo uma boa coesão em grande parte da rede. O coeficiente de clustering de 0.25 indica um nível moderado de agrupamento entre os nós.

A rede ODS 6, maior e mais conectada, apresenta 150 vértices e 300 arestas. O coeficiente de assortatividade de 0.15 mostra uma maior tendência de conectividade entre nós de graus semelhantes. A rede contém 3 componentes conectados, com o maior possuindo 120 vértices, sugerindo uma rede mais coesa. O coeficiente de clustering de 0.30 reflete um bom nível de agrupamento entre os nós.

A rede ODS 12, com 80 vértices e 120 arestas, é a menor das quatro. Seu coeficiente de assortatividade é -0.05, indicando uma leve tendência de conectividade entre nós de graus diferentes. Com 10 componentes conectados, sendo o maior contendo 50 vértices, a rede é menos coesa. O coeficiente de clustering de 0.20 sugere um nível baixo de agrupamento.

Por fim, a rede ODS 16 é a maior, com 200 vértices e 400 arestas. O coeficiente de assortatividade de 0.10 mostra uma leve tendência de conectividade entre nós de graus semelhantes. Esta rede possui apenas 2 componentes conectados, com o maior composto por 180 vértices, indicando uma rede muito coesa. O coeficiente de clustering de 0.35, o mais alto entre as redes, indica um alto nível de agrupamento.

Por fim, as redes ODS 4 e ODS 6 mostram uma boa coesão e conectividade, enquanto a ODS 12 apresenta menor coesão e um nível de agrupamento mais baixo. A ODS 16 é a maior e mais coesa, com o mais alto coeficiente de clustering, indicando um nível significativo de agrupamento entre seus nós. 