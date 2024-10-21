import os
tabuleiro = "_1|_2|_3\n_4|_5|_6\n 7| 8| 9" 
# aplicar compreensão em dicionário
dict_tabuleiro = [
    {"piece":1,"played":False},
    {"piece":2,"played":False},
    {"piece":3,"played":False},
    {"piece":4,"played":False},
    {"piece":5,"played":False},
    {"piece":6,"played":False},
    {"piece":7,"played":False},
    {"piece":8,"played":False},
    {"piece":9,"played":False},
]


def checkFimJogo():
    fim = all(item["played"]==True for item in dict_tabuleiro)
    return fim
    
def vezJogador(jogada,vezJogador):
    if dict_tabuleiro[jogada-1]["played"] == False:
            dict_tabuleiro[jogada-1]["piece"] = vezJogador
            dict_tabuleiro[jogada-1]["played"] = True
    else:
        print("Este espaço já foi jogado, por favor escolha outro")


def alteraTabuleiro():
    global tabuleiro_pecas
    listFormat = [
        dict_tabuleiro[0]["piece"],
        dict_tabuleiro[1]["piece"],
        dict_tabuleiro[2]["piece"],
        dict_tabuleiro[3]["piece"],
        dict_tabuleiro[4]["piece"],
        dict_tabuleiro[5]["piece"],
        dict_tabuleiro[6]["piece"],
        dict_tabuleiro[7]["piece"],
        dict_tabuleiro[8]["piece"]
    ]

    tabuleiro_pecas = "_{}|_{}|_{}\n_{}|_{}|_{}\n {}| {}| {}".format(*listFormat)

alteraTabuleiro()

print(tabuleiro_pecas)

def jogando():
    global dict_tabuleiro

    checkFim = False
    vezJogada = "X"    
    while checkFim==False:

        jogada = int(input(" Insira sua jogada:  "))
        os.system('cls') or None
        global tabuleiro_pecas
        
        vezJogador(jogada,vezJogada)

        if vezJogada == "O":
            vezJogada = "X"
        else:
            vezJogada = "O"
        
        alteraTabuleiro()
        #tabuleiro = tabuleiro.replace("{}".format(jogada),"O")

        print(tabuleiro_pecas)
        checkFim = checkFimJogo()


jogando()