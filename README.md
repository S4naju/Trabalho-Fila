# Trabalhos sobre Filas no Python

### Sobre o projeto:
Estes projetos foram desenvolvidos como parte da disciplina Estrutura de Dados no IFRJ - Niterói, com o objetivo de aplicar na prática os conceitos de filas em Python, para entender melhor como elas funcionam e como manipular dados usando esse tipo de estrutura.

Uma **fila** é uma estrutura de dados do tipo ***FIFO (First In, First Out)***, ou seja, o primeiro elemento a entrar é o primeiro a sair. Alguns exemplos de filas na prática: fila de cinema, supemercado, médico...

---

### Estrutura orientada pelo professor:

1. **Trabalho 1: Fila usando `queue.Queue`**  
   Neste trabalho, foi criada uma classe chamada `Fila` que funciona como um wrapper para a classe `Queue` do Python. A ideia é facilitar o uso da fila e permitir que o usuário defina o tamanho máximo, insira e remova itens de forma simples.
   
   **Funcionalidades:**
   - Pergunta ao usuário o tamanho máximo da fila.  
   - Permite inserir quantos itens quiser, dentro do limite da fila.  
   - Permite remover itens do início da fila.  
   - Mostra se a fila está cheia ou vazia.  
   - Mostra o tamanho atual da fila e o tamanho máximo.

2. **Trabalho 2: Fila sem dependências externas**  
   Neste trabalho, foi criada uma classe chamada `Fila` totalmente do zero, sem utilizar bibliotecas externas. A ideia foi implementar a lógica da fila manualmente,  incluindo verificação de limites e tratamento de erros caso o usuário tente inserir demais ou remover de uma fila vazia.
   
   **Funcionalidades:**
   - Pergunta ao usuário o tamanho máximo da fila.  
   - Permite inserir e remover itens da fila, verificando os limites.  
   - Mostra se a fila está cheia ou vazia.  
   - Mostra o tamanho atual da fila e o tamanho máximo.

---

### Diferenças entre os trabalhos:
- **Trabalho 1:** mais prático, utiliza a `Queue` pronta do Python e abstrai a lógica interna.  
- **Trabalho 2:** implementa a fila manualmente, permitindo compreender detalhadamente como a estrutura funciona.

---

### Como usar:

Basta rodar o arquivo Python correspondente a cada trabalho. O programa interage com você, pedindo os itens a inserir e quantos deseja remover, mostrando sempre o estado atual da fila.

---

### Autora:
**Ana Julia Sampaio**

Disciplina: **Estrutura de Dados**

Instituto Federal do Rio de Janeiro – **Campus Niterói**
