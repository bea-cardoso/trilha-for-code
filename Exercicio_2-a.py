import random

#variaveis de vitoria e derrota do player1
n = 0  #vitórias
m = 0  #derrotas

#loop até que o player1 tenha 3 vitorias ou 3 derrotas

while n < 3 and m < 3:    # Assim que n ou m atinge 3, a condição proposta se torna falsa, o que faz com que o loop pare.
  player1 = input ("Escolha entre pedra, papel ou tesoura: ")

  #verificar se a respsota é valida
  while player1 not in ["pedra", "tesoura", "papel"]:
    print("Escolha inválida! Escolher entre pedra, papel ou tesoura.")
    player1 = input("Escolha entre pedra, papel ou tesoura: ")

  
 
  lista1 = ["pedra", "papel", "tesoura"]
 
  player2 = random.choice(lista1)
 
  print("Eu escolho: " + player2)
 
  if player1 == player2:
    print("Deu Empate")
  elif (player1 == "pedra" and player2 == "tesoura") or (player1 == "papel" and player2 == "pedra") or (player1 == "tesoura" and player2 == "papel"):
    print("Vitória")
    n = n + 1
  else:
    print("Derrota")
    m = m + 1
#exibi o resultado final
print("Vitórias: " + str(n)) # e a mesma coisa que botar como está em baixo
print("Derrotas:", m )