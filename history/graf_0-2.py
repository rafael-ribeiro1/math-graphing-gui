
from graphics import *


def main(c1):
    win = GraphWin("Gráfico Função", 500, 500)
    win.setBackground('white')
    img = Image(Point(250, 250), "graf.gif")
    img.draw(win)
    x = -6
    while True:
        y = 0
        for i1 in range(g, -1, -1):
            y += c1[i1]*x**i1
        if x > 6:
            break
        if x < 0:
            xpos = 250 - (250*(0-x)) / 6
            if y < 0:
                ypos = 250 + (250 * (0 - y)) / 6
            else:
                ypos = 250 - (250 * y) / 6
            p2 = Point(xpos, ypos)
            if x == -6:
                p1 = Point(xpos, ypos)
        elif x >= 0:
            xpos = 250 + (250 * x) / 6
            if y < 0:
                ypos = 250 + (250 * (0 - y)) / 6
            else:
                ypos = 250 - (250 * y) / 6
            p2 = Point(xpos, ypos)
        ln = Line(p1, p2)
        ln.setOutline('blue')
        ln.setWidth(3)
        ln.draw(win)
        x += 0.01
        p1 = p2
    win.getMouse()
    win.close()


print('=-'*20+'=')
print("{:^41}".format("GRÁFICOS DE FUNÇÕES"))
print('=-'*20+'=')
g = int(input('Digite o grau do polinómio: '))
if g < 0:
    while g < 0:
        print('\033[31mERRO!!! O grau tem de ser maior que 0!')
        g = int(input('Digite novamente: '))
c = list()
for i in range(g, -1, -1):
    print('Digite o coeficiente do termo de grau {}'.format(i), end='')
    c.append(float(input(': ')))
c.reverse()

main(c)
