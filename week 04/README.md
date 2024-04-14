# Complexidade das diferentes operações na Árvore de Busca Binária (BST)

## 🛠️ Instruções de Execução

1. Certifique-se de ter Python instalado em seu sistema.
2. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/quelita2/aedii.git
```

3. Navegue até o diretório do projeto:
```bash
cd aedii
```

4. Execute o arquivo de teste para verificar se a solução está funcionando corretamente:
```bash
pytest
```

## 🎯 Challenge 01: Encontrar o valor mais próximo

Este é um algoritmo Python para encontrar o valor mais próximo de um valor alvo em uma Árvore de Pesquisa Binária (BST).

### Descrição da Solução

A solução consiste em uma função chamada `findClosestValue(tree, target)`, que recebe uma árvore de pesquisa binária (BST) e um valor alvo como entrada e retorna o valor na BST que está mais próximo do valor alvo.

O algoritmo começa a busca pelo valor mais próximo a partir do nó raiz da árvore de busca binária. Ele trabalha de forma iterativa, explorando a árvore e estreitando a busca com base no valor alvo e no valor atual do nó. O valor mais próximo é constantemente atualizado durante o processo de busca.

### Complexidade do Algoritmo
A complexidade de tempo do algoritmo é O(h), onde h é a altura da árvore de pesquisa binária. No melhor caso, quando a árvore está perfeitamente balanceada, a complexidade de tempo é O(log n), onde n é o número de nós na árvore. No pior caso, quando a árvore é desbalanceada, a complexidade de tempo pode ser O(n), onde n é o número de nós na árvore.

A complexidade de espaço é O(1), pois o algoritmo utiliza apenas uma quantidade constante de espaço adicional para armazenar variáveis locais e recursivas.

## 🎯 Challenge 02: Encontre o k-ésimo maior termo em uma Árvore Binária de Busca (BST)

Este desafio consiste em encontrar o k-ésimo maior inteiro em uma Árvore Binária de Busca (BST).

### Descrição da Solução

O código utiliza uma abordagem de travessia em ordem reversa para coletar os valores dos nós da árvore em uma lista ordenada. Em seguida, ele retorna o k-ésimo maior valor dessa lista. A BST é assumida como contendo apenas valores inteiros, e valores duplicados são tratados como distintos para determinar o k-ésimo maior inteiro.

### Complexidade do Algoritmo

A complexidade do algoritmo pode ser expressa como O(h + k), onde h é a altura da árvore a ser percorrida. No pior caso, quando a árvore é percorrida completamente em ordem reversa, a complexidade é O(n), onde n é o número total de nós na árvore. No entanto, em média, a complexidade é menor, com uma média de O(log n), onde n é o número total de nós na árvore. Isso ocorre porque, em média, apenas uma fração da árvore é percorrida em ordem reversa, dependendo do valor de k e da distribuição dos nós na árvore.

---
<div align="center">
Feito com ❤ por <a href="https://github.com/quelita2" target="_blank">Quelita Míriam </a> e <a href="https://github.com/roseliasilva" target="_blank">Rosélia Nascimento </a> 👩🏼‍💻
</div>
