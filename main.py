def calcula_minimo(x, y, alpha):
    iteracoes = 1
    a = 6*x + 3 * y + 3
    b = 3*x + 4*y +1
    vetor = (a**2 + b**2)**0.5
    x_novo = x - alpha * a
    y_novo = y - alpha * b
    x = x_novo
    y = y_novo

    while vetor > 10**-5:
        a = 6*x + 3 * y + 3
        b = 3*x + 4*y +1
        vetor = (a**2 + b**2)**0.5
        x_novo = x + alpha * (-a)
        y_novo = y + alpha * (-b)
        x = x_novo
        y = y_novo
        iteracoes += 1
    return (f"O x final vale {x}, o y final vale {y} e número de interações totais foi {iteracoes}, dado um alpha = {alpha}.")

print(calcula_minimo(0, 0, 0.1))
print(calcula_minimo(0, 0, 0.15))
print(calcula_minimo(0, 0, 0.2))
print(calcula_minimo(0, 0, 0.3))
print(calcula_minimo(0, 0, 0.5))