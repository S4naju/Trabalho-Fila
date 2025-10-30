class Fila:
    def __init__(self):
        self.fila = []
        print("--- BEM VINDO AO CRIADOR DE FILAS ---")
        while True:
            try:
                tam = int(input("qual o tamanho máximo da sua fila? "))
                if tam < 0:
                    print("digite um número maior ou igual a zero!\n")
                    continue
                self.maxsize = tam 
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
                if self.maxsize != 0 and quantItens > self.maxsize:
                    print("não pode ultrapassar o tamanho máximo da fila!\n")
                else:
                    for i in range(quantItens):
                        itens = input(f"digite o {i+1}º item da sua lista: ")
                        self.fila.append(itens)
                        print(list(self.fila))
                    break
            except ValueError:
                    print("por favor, digite um valor válido!")

    def remover(self):
        while True:
            try:
                tamanho= len(self.fila)
                if tamanho == 0:
                    print("não da pra remover itens, a fila está vazia!\n")
                    break
                remove = int(input("\nquantos item da sua fila você deseja remover? "))
                if remove == 0:
                    print("sem remoções na lista!\n")
                    break
                if remove > tamanho:
                    print(f"a fila so tem {tamanho} itenns! tente novamente!\n")
                    continue
                for i in range(remove):
                    print(f"item removido da fila: {self.fila.pop(0)}")
                    print(list(self.fila))
                break
            except ValueError:
                print("por favor, digite um número válido!\n")

    def cheia(self):
        tamanho= len(self.fila)
        if tamanho >= self.maxsize:
            print("\na fila está cheia!")
            print(list(self.fila))
        else:
            print("\na fila não está cheia!")
            print(list(self.fila))

    def vazia(self):
        tamanho= len(self.fila)
        if tamanho == 0:
            print("\na fila está vazia!")
            print(list(self.fila))
        else:
            print("\na fila não está vazia!")
            print(list(self.fila))

    def tamanho(self):
        print(f"\no tamanho da fila é de: {len(self.fila)}")
        print(list(self.fila))

    def tamMaximo(self):
        if self.maxsize == 0:
            print("\no tamanho máximo da fila é ilimitado!")
        else:
            print(f"\no tamanho máximo da fila é: {self.maxsize}")
        print(list(self.fila))

filas = Fila() # instancia
filas.inserir() # chamando o método
filas.remover()
filas.cheia()
filas.vazia()
filas.tamanho()
filas.tamMaximo()
