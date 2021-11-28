
from graphics import *


def main(c1):
    win = GraphWin("Gráfico Função", 500, 500)
    win.setBackground('white')
    xmin = -6
    xmax = 6
    xmed = (xmin+xmax)/2
    xdif = xmax - xmin
    x0pos = -1
    x = xmin
    if xmin < 0 < xmax and not xmed == 0:
        x0pos = -xmin * (250/(xdif/2))
        ox = Line(Point(x0pos, 0), Point(x0pos, 500))
        ox.setOutline('black')
        ox.draw(win)
    elif xmed == 0:
        x0pos = 250
        ox = Line(Point(x0pos, 0), Point(x0pos, 500))
        ox.setOutline('black')
        ox.draw(win)
    ymin = -6
    ymax = 6
    ymed = (ymin + ymax) / 2
    ydif = ymax - ymin
    y0pos = -1
    if ymin < 0 < ymax and not ymed == 0:
        y0pos = 500 - (-ymin * (250 / (ydif / 2)))
        oy = Line(Point(0, y0pos), Point(500, y0pos))
        oy.setOutline('black')
        oy.draw(win)
    elif ymed == 0:
        y0pos = 250
        oy = Line(Point(0, y0pos), Point(500, y0pos))
        oy.setOutline('black')
        oy.draw(win)
    p1 = p2 = Point(0, 0)
    xpos = ypos = 0
    while True:
        y = 0
        for i1 in range(g, -1, -1):
            y += c1[i1]*x**i1
        if x > xmax:
            break
        if xmin < 0 < xmax:
            if x < 0:            #
                # xpos = x0pos - ((x0pos*(0-x)) / (xdif/2))
                xpos = x0pos - ((x0pos*(0-x)) / (0 - xmin))
                if ymin < 0 < ymax:
                    if y < 0:
                        ypos = y0pos + ((y0pos * (0 - y)) / ymax)
                    else:
                        ypos = y0pos - ((y0pos * y) / ymax)
                else:
                    ypos = 500-((y - ymin) * (500 / ydif))
                p2 = Point(xpos, ypos)
                if x == xmin:
                    p1 = Point(xpos, ypos)
            elif x >= 0:         #
                # xpos = x0pos + ((x0pos * x) / (xdif / 2))
                xpos = x0pos + ((x0pos * x) / (0 - xmin))
                if ymin < 0 < ymax:
                    if y < 0:
                        ypos = y0pos + ((y0pos * (0 - y)) / ymax)
                    else:
                        ypos = y0pos - ((y0pos * y) / ymax)
                else:
                    ypos = 500-((y - ymin) * (500 / ydif))
                p2 = Point(xpos, ypos)
                if x == xmin:
                    p1 = Point(xpos, ypos)
        else:
            if x < 0:            #
                # xpos = x0pos - ((x0pos*(0-x)) / (xdif/2))
                xpos = (x - xmin) * (500 / xdif)
                if ymin < 0 < ymax:
                    if y < 0:
                        ypos = y0pos + ((y0pos * (0 - y)) / ymax)
                    else:
                        ypos = y0pos - ((y0pos * y) / ymax)
                else:
                    ypos = 500-((y - ymin) * (500 / ydif))
                p2 = Point(xpos, ypos)
                if x == xmin:
                    p1 = Point(xpos, ypos)
            elif x >= 0:         #
                # xpos = x0pos + ((x0pos * x) / (xdif / 2))
                xpos = (x - xmin) * (500 / xdif)
                if ymin < 0 < ymax:
                    if y < 0:
                        ypos = y0pos + ((y0pos * (0 - y)) / ymax)
                    else:
                        ypos = y0pos - ((y0pos * y) / ymax)
                else:
                    ypos = 500-((y - ymin) * (500 / ydif))
                p2 = Point(xpos, ypos)
                if x == xmin:
                    p1 = Point(xpos, ypos)
        ln = Line(p1, p2)  #
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
        print('\033[31mERRO!!! O grau tem de ser maior que 0!\033[m')
        g = int(input('Digite novamente: '))
c = list()
for i in range(g, -1, -1):
    print('Digite o coeficiente do termo de grau {}'.format(i), end='')
    c.append(float(input(': ')))
c.reverse()

main(c)
