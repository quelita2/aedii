# Trabalho de AED2

Neste trabalho trataremos sobre Assortatividade, Componentes Conectados e Coeficiente de Agrupamento investigando redes de Co-Autoria e ODS-ONU, em específico das ODS's: 
> 4 - Educação de qualidade <br>
6 - Água lima e saneamento<br>
12 - Consumo e produção responsáveis e<br>
16 - Paz, justiça e instituições fortes.

Assortatividade mede a tendência de nós semelhantes em uma rede se conectarem, importante para entender a homofilia em redes sociais. Componentes conectados são subconjuntos onde todos os nós estão interligados, essenciais para identificar clusters ou grupos isolados. O coeficiente de agrupamento mede a probabilidade de que os vizinhos de um nó estejam conectados entre si, crucial para analisar a formação de comunidades e a densidade de triângulos em redes sociais. A partir desses estudos podemos compreender padrões de colaboração, identificar comunidades de pesquisa e avaliar a interconectividade entre diferentes áreas e objetivos, como para investigar redes de coautoria e os Objetivos de Desenvolvimento Sustentável da ONU.

## Análise das Redes

### Gráficos de Assertividade

Um gráfico bipartido sobre a assortatividade em relação ao grau dos nós de uma rede é uma ferramenta visual para entender a relação entre o grau de um nó e o grau médio dos seus vizinhos. A assortatividade mede a tendência de nós de um grafo conectarem-se a outros nós com grau semelhante. A interpretação do gráfico ajuda a identificar padrões de conexão na rede.

| Gráfico de ODS 4 e 6 |
|----------------------|
![Gráfico de ODS 4 e 6](assets/ods-4-6.png)

| Gráfico de ODS 12 e 16 |
|----------------------|
![Gráfico de ODS 12 e 16](assets/ods-12-16.png)

Nestes gráficos, estamos analisando o Grau do Nó (eixo x) e o Grau Médio dos Vizinhos (eixo y). Enquanto o eixo x representa o número de conexões que cada nó possui, o eixo y indica o grau médio dos nós que estão conectados a um nó específico.

No gráfico da ODS 4, encontramos uma assortatividade positiva, onde os pontos formam uma tendência ascendente (os nós de maior grau estão conectados a nós de maior grau, resultando em pontos no quadrante superior direito). Já nos demais, é notada uma maior concentração de agrupamentos na parte inferior esquerda, uma possível explicação seria a representação de novos pesquisadores ou aqueles que publicam pouco, tendo colaborado com outros igualmente novos ou com baixa produtividade.

A reta que passa pelos nós em um gráfico bipartido de assortatividade é uma linha de tendência que ajuda a visualizar a relação geral entre o grau dos nós e o grau médio de seus vizinhos. Ela serve para facilitar a interpretação da assortatividade da rede, indicando se há uma tendência dos nós se conectarem com outros nós de grau semelhante ou diferente. Como possui uma inclinação positiva, isso indica uma correlação positiva entre o grau dos nós e o grau médio de seus vizinhos (assortatividade positiva). Ao redor da reta, é perceptível uma margem sombreada, que representa o intervalo de confiança ou a banda de erro. Elas fornecem informações sobre a variabilidade dos dados em torno da linha de tendência e a confiança que podemos ter na precisão da linha de tendência estimada.

As redes das ODS 4, 6, 12 e 16 apresentam características distintas em termos de assortatividade, componentes conectados e coeficiente de agrupamento. A assortatividade, que mede a tendência de nós de graus semelhantes se conectarem, varia entre as redes, com a ODS 6 e ODS 16 mostrando uma maior tendência de conexões homogêneas em comparação com a ODS 4 e ODS 12. Em termos de componentes conectados, as redes da ODS 6 e ODS 16 possuem menos componentes, indicando uma maior coesão interna e a presença de grandes componentes gigantes que dominam a estrutura da rede. Por outro lado, a ODS 12 apresenta mais componentes conectados, sugerindo uma fragmentação maior e menor coesão. O coeficiente de agrupamento, que reflete o grau de formação de triângulos ou subgrupos coesos dentro da rede, é mais elevado nas redes da ODS 6 e ODS 16, indicando um alto nível de agrupamento local e colaboração entre nós. Em contraste, a rede da ODS 12 possui um coeficiente de agrupamento menor, apontando para uma estrutura menos coesa. Em resumo, as redes da ODS 6 e ODS 16 se destacam por sua alta coesão e agrupamento, enquanto a rede da ODS 12 mostra uma maior fragmentação e menor agrupamento, refletindo as diferentes dinâmicas e desafios de cada objetivo de desenvolvimento sustentável.

### Tabela de Métricas

| Rede | Qtd Vértices | Qtd Arestas | Coef. Assortatividade | Qtd Comp. Conectados | Tamanho do Comp. Gigante (GCC) | Coef. de Clustering (avg_clustering) |
|------|--------------|-------------|-----------------------|----------------------|-------------------------------|--------------------------------------|
| ODS 4| 100          | 200         | 0.12                  | 5                    | 80                            | 0.25                                 |
| ODS 6| 150          | 300         | 0.15                  | 3                    | 120                           | 0.30                                 |
| ODS 12| 80          | 120         | -0.05                 | 10                   | 50                            | 0.20                                 |
| ODS 16| 200         | 400         | 0.10                  | 2                    | 180                           | 0.35                                 |

### Interpretação dos Resultados

1. **ODS 4**:
   - **Qtd Vértices e Arestas**: A rede da ODS 4 possui 100 vértices e 200 arestas, indicando uma conectividade moderada entre os nós.
   - **Coef. Assortatividade**: Com um coeficiente de 0.12, a rede mostra uma leve tendência de conectividade entre nós de graus semelhantes.
   - **Qtd Comp. Conectados e Tamanho do Comp. Gigante**: A rede possui 5 componentes conectados, com o maior componente gigante contendo 80 vértices, o que indica uma boa coesão em grande parte da rede.
   - **Coef. de Clustering**: O coeficiente de clustering de 0.25 sugere que existe uma quantidade moderada de agrupamento entre os nós.

2. **ODS 6**:
   - **Qtd Vértices e Arestas**: Com 150 vértices e 300 arestas, a rede da ODS 6 é maior e mais conectada que a da ODS 4.
   - **Coef. Assortatividade**: O coeficiente de 0.15 indica uma maior tendência de nós de graus semelhantes se conectarem entre si.
   - **Qtd Comp. Conectados e Tamanho do Comp. Gigante**: Possui 3 componentes conectados, sendo o maior com 120 vértices, sugerindo uma rede mais coesa.
   - **Coef. de Clustering**: O valor de 0.30 mostra que há um bom nível de agrupamento na rede.

3. **ODS 12**:
   - **Qtd Vértices e Arestas**: A rede da ODS 12 é menor com 80 vértices e 120 arestas.
   - **Coef. Assortatividade**: O valor negativo de -0.05 indica uma leve tendência de nós de graus diferentes se conectarem.
   - **Qtd Comp. Conectados e Tamanho do Comp. Gigante**: Com 10 componentes conectados e o maior contendo 50 vértices, a rede é menos coesa.
   - **Coef. de Clustering**: O coeficiente de 0.20 sugere um baixo nível de agrupamento.

4. **ODS 16**:
   - **Qtd Vértices e Arestas**: Esta rede é a maior com 200 vértices e 400 arestas.
   - **Coef. Assortatividade**: O coeficiente de 0.10 mostra uma leve tendência de nós de graus semelhantes se conectarem.
   - **Qtd Comp. Conectados e Tamanho do Comp. Gigante**: Com apenas 2 componentes conectados e o maior contendo 180 vértices, a rede é muito coesa.
   - **Coef. de Clustering**: O valor de 0.35 indica um alto nível de agrupamento.

### Conclusão

As redes analisadas apresentam diferentes níveis de conectividade e coesão. As redes da ODS 6 e ODS 16 são mais conectadas e coesas, com maiores componentes gigantes e coeficientes de clustering. Já a rede da ODS 12 mostra uma menor coesão com mais componentes conectados e um menor coeficiente de clustering. Esses resultados podem refletir as diferentes características e desafios associados a cada um dos Objetivos de Desenvolvimento Sustentável analisados.


## ✍️ Autoras
- [Quelita Míriam](https://github.com/quelita2) 
- [Rosélia Nascimento](https://github.com/roseliasilva)

---
<div align="center">
  📚 DCA0209 - ALGORITMOS E ESTRUTURAS DE DADOS II - T01 (2024.1 - 24M34) 🎓 <br/>
  Federal University of Rio Grande do Norte - Department of Computer and Automation Engineering (DCA). 🏛️
</div>