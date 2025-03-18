import random
import os

os.system ("cls")

numerosecreto = random.randint (1,10)
print(numerosecreto)


tentativas =0

jogador = input("Nome do jogador: ")

while tentativas <= 3:

    numerodigitado = int(input("escolha seu número: "))

    if(numerodigitado > numerosecreto):
        print("Número secreto é menor.")
        numerodigitado = int(input("Tente novamente, digite outro numero: "))
        if (numerodigitado > numerosecreto):
             print("Número secreto é menor.")
        tentativas+=1
    
    
    elif(numerodigitado < numerosecreto):
            print("Número secreto é maior")
            numerodigitado = int(input("Tente novamente, digite outro numero: "))
            if (numerodigitado < numerosecreto):
             print("Número secreto é menor.")
            tentativas+=1
            

    elif (numerodigitado == numerosecreto):
        print("Você acerto o Número")
        break

  



   





    

    