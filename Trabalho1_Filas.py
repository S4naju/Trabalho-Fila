from queue import Queue as que
class Fila:
    def __init__(self):
        self.fila = que()
        print("--- BEM VINDO AO CRIADOR DE FILAS ---")
        while True:
            try:
                tam = int(input("qual o tamanho máximo da sua fila? "))
                if tam < 0:
                    print("digite um número maior ou igual a zero!\n")
                    continue
                self.fila = que(maxsize=tam)
                if tam == 0:
                    print("você criou uma fila ilimitada!\n")
                else:
                    print(f"você criou uma fila com tamanho máximo de {tam}!\n")
                break
            except ValueError:
                print("por favor, digite um número válido!\n")

    def inserir(self):
        while True:
            try:
                quantItens = int(input("quantos itens você deseja adicionar? "))
                if self.fila.maxsize != 0 and quantItens > self.fila.maxsize:
                    print("não pode ultrapassar o tamanho máximo da fila!\n")
                else:
                    for i in range(quantItens):
                        itens = input(f"digite o {i+1}º item da sua lista: ")
                        self.fila.put(itens)
                        print(list(self.fila.queue))
                    break
            except ValueError:
                    print("por favor, digite um valor válido!")

    def remover(self):
        while True:
            try:
                if self.fila.empty():
                    print("não da pra remover itens, a fila está vazia!\n")
                    break
                remove = int(input("quantos item da sua fila você deseja remover? "))
                if remove == 0:
                    print("sem remoções na lista!\n")
                    break
                if remove > self.fila.qsize():
                    print(f"a fila so tem {self.fila.qsize} itenns! tente novamente!\n")
                    remove = self.fila.qsize()
                    continue
                for i in range(remove):
                    print(f"item removido da fila: {self.fila.get()}")
                    print(list(self.fila.queue))
                break
            except ValueError:
                print("por favor, digite um número válido!\n")

    
    def cheia(self):
        if self.fila.full() == True:
            print("\na fila está cheia!")
            print(list(self.fila.queue))
        else:
            print("\na fila não está cheia!")
            print(list(self.fila.queue))

    def vazia(self):
        if self.fila.empty() == True:
            print("\na fila está vazia!")
            print(list(self.fila.queue))
        else:
            print("\na fila não está vazia!")
            print(list(self.fila.queue))

    def tamanho(self):
        print(f"\no tamanho da fila é de: {self.fila.qsize()}")
        print(list(self.fila.queue))

    def tamMaximo(self):
        if self.fila.maxsize == 0:
            print("\no tamanho máximo da fila é ilimitado!")
        else:
            print(f"\no tamanho máximo da fila é: {self.fila.maxsize}")
        print(list(self.fila.queue))

filas = Fila() # instancia
filas.inserir() # chamando o método
filas.remover()
filas.cheia()
filas.vazia()
filas.tamanho()
filas.tamMaximo()
