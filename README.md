# Trabalhos sobre Filas no Python

### Sobre o projeto:
Estes projetos foram desenvolvidos como parte da disciplina **Estrutura de Dados** no **IFRJ - Niterói**, com o objetivo de aplicar na prática os conceitos de filas em Python, para entender melhor como elas funcionam e como manipular dados usando esse tipo de estrutura.

---

### Estrutura orientada pelo professor:

1. **Trabalho 1: Fila usando `queue.Queue`**  
   Neste trabalho, foi criada uma classe chamada `Fila` que funciona como um **wrapper** para a classe `Queue` do Python. A ideia era facilitar o uso da fila, sem precisar lidar diretamente com a `Queue`.  
   
   **Métodos implementados:**
   - `__init__()` – construtor da classe.  
   - `inserir(item)` – adiciona um item à fila.  
   - `remover()` – remove e retorna o item do início da fila.  
   - `cheia()` – verifica se a fila está cheia.  
   - `vazia()` –  verifica se a fila está vazia. 
   - `tamanho()` – retorna o número de elementos na fila.  
   - `tamanho_maximo()` – retorna a capacidade máxima da fila.

2. **Trabalho 2: Fila sem dependências externas**  
   Neste trabalho, foi criada uma classe chamada `Fila`totalmente do zero, **sem utilizar bibliotecas externas**. A ideia foi implementar a lógica da fila manualmente, tratando possíveis problemas relacionados à manipulação de dados, utilizando e propagando exceções adequadas.  
   
   **Métodos implementados:**
   - `__init__()` – construtor da classe.  
   - `inserir(item)` – adiciona um item à fila, lançando exceção se a fila estiver cheia.  
   - `remover()` – remove e retorna o item do início da fila, lançando exceção se a fila estiver vazia.  
   - `cheia()` – verifica se a fila está cheia. 
   - `vazia()` –  verifica se a fila está vazia.  
   - `tamanho()` – retorna o número de elementos na fila.
  
