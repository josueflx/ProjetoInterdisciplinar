# -*- uncoding: utf-8 -*-

from produtos.Papeis import Papel
from produtos.Caderno import Caderno
from produtos.CaixaLapis import CaixaLapis

# variaveis globais
p = "Folha de Papel"
cl = "Caixa de Lápis"
c = "Caderno"
s = "Retornar"
choosen = 0
papel = Papel
caderno = Caderno
caixaLapis = CaixaLapis

class Visualiza():

    # função
    def menu_cadastro(self):
        print("==============================")
        print("== Loft Papelaria Exibição  ==")
        print("==============================")
        print("  --------------------------")
        print("  ||%17s(1)  ||" % p)
        print("  ||%17s(2)  ||" % cl)
        print("  ||%13s(3)      ||" % c)
        print("  ||%13s(4)      ||" % s)
        print("  --------------------------")
        view = Visualiza
        choosen = view.choosen(view)
        view.verify(choosen)

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
                return escolha
                break
            else:
                print("Opção invalida!\nPor favor informar um opção valida de acordo com os indices!")
                escolha = int(input("Informe o indice de sua escolha: "))

    def verify(escolha):
        v = Visualiza
        if(escolha == 1):
            print("\nCarregando arquivos de Visualização de Papeis!\n")
            papel.visualiza(papel, "papeis")
            v.menu_cadastro(v)
        elif(escolha == 2):
            print("\nCarregando arquivos de Visualização de Caixas de Lapis!\n")
            caixaLapis.visualiza(caixaLapis, "caixaLapis")
            v.menu_cadastro(v)
        elif (escolha == 3):
            print("\nCarregando arquivos de Visualização de Cadernos!\n")
            caderno.visualiza(caderno, "cadernos")
            v.menu_cadastro(v)
        elif (escolha == 4):
            print("\nEscolheu retornar ao menu inicial!\n")
            retornar()
        else:
            print("\nOpção invalida!\nIremos retornar ao menu Inicial!\n")

def retornar():
    from Main import Menu
    m = Menu
    m.menu(m)