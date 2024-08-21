# Trabalho final - Unidade 3

- **Requisito 1:** Gerar uma rede (grafo) dirigida a partir dos links das páginas do Wikipédia considerando a fusão de 3 SEEDs (páginas iniciais). 

- **Requisito 2:** A partir da rede construída gerar uma figura que destaque as propriedades de centralidade da rede utilizando o Gephi, tais como degree centrality, closeness centrality, betweness centraliy e eigenvector centrality. 

- **Requisito 3:** A partir da rede construída gerar uma figura que contenha os gráficos da Cumulative Density Function (CDF) e Probability Density Function (PDF) considerando o in-Degree dos vértices da rede.

- **Requisito 4:** A partir da rede construída gerar uma figura similar no gephi destacando o k-core e o k-shell da rede. O layout é de livre escolha. Os vértices devem ter um tamanho proporcional a propriedade in-degree.

- **Requisito 5:** A rede deverá estar em produção. As cores deverão ser relacionadas ao critério de comunidade e o tamanho do vértice a métrica in-degree.

## Requisito 1

As páginas Wikipedia escolhidas para a construção da rede do trabalho:

- [Telehelth](https://en.wikipedia.org/wiki/Telehealth)
- [Electronic health record](https://en.wikipedia.org/wiki/Electronic_health_record)
- [Health information exchange](https://en.wikipedia.org/wiki/Health_information_exchange)

Utilizou-se o algoritmo disponibilizado pelo professor para transformar essas páginas do Wikipedia em uma rede direcionada e, após usar rotinas do NetworkX para uni-las em uma única rede, utilizou-se o software Gephi para criar uma visualização dela.

Nessa representação, os **nós** são páginas do Wikipedia e as **arestas** são os links entre as páginas. Como é possível ver, duas estratégias foram utilizadas para essa representação: as cores dos nós  são relacionadas ao critério de comunidade e o tamanho deles à métrica in-degree. Dessa forma, é possível ver na figura que algumas páginas são mais citadas pelas outras.

## Requisito 2

Abaixo, observa-se as imagens que representam as métricas de degree centrality, closeness centrality, betweenness centrality e eigenvector centrality.

| Degree Centrality | Closeness Centrality | Betweeness Centrality | Eigenvector Centrality |
|-------------------|----------------------|----------------------|----------------------|
![Degree centrality](./assets/imgs/degree.png)|![Closeness Centrality](assets/imgs/closeness.png)|![Betweeness Centrality](assets/imgs/betweeness.png)|![Eigenvector Centrality](assets/imgs/eigenvector.png)



- **Degree centrality:** mede o número de conexões diretas de um nó na rede
- **Closeness centrality:** avalia a proximidade de um nó em relação aos demais, considerando o comprimento médio dos caminhos mais curtos
- **Betweenness centrality:** indica a importância de um nó na comunicação entre outros nós, identificando quantos caminhos passam por ele
- **Eigenvector centrality:** atribui importância aos nós com base na qualidade das conexões que possuem, levando em consideração a relevância dos nós aos quais estão conectados

Ao analisar as imagens acima, destacamos que, no **degree centrality**, os nós com maior in degree, são evidenciados. Esses nós pertencem ao grupo de páginas que possuem muitos links apontando para elas. No **closeness centrality**, identificamos os nós mais proeminentes, que acabam ficando mais próxima dos nós da rede. Na prática, isso significa que não precisamos navegar muito tempo no Wikipedia para alcançá-los, desde que as páginas pesquisadas sejam relacionadas aos temas considerados por nós neste trabalho. O **eigenvector centrality** fornece informações sobre a importância de cada nó com base na qualidade de suas conexões em tons mais avermelhados. Esses, quando comparado aos outros, possuem como vizinhos as páginas que mais caracterizam os temas pesquisados na rede. Por fim, o **betweenness centrality** revela a importância de um nó para a navegação entre outros na rede. Ou seja, caso você queira navegar de uma página a outra relacionada a esse tema, é muito provável que você passe por uma dessas páginas.

## Requisito 3

Ao examinar o gráfico, observe que as barras verticais em azul denotam a quantidade de conexões, enquanto a curva em vermelho representa a Função de Densidade de Probabilidade Cumulativa (CDF), à esquerda, e a Função de Densidade de Probabilidade (PDF), à direita. Há uma predominância de conexões de baixo grau, indicando uma quantidade elevada, contrastando com a presença de elementos mais relevantes (graus maiores) em menor quantidade.

| Histograma da rede | 
|--------------------|
![Histograma da rede](./assets/imgs/histogram.png)

| Histograma com CDF | Histograma com PDF | 
|----------------------|----------------------|
![Histograma com CDF](./assets/imgs/histogram_cdf.png)|![Histograma com PDF](assets/imgs/histogram_pdf.png)|

Observando a Função Densidade de Probabilidade (FDP), concluímos que na base de dados utilizada de links da Wikipedia, há poucas páginas sobre os temas pesquisados que concentram um grande número de links direcionados a elas. Logo, essas páginas emergem como as mais relevantes dentro desses tópicos, como evidenciado pelo exemplo da indústria do petróleo, onde a probabilidade de escolher um nó de indegree alto é abaixo de 2%, enquanto para indegrees entre 0 e 50, as probabilidades ultrapassam 10%, sugerindo maior relevância.

Ao analisar a Função de Densidade de Probabilidade Cumulativa (CDF), destaca-se que os nós com graus inferiores a 50 compreendem aproximadamente 90% do conjunto total de dados. Contrapondo essa predominância, identificamos uma parcela ínfima próxima do *in degree* 200, indicando uma concentração de nós considerados mais relevantes. Em resumo, inicialmente, temos uma representação expressiva de graus mais baixos, abrangendo mais de 10% da rede; entretanto, entre 25 e próximo de 50, essa representação diminui drasticamente, com os nós de grau acima de 25 compreendendo menos de 1% da rede. Além disso, os nós com grau superior a 100 constituem menos de 1% da rede de forma acentuada.

## Requisito 4

O k-core é o subconjunto de nós que possuem pelo menos grau k. O k-shell resumidamente, representa o subconjunto de nós removidos para alcançar o próximo k-core. O k-core de uma rede representa os nós mais profundos dela, que formam o que se chama de núcleo. Abaixo estão apresentados o k-core e o k-shell da rede construída.

| k-core | 
|--------|
![k-core](./assets/imgs/k-core.png)

## Requisito 5

A rede construída está em produção no seguinte endereço [Wikipedia Network](https://quelita2.github.io/aedii/)

## ✍️ Autora
- [Quelita Míriam](https://github.com/quelita2) 

---
<div align="center">
  📚 DCA0209 - ALGORITMOS E ESTRUTURAS DE DADOS II - T01 (2024.1 - 24M34) 🎓 <br/>
  Universidade Federal do Rio Grande do Norte - Departamento de Computação e Automação (DCA). 🏛️
</div>