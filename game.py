import random #


def choose_options():
  options = ("piedra", "papel", "tijera")
  user = input("Ingrese piedra, papel o tijera: ")
  user = user.lower()
  if not user in options:
     print("Opcion invalida")
     return None, None
  computer = random.choice(options) #elige aleatoriamente
  print("El usuario eligio:", user)
  print("La computadora eligio:", computer)
  return user, computer


def rules(user, computer, contador_user ,contador_computer):
  if user == computer:
    print("Empate")
  elif user == "piedra" and computer == "tijera":
    print("Ganaste esta ronda")
    contador_user += 1
  elif user == "piedra" and computer == "tijera":
    print("Ganaste esta ronda")
    contador_user += 1
  elif user == "papel" and computer == "piedra":
    print("Ganaste esta ronda")
    contador_user += 1
  elif user == "tijera" and computer == "papel":
    print("Ganaste esta ronda")
    contador_user += 1
  else:
    print("Perdiste esta ronda")
    contador_computer += 1
  return contador_user, contador_computer
  

def game():
  contador_user = 0
  contador_computer = 0
  round = 1
  while True:
    print(" " * 100)
    print("ROUND", round)
    print(" " * 100)
    round +=1
    user, computer = choose_options()
    contador_user, contador_computer = rules(user, computer, contador_user ,contador_computer)
    if contador_user == 2:
      print("Ganaste el partido!")
      break
    if contador_computer == 2:
      print("Dedicate a otra cosa")
      break

game()