# -*- uncoding: utf-8 -*-

# variaveis globais
p = "Folha de Papel"
cl = "Caixa de Lápis"
c = "Caderno"
s = "Sair"
choosen = 0

class Produto:

    # função
    def menu_cadastro(self):
        print("==============================")
        print("== Loft Papelaria Cadastro  ==")
        print("==============================")
        print("  --------------------------")
        print("  ||%17s(1)  ||" % p)
        print("  ||%17s(2)  ||" % cl)
        print("  ||%13s(3)      ||" % c)
        print("  ||%12s(4)       ||" % s)
        print("  --------------------------")
        prod = Produto
        choosen = prod.choosen(prod)
        prod.verify(choosen)

    def choosen(self):
        escolha = int(input("Informe o indice de sua escolha: "))
        while True:
            if(escolha == 1):
                print("\nCarregando arquivos de Folhas de Papel!")
                return escolha
                break
            elif(escolha == 2):
                print("\nCarregando arquivos das Caixas de Lápis!")
                return escolha
                break
            elif (escolha == 3):
                print("\nCarregando arquivos de Cadernos!")
                return escolha
                break
            elif(escolha == 4):
                print("\nVoltando ao Menu Inicial!")
                return escolha
                break
            else:
                print("Opção invalida!\nPor favor informar um opção valida de acordo com os indices!")
                escolha = int(input("Informe o indice de sua escolha: "))

    def verify(escolha):
        if(escolha == 1):
            print("Escolheu Cadastro de Papeis!\n")
        elif(escolha == 2):
            print("Escolheu Cadastro de Caixas de Lapis!\n")
        elif (escolha == 3):
            print("Escolheu Cadastro de Cadernos!\n")
        elif (escolha == 4):
            print("Escolheu retornar ao menu inicial!\n")
            importacao()
        else:
            print("Opção invalida!\nIremos retornar ao menu Inicial!\n")

def importacao():
    from Main import Menu
    m = Menu
    m.menu(m)
"""if __name__ == '__main__':
    prod = Produto
    prod.menu_cadastro(prod)"""