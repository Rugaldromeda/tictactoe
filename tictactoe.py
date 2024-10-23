import os

dict_tabuleiro = [
    {"piece": i + 1, "played": False, "player": None} 
    for i in range(9)
]

jogo_finalizado = None

def checkFimJogo():
    finalizado = all(item["played"]==True for item in dict_tabuleiro)
    if finalizado == True:
        print("Empate!")
    return finalizado
    
def vezJogador(jogada,vezJogador,jogador):
    if dict_tabuleiro[jogada-1]["played"] == False:
            dict_tabuleiro[jogada-1]["piece"] = vezJogador
            dict_tabuleiro[jogada-1]["played"] = True
            dict_tabuleiro[jogada-1]["player"] = jogador
    else:
        print("Este espaço já foi jogado, por favor escolha outro!")

    verificaIndices(jogador)

def checkVitoria(list, player):
    listPattern = [dict_tabuleiro[list[0]]["player"],dict_tabuleiro[list[1]]["player"], dict_tabuleiro[list[2]]["player"]]
    checkVic = all(i == player for i in listPattern)

    return checkVic

def verificaIndices(player):
    global dict_tabuleiro
    global jogo_finalizado
    indVictory = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[6,4,2],[0,3,6],[1,4,7],[2,5,8]]
    for i in range(len(indVictory)):
        indVic = indVictory[i]
        victory = checkVitoria(indVic,player)
        if victory == True:
            print("Jogador {} ganhou!".format(player))
            jogo_finalizado = True
            break

def atualizaTabuleiro():
    global tabuleiro_pecas
    listFormat = [dict_tabuleiro[i]["piece"] for i in range(len(dict_tabuleiro))]

    tabuleiro_pecas = "_{}|_{}|_{}\n_{}|_{}|_{}\n {}| {}| {}".format(*listFormat)

    print(tabuleiro_pecas)

def jogando():
    print("Bem vindo ao jogo da velha!")

    vezJogada = None
    choicePlayer1 = int(input("Jogador 1, por favor escolha sua peça! \n 1 - X  2 - o :"))

    if choicePlayer1 == 1:
        vezJogada = "X"
    else:
        vezJogada = "o"

    print("Você escolheu a peça {}! \n Escolha um número pra indicar onde quer jogar".format(vezJogada))

    atualizaTabuleiro()
    global dict_tabuleiro

    checkFim = False
    jogador = 1

    while not checkFim:
        
        print("Jogador {}!".format(jogador))
        jogada = int(input(" Insira sua jogada:  "))

        os.system('cls') or None
        global tabuleiro_pecas
        
        vezJogador(jogada,vezJogada, jogador)

        if vezJogada == "o":
            vezJogada = "X"
        else:
            vezJogada = "o"
        
        if jogador == 1:
            jogador = 2
        else:
            jogador = 1 

        atualizaTabuleiro()
        
        checkFim = checkFimJogo()
        verificaIndices(jogador)
        if jogo_finalizado == True:
            checkFim = True
            
    print("Fim de jogo!")

jogando()