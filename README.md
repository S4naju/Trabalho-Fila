# Trabalhos sobre Filas no Python

### Sobre o projeto:
Estes projetos foram desenvolvidos como parte da disciplina Estrutura de Dados no IFRJ - Niterói, com o objetivo de aplicar na prática os conceitos de filas em Python, para entender melhor como elas funcionam e como manipular dados usando esse tipo de estrutura.

Uma **fila** é uma estrutura de dados do tipo ***FIFO (First In, First Out)***, ou seja, o primeiro elemento a entrar é o primeiro a sair. Exemplos de filas na prática: fila de cinema, supemercado, médico...

---

### Estrutura orientada pelo professor:

1. **Trabalho 1: Fila usando `queue.Queue`**  
   Foi criada uma classe `Fila` como um wrapper da classe `Queue` do Python, facilitando o uso de filas com controle de tamanho.
   
   **Funcionalidades:**
   - Define tamanho máximo da fila  
   - Insere e remove itens facilmente
   - Verifica se a fila está cheia ou vazia
   - Mostra tamanho atual e máximo

2. **Trabalho 2: Fila sem dependências externas**  
   Foi implementada uma classe `Fila` do zero, sem uso de bibliotecas, com toda a lógica de controle feita manualmente.
   
   **Funcionalidades:**
   - Define tamanho máximo da fila
   - Insere e remove itens com validação
   - Evita inserção em fila cheia e remoção em fila vazia
   - Mostra tamanho atual e máximo

---

### Diferenças entre os trabalhos:
- **Trabalho 1:** mais prático, utiliza a `Queue` pronta do Python e abstrai a lógica interna.  
- **Trabalho 2:** implementa a fila manualmente, permitindo compreender detalhadamente como a estrutura funciona.

---

### Autora:
**Ana Julia Sampaio**

Disciplina: **Estrutura de Dados**

Instituto Federal do Rio de Janeiro – **Campus Niterói**
