def calcula_minimo(x, y):
    interacoes = 1
    a = 6*x + 3 * y + 3
    b = 3*x + 4*y +1
    vetor = (a**2 + b**2)**0.5
    x_novo = x - 0.1 * a
    y_novo = y - 0.1 * b
    x = x_novo
    y = y_novo

    while vetor > 10**-5:
        a = 6*x + 3 * y + 3
        b = 3*x + 4*y +1
        vetor = (a**2 + b**2)**0.5
        x_novo = x + 0.1 * (-a)
        y_novo = y + 0.1 * (-b)
        x = x_novo
        y = y_novo
        interacoes += 1
    return (f"O x final vale {x}, o y final vale {y} e o número de interações totais foi {interacoes}.")

print(calcula_minimo(0, 0))