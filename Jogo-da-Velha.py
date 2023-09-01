import random

#Função que irá mostrar um menu onde o jogador deve escolher qual modo de jogo ele quer
def imprimeMenuPrincipal():
    while True:
        escolha = int(input("Escolha o modo de jogo. Usuario x Usuario(1) e Usuario x Maquina(2) \nR: "))
        match escolha:
            case 1:
                resultado = modoJogador()
                imprimePontuacao(resultado)
            case 2:
                resultado = modofacil()
                imprimePontuacao(resultado)
            case 0:
                print("Encerrando o programa...")
            case _:
                print("Número Inválido!")

#Função que irá iniciar o tabuleiro para consequentemente mostrar para o jogador
def inicializarTabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


#Função que irá mostrar o tabuleiro para o jogador
def imprimirTabuleiro(tabuleiro):
    print("   0   1   2")
    print("0: " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("  ---|---|---")
    print("1: " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("  ---|---|---")
    print("2: " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])


#Função que irá ler o que o usuário digitou para linha
def leiaCoordenadaLinha():
    return int(input("Escolha a linha (0, 1, 2): "))


#Função que irá ler o que o usuário digitou para coluna
def leiaCoordenadaColuna():
    return int(input("Escolha a coluna (0, 1, 2): "))


#Função que irá identificar se a posição que o jogador digitou está ocupada
def posicaoValida(tabuleiro, linha, coluna):
    if 0 <= linha < 3 and 0 <= coluna < 3:
        return tabuleiro[linha][coluna] == " "
    return False


#Função que irá receber as informações que o usúario digitou, como linha e coluna
def jogar(tabuleiro,linha , coluna, jogador):
    tabuleiro[linha][coluna] = jogador


#Função que irá verificar o tabuleiro e ver se alguém saiu como vencedor
def verificaVencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(elemento == jogador for elemento in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False


#Verifica se deu velha no jogo
def verificaVelha(tabuleiro):
    return all(elemento != " " for linha in tabuleiro for elemento in linha)


#Função que calcula a pontuação com base no resultado da rodada
def calcularPontuacao(resultado, pontuacao_x, pontuacao_o):
    if resultado == "X":
        pontuacao_x += 1
    elif resultado == "O":
        pontuacao_o += 1
    return pontuacao_x, pontuacao_o


#Função que verifica se alguém atingiu 3 vitórias
def verificaVitoria(pontuacao_x, pontuacao_o):
    return pontuacao_x >= 3 or pontuacao_o >= 3


#Função que permite que o usuário faça uma jogada
def jogadaUsuario(tabuleiro, jogador_atual):
    while True:
        imprimirTabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é a sua vez!")
        linha = leiaCoordenadaLinha()
        coluna = leiaCoordenadaColuna()

        if posicaoValida(tabuleiro, linha, coluna):
            jogar(tabuleiro, linha, coluna, jogador_atual)
            break
        else:
            print("Posição inválida. Tente novamente.")


#Função que permite que o computador faça uma jogada aleatória
def jogadaComputador(tabuleiro, jogador_atual):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)

        if posicaoValida(tabuleiro, linha, coluna):
            print(f"Computador escolheu a posição ({linha}, {coluna}).")
            jogar(tabuleiro, linha, coluna, jogador_atual)
            break


#Função Principal do Jogador, onde irá utilizar as funções criadas
def modoJogador():
    pontuacao_x = 0
    pontuacao_o = 0

    while True:
        tabuleiro = inicializarTabuleiro()
        jogador_atual = "X"

        while True:
            jogadaUsuario(tabuleiro, jogador_atual)

            if verificaVencedor(tabuleiro, jogador_atual):
                imprimirTabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu a rodada!")
                resultado = jogador_atual
                pontuacao_x, pontuacao_o = calcularPontuacao(resultado, pontuacao_x, pontuacao_o)
                jogador_atual = "X"
                break
            elif verificaVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("A rodada terminou em empate!")
                resultado = "Empate"
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        if verificaVitoria(pontuacao_x, pontuacao_o):
            break

    return "X" if pontuacao_x >= 3 else "O"


#Função Principal do Jogador vs Computador
def modofacil():
    pontuacao_x = 0
    pontuacao_o = 0

    while True:
        tabuleiro = inicializarTabuleiro()
        jogador_atual = "X"

        while True:
            if jogador_atual == "X":
                jogadaUsuario(tabuleiro, jogador_atual)
            else:
                jogadaComputador(tabuleiro, jogador_atual)

            if verificaVencedor(tabuleiro, jogador_atual):
                imprimirTabuleiro(tabuleiro)
                if jogador_atual == "X":
                    print("Você venceu a rodada!!!!")
                    resultado = jogador_atual
                    pontuacao_x, pontuacao_o = calcularPontuacao(resultado, pontuacao_x, pontuacao_o)
                    jogador_atual = "X"
                    break
                else:
                    print("O computador venceu!!!!")
                    resultado = jogador_atual
                    pontuacao_x, pontuacao_o = calcularPontuacao(resultado, pontuacao_x, pontuacao_o)
                    jogador_atual = "X"
                break
            elif verificaVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("A rodada terminou em empate!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"
        if verificaVitoria(pontuacao_x, pontuacao_o):
            break

    return "X" if pontuacao_x >= 3 else "O"


#Função para exibir o resultado após o jogo
def imprimePontuacao(resultado):
    print(f"Fimmmm de Jogo! Entreguem os trofeus, o Jogador {resultado} venceu!")


#Principal
imprimeMenuPrincipal()
