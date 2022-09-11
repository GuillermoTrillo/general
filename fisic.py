import math
print("Escreva o tempo desejado! você tem 8 oportunidades!")

Xcon = -2
Ycon = 5
for i in range(8):  
    entrada = input()
    t = float(entrada)
    xT = 5 * (t ** 2) + 3 * (t**3) - 2
    yT = 2 * (t ** 3) + 5
    xdel = xT - Xcon
    ydel = yT - Ycon
    D = math.sqrt(xdel ** 2 + ydel ** 2)
    Vm = D / t
    print("\n Δt  |   D    |  Vm ")
    print(t, " | ", round(D, 2), " | ", round(Vm, 2), "\n")