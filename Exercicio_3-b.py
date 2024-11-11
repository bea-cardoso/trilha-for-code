import random

def escolha_do_player1():
    player1 = input("Escolha entre pedra, papel ou tesoura: ")
    
    while player1 not in ["pedra", "tesoura", "papel"]:
       print("Escolha inválida! Escolher entre pedra, papel ou tesoura.")
       player1 = input("Escolha entre pedra, papel ou tesoura: ")
    
    return player1

#escolha do computador
def escolha_do_player2():
   player2 = random.choice(["pedra", "papel", "tesoura"])
   print("Eu escolho: " + player2)
   return player2

def jogando():   
#variaveis de vitoria e derrota do player1
    n = 0  #vitórias
    m = 0  #derrotas

#loop até que o player1 tenha 3 vitorias ou 3 derrotas
    while n < 3 and m < 3:
        player1 = escolha_do_player1() # chamar uma função para executá-la e obter o resultado, 
                                       #precisa colocar os parênteses ().
        player2 = escolha_do_player2()
    
    #fazendo o loop
        if player1 == player2:
            print("Deu Empate")
        elif (player1 == "pedra" and player2 == "tesoura") or (player1 == "papel" and player2 == "pedra") or (player1 == "tesoura" and player2 == "papel"):
            print("Vitória")
            n = n + 1
        else:
            print("Derrota")
            m = m + 1

#resultados final
    print("Vitórias: " + str(n))
    print("Derrotas:", m) 

jogando()