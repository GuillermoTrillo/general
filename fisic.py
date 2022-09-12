import math
print("Escreva o tempo desejado! você tem 8 oportunidades!")
#Xcon e Ycon são constantes; o valor de quando t = 0. Eles são o instante inicial. 
Xcon = -2
Ycon = 5
#O for que repite os cálculos e os imprime na tela. Poderia ter feito que se imprimissem todos em uma lista para que ficase mais lindo, 
#mas assim é mais simples, e não é necessário confundir mais as coisas.
for i in range(8):  
    entrada = input()
    t = float(entrada)
    #xT e yT são os cálculos para saber o X e o Y no instante t escolhido.
    xT = 5 * (t ** 2) + 3 * (t**3) - 2
    yT = 2 * (t ** 3) + 5
    #xdel e ydel são a variação de cada coordenada em um periodo de tempo entre o t final escolhido e o t inicial escolhido.
    xdel = xT - Xcon
    ydel = yT - Ycon
    #D é a distancia entre as coordenadas do instante t final escolhido e do instante t inicial escolhido.
    D = math.sqrt(xdel ** 2 + ydel ** 2)
    #Vm é a velocidade média entre um ponto e outro.
    Vm = D / t
    # Aqui ele escreve no terminal os respectivos valores do instante temporal escolhido, a distância calculada por D e a velocidade média 
    # calculada por Vm.
    print("\n Δt  |   D    |  Vm ")
    print(t, " | ", round(D, 2), " | ", round(Vm, 2), "\n")
