
from graphics import *


def main():
    menu = GraphWin("Gráfico de Funções - MENU", 500, 300)
    menu.setBackground(color_rgb(102, 108, 113))
    fp = Image(Point(136.5, 54.5), 'menu-polinomiais.gif')
    fp.draw(menu)
    ms = Image(Point(408, 256.5), 'menu-sair.gif')
    ms.draw(menu)
    codes = False
    while True:
        code = -1
        while True:
            s = menu.getMouse()
            xs = s.getX()
            ys = s.getY()
            if 38 < xs < 235 and 37 < ys < 72:
                code = 1
                break

            if 349 < xs < 467 and 239 < ys < 274:
                code = 0
                break
        if code == 0:
            sair = GraphWin("SAIR", 300, 100)
            sair.setBackground(color_rgb(102, 108, 113))
            msg = Image(Point(135, 28), 'sair-msg.gif')
            msg.draw(sair)
            sa = Image(Point(106, 68.5), 'menu-sair.gif')
            sa.draw(sair)
            ca = Image(Point(229, 68.5), 'sair-cancelar.gif')
            ca.draw(sair)
            while True:
                ss = sair.getMouse()
                xss = ss.getX()
                yss = ss.getY()
                if 47 < xss < 165 and 51 < yss < 86:
                    sair.close()
                    codes = True
                    break
                if 170 < xss < 288 and 51 < yss < 86:
                    sair.close()
                    break
        else:
            g = 0
            c = list()
            if code == 1:
                fpg = GraphWin("Função Polinimial", 300, 100)
                fpg.setBackground(color_rgb(102, 108, 113))
                fpgm = Image(Point(110.5, 28), 'fpg-msg.gif')
                fpgm.draw(fpg)
                fpgs = Image(Point(209, 70.5), 'bt-seguinte.gif')
                fpgs.draw(fpg)
                fpge = Entry(Point(59, 61), 5)
                fpge.draw(fpg)
                while True:
                    v1a = fpg.checkKey()
                    v1b = fpg.checkMouse()
                    if v1a == "Return" or (v1b is not None and (150 < v1b.getX() < 268 and 53 < v1b.getY() < 88)):
                        txt = fpge.getText()
                        if txt == '' or int(txt) < 0 or int(txt) > 10:
                            error = GraphWin("Erro", 200, 60)
                            error.setBackground(color_rgb(102, 108, 113))
                            error_msg = Text(Point(100, 30), '')
                            if txt == '':
                                error_msg = Text(Point(100, 30), "ERRO! O campo tem de ser preenchido!")
                                error_msg.setSize(8)
                            elif int(txt) < 0:
                                error_msg = Text(Point(100, 30), 'ERRO! O grau tem de ser maior que 0!')
                                error_msg.setSize(8)
                            elif int(txt) > 10:
                                error_msg = Text(Point(100, 30), 'Excesso!')
                                error_msg.setSize(8)
                            error_msg.draw(error)
                            error.getMouse()
                            error.close()
                        else:
                            g = int(txt)
                            break
                hfpc = 43 + 38 * g + 70
                fpc = GraphWin("Função Polinomial", 150, hfpc)
                fpc.setBackground(color_rgb(102, 108, 113))
                fpcs = Image(Point(71, hfpc - 29.5), 'bt-seguinte.gif')
                fpcs.draw(fpc)
                for i in range(0, g+1):
                    c.append(list())
                    c[i].append(Entry(Point(100, hfpc - 27 - (43+38*i)), 5))
                    c[i][0].draw(fpc)
                    c[i].append(Text(Point(55, hfpc - 27 - (43+38*i)), "a" + str(i) + " ="))
                    c[i][1].draw(fpc)
                while True:
                    v1a = fpc.checkKey()
                    v1b = fpc.checkMouse()
                    if v1a == "Return" or (v1b is not None and (12 < v1b.getX() < 130 and hfpc - 29.5 - 17.5 < v1b.getY() < hfpc - 29.5 + 17.5)):
                        vv = 0
                        for i in range(0, g+1):
                            txt = c[i][0].getText()
                            if txt == '':
                                vv += 1
                        if vv > 0:
                            error = GraphWin("Erro", 210, 60)
                            error.setBackground(color_rgb(102, 108, 113))
                            error_msg = Text(Point(105, 30), "ERRO! Os campos tem de ser preenchidos!")
                            error_msg.setSize(8)
                            error_msg.draw(error)
                            error.getMouse()
                            error.close()
                        else:
                            for i in range(0, g + 1):
                                txt = c[i][0].getText()
                                c[i].append(float(txt))
                            break
                fpg.close()
                fpc.close()
            dj = GraphWin("Definições Janela", 300, 126)
            dj.setBackground(color_rgb(102, 108, 113))
            djt = Image(Point(117.5, 35.5), 'df-msg.gif')
            djt.draw(dj)
            djs = Image(Point(212, 91.5), 'bt-seguinte.gif')
            djs.draw(dj)
            xmine = Entry(Point(102.5, 20), 5)
            xmine.draw(dj)
            xmaxe = Entry(Point(242.5, 20), 5)
            xmaxe.draw(dj)
            ymine = Entry(Point(102.5, 49), 5)
            ymine.draw(dj)
            ymaxe = Entry(Point(242.5, 49), 5)
            ymaxe.draw(dj)
            while True:
                v1a = dj.checkKey()
                v1b = dj.checkMouse()
                if v1a == "Return" or (v1b is not None and (153 < v1b.getX() < 271 and 74 < v1b.getY() < 109)):
                    vv = 0
                    if xmine.getText() == '' or xmaxe.getText() == '' or ymine.getText() == '' or ymaxe.getText() == '':
                        vv = 1
                    if vv > 0 or (vv == 0 and (float(xmine.getText()) >= float(xmaxe.getText())) or (float(ymine.getText()) >= float(ymaxe.getText()))):
                        error = GraphWin("Erro", 210, 60)
                        error.setBackground(color_rgb(102, 108, 113))
                        if vv > 0:
                            error_msg = Text(Point(105, 30), "ERRO! Os campos tem de ser preenchidos!")
                            error_msg.setSize(8)
                            error_msg.draw(error)
                        elif float(xmine.getText()) >= float(xmaxe.getText()):
                            error_msg = Text(Point(105, 30), "ERRO! min tem que ser menor que max!")
                            error_msg.setSize(8)
                            error_msg.draw(error)
                        elif float(ymine.getText()) >= float(ymaxe.getText()):
                            error_msg = Text(Point(105, 30), "ERRO! min tem que ser menor que max!")
                            error_msg.setSize(8)
                            error_msg.draw(error)
                        error.getMouse()
                        error.close()
                    else:
                        xmin = float(xmine.getText())
                        xmax = float(xmaxe.getText())
                        ymin = float(ymine.getText())
                        ymax = float(ymaxe.getText())
                        break
            dj.close()
            win = GraphWin("Gráfico Função", 500, 500)
            win.setBackground('white')
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
                if code == 1:
                    for i1 in range(g, -1, -1):
                        y += c[i1][2]*x**i1
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
                if (xdif <= 10 and ydif <= 10) or (xdif <= 10 and ydif <= 20) or (xdif <= 20 and ydif <= 10):
                    x += 0.01
                else:
                    x += (0.01*xdif*ydif)/100
                p1 = p2
            win.getMouse()
            win.close()
        if codes:
            break
    menu.close()


main()
