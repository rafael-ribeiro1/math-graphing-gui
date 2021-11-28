
from graphics import *


def main():
    win = GraphWin("Gráfico Função", 500, 500)
    win.setBackground('white')
    img = Image(Point(250, 250), "graf.gif")
    img.draw(win)
    x = -6
    while True:
        y = x
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


main()
