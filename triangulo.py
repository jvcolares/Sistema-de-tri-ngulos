import math

x1 = float(input("Digite a coordenada x1 do ponto A: "))
y1 = float(input("Digite a coordenada y1 do ponto A: "))
x2 = float(input("Digite a coordenada x2 do ponto B: "))
y2 = float(input("Digite a coordenada y2 do ponto B: "))
x3 = float(input("Digite a coordenada x3 do ponto C: "))
y3 = float(input("Digite a coordenada y3 do ponto C: "))

distancia_a=math.sqrt((x1-x2)**2+(y1-y2)**2)
distancia_b=math.sqrt((x2-x3)**2+(y2-y3)**2)
distancia_c=math.sqrt((x3-x1)**2+(y3-y1)**2)

if distancia_a<distancia_b + distancia_c and distancia_b<distancia_a + distancia_c and distancia_c<distancia_a + distancia_b:
    print("Os pontos A, B e C formam um triângulo")

    if distancia_a==distancia_b and distancia_b==distancia_c and distancia_a==distancia_c:
        print("O triângulo é equilátero")
    elif distancia_a==distancia_b or distancia_b==distancia_c or distancia_a==distancia_c:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Os pontos A, B e C não formam um triângulo")
