
from graphics import *
from math import sin, cos, tan, pi, isclose, radians


def sup(val):
    val = str(val)
    res = ''
    if len(val) == 1:
        if val == 1:
            res = chr(0x00b9)
        elif 2 <= int(val) <= 3:
            res = chr(0x00b0 + int(val))
        else:
            res = chr(0x2070 + int(val))
        return res
    else:
        n = list()
        for c2 in range(0, len(val)):
            n.append(val[c2])
        for cont in range(0, len(val)):
            if val == 1:
                res = chr(0x00b9)
            elif 2 <= int(val) <= 3:
                a = n[cont]
                res = chr(0x00b0 + int(a))
            else:
                res = chr(0x2070 + int(val[cont]))
        return res


def fmsg(grau):
    msg = ''
    for c in range(grau, -1, -1):
        if c != 0:
            msg = msg + ('a' + str(c) + 'x' + sup(c) + ' ')
        else:
            msg = msg + ('a' + str(c))
        if c != 0:
            msg = msg + '+ '
    return msg


def wfc(grau):
    if grau <= 2:
        w = 150
    else:
        w = 150 + (grau - 2)*30 + grau*15
    return w


def main():
    menu = GraphWin("Gráfico de Funções - MENU", 500, 300)
    menu.setBackground(color_rgb(102, 108, 113))
    fp = Image(Point(136.5, 54.5), 'menu-polinomiais.gif')
    fp.draw(menu)
    ff = Image(Point(364.5, 54.5), 'menu-fracionarias.gif')
    ff.draw(menu)
    fr = Image(Point(136.5, 125.5), 'menu-raiz.gif')
    fr.draw(menu)
    fm = Image(Point(364.5, 125.5), 'menu-modulo.gif')
    fm.draw(menu)
    ft = Image(Point(136.5, 196.5), 'menu-trigonometricas.gif')
    ft.draw(menu)
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
            if 266 < xs < 463 and 37 < ys < 72:
                code = 2
                break
            if 38 < xs < 235 and 108 < ys < 143:
                code = 3
                break
            if 266 < xs < 463 and 108 < ys < 143:
                code = 4
                break
            if 38 < xs < 235 and 179 < ys < 214:
                code = 5
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
            g = 0               # code == 1
            c = list()
            gn = 0              # code == 2
            cn = list()
            gd = 0
            cd = list()
            ir = 0              # code == 3
            gr = 0
            cr = list()
            gm = 0              # code == 4
            cm = list()
            tt = 0              # code == 5
            gt = 0
            ct = list()
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
                wfpc = wfc(g)
                fpc = GraphWin("Função Polinomial", wfpc, hfpc)
                fpc.setBackground(color_rgb(102, 108, 113))
                fpmsg = fmsg(g)
                fpmc = Text(Point(wfpc/2, 35/2), fpmsg)
                fpmc.setFace('courier')
                fpmc.setSize(8)
                fpmc.draw(fpc)
                fpcs = Image(Point(71, hfpc - 29.5), 'bt-seguinte.gif')
                fpcs.draw(fpc)
                for i in range(0, g+1):
                    c.append(list())
                    c[i].append(Entry(Point(100, hfpc - 27 - (43+38*i)), 5))
                    c[i][0].draw(fpc)
                    c[i].append(Text(Point(50, hfpc - 27 - (43+38*i)), "a" + str(i) + " ="))
                    c[i][1].setFace('courier')
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
            elif code == 2:
                ffgn = GraphWin("Função Fracionária", 300, 100)
                ffgn.setBackground(color_rgb(102, 108, 113))
                ffgnm = Image(Point(149.5, 28.5), 'ffgn-msg.gif')
                ffgnm.draw(ffgn)
                ffgns = Image(Point(209, 70.5), 'bt-seguinte.gif')
                ffgns.draw(ffgn)
                ffgne = Entry(Point(59, 61), 5)
                ffgne.draw(ffgn)
                while True:
                    v1a = ffgn.checkKey()
                    v1b = ffgn.checkMouse()
                    if v1a == "Return" or (v1b is not None and (150 < v1b.getX() < 268 and 53 < v1b.getY() < 88)):
                        txt = ffgne.getText()
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
                            gn = int(txt)
                            break
                hffcn = 43 + 38 * gn + 70
                wffcn = wfc(gn)
                ffcn = GraphWin("Função Fracionária", wffcn, hffcn)
                ffcn.setBackground(color_rgb(102, 108, 113))
                ffnmsg = fmsg(gn)
                ffnmc = Text(Point(wffcn / 2, 35 / 2), ffnmsg)
                ffnmc.setFace('courier')
                ffnmc.setSize(8)
                ffnmc.draw(ffcn)
                ffcns = Image(Point(71, hffcn - 29.5), 'bt-seguinte.gif')
                ffcns.draw(ffcn)
                for i in range(0, gn + 1):
                    cn.append(list())
                    cn[i].append(Entry(Point(100, hffcn - 27 - (43 + 38 * i)), 5))
                    cn[i][0].draw(ffcn)
                    cn[i].append(Text(Point(50, hffcn - 27 - (43 + 38 * i)), "a" + str(i) + " ="))
                    cn[i][1].setFace('courier')
                    cn[i][1].draw(ffcn)
                while True:
                    v1a = ffcn.checkKey()
                    v1b = ffcn.checkMouse()
                    if v1a == "Return" or (v1b is not None and (
                            12 < v1b.getX() < 130 and hffcn - 29.5 - 17.5 < v1b.getY() < hffcn - 29.5 + 17.5)):
                        vv = 0
                        for i in range(0, gn + 1):
                            txt = cn[i][0].getText()
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
                            for i in range(0, gn + 1):
                                txt = cn[i][0].getText()
                                cn[i].append(float(txt))
                            break
                ffgn.close()
                ffcn.close()
                ffgd = GraphWin("Função Fracionária", 300, 100)
                ffgd.setBackground(color_rgb(102, 108, 113))
                ffgdm = Image(Point(150, 28.5), 'ffgd-msg.gif')
                ffgdm.draw(ffgd)
                ffgds = Image(Point(209, 70.5), 'bt-seguinte.gif')
                ffgds.draw(ffgd)
                ffgde = Entry(Point(59, 61), 5)
                ffgde.draw(ffgd)
                while True:
                    v1a = ffgd.checkKey()
                    v1b = ffgd.checkMouse()
                    if v1a == "Return" or (v1b is not None and (150 < v1b.getX() < 268 and 53 < v1b.getY() < 88)):
                        txt = ffgde.getText()
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
                            gd = int(txt)
                            break
                hffcd = 43 + 38 * gd + 70
                wffcd = wfc(gd)
                ffcd = GraphWin("Função Fracionária", wffcd, hffcd)
                ffcd.setBackground(color_rgb(102, 108, 113))
                ffdmsg = fmsg(gd)
                ffdmc = Text(Point(wffcd / 2, 35 / 2), ffdmsg)
                ffdmc.setFace('courier')
                ffdmc.setSize(8)
                ffdmc.draw(ffcd)
                ffcds = Image(Point(71, hffcd - 29.5), 'bt-seguinte.gif')
                ffcds.draw(ffcd)
                for i in range(0, gd + 1):
                    cd.append(list())
                    cd[i].append(Entry(Point(100, hffcd - 27 - (43 + 38 * i)), 5))
                    cd[i][0].draw(ffcd)
                    cd[i].append(Text(Point(50, hffcd - 27 - (43 + 38 * i)), "a" + str(i) + " ="))
                    cd[i][1].setFace('courier')
                    cd[i][1].draw(ffcd)
                while True:
                    v1a = ffcd.checkKey()
                    v1b = ffcd.checkMouse()
                    if v1a == "Return" or (v1b is not None and (
                            12 < v1b.getX() < 130 and hffcd - 29.5 - 17.5 < v1b.getY() < hffcd - 29.5 + 17.5)):
                        vv = v0 = 0
                        for i in range(0, gd + 1):
                            txt = cd[i][0].getText()
                            if txt == '':
                                vv += 1
                            if gd == 0 and float(txt) == 0:
                                v0 = 1
                        if vv > 0 or v0 == 1:
                            error = GraphWin("Erro", 210, 60)
                            error.setBackground(color_rgb(102, 108, 113))
                            if vv > 0:
                                error_msg = Text(Point(105, 30), "ERRO! Os campos tem de ser preenchidos!")
                                error_msg.setSize(8)
                                error_msg.draw(error)
                            elif v0 == 1:
                                error_msg = Text(Point(105, 30), "ERRO! O denominador não pode ser 0!")
                                error_msg.setSize(8)
                                error_msg.draw(error)
                            error.getMouse()
                            error.close()
                        else:
                            for i in range(0, gd + 1):
                                txt = cd[i][0].getText()
                                cd[i].append(float(txt))
                            break
                ffgd.close()
                ffcd.close()
            elif code == 3:
                fri = GraphWin("Função Raíz", 300, 100)
                fri.setBackground(color_rgb(102, 108, 113))
                frim = Image(Point(110.5, 28), 'fri-msg.gif')
                frim.draw(fri)
                fris = Image(Point(209, 70.5), 'bt-seguinte.gif')
                fris.draw(fri)
                frie = Entry(Point(59, 61), 5)
                frie.draw(fri)
                while True:
                    v1a = fri.checkKey()
                    v1b = fri.checkMouse()
                    if v1a == "Return" or (v1b is not None and (150 < v1b.getX() < 268 and 53 < v1b.getY() < 88)):
                        txt = frie.getText()
                        if txt == '' or int(txt) < 0:
                            error = GraphWin("Erro", 200, 60)
                            error.setBackground(color_rgb(102, 108, 113))
                            error_msg = Text(Point(100, 30), '')
                            if txt == '':
                                error_msg = Text(Point(100, 30), "ERRO! O campo tem de ser preenchido!")
                                error_msg.setSize(8)
                            elif int(txt) < 0:
                                error_msg = Text(Point(100, 30), 'ERRO! O grau tem de ser maior que 0!')
                                error_msg.setSize(8)
                            error_msg.draw(error)
                            error.getMouse()
                            error.close()
                        else:
                            ir = int(txt)
                            break
                fri.close()
                frg = GraphWin("Função Raíz", 300, 100)
                frg.setBackground(color_rgb(102, 108, 113))
                frgm = Image(Point(110.5, 28), 'fpg-msg.gif')
                frgm.draw(frg)
                frgs = Image(Point(209, 70.5), 'bt-seguinte.gif')
                frgs.draw(frg)
                frge = Entry(Point(59, 61), 5)
                frge.draw(frg)
                while True:
                    v1a = frg.checkKey()
                    v1b = frg.checkMouse()
                    if v1a == "Return" or (v1b is not None and (150 < v1b.getX() < 268 and 53 < v1b.getY() < 88)):
                        txt = frge.getText()
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
                            gr = int(txt)
                            break
                hfrc = 43 + 38 * gr + 70
                wfrc = wfc(gr)
                frc = GraphWin("Função Raíz", wfrc, hfrc)
                frc.setBackground(color_rgb(102, 108, 113))
                frmsg = fmsg(gr)
                frmc = Text(Point(wfrc / 2, 35 / 2), frmsg)
                frmc.setFace('courier')
                frmc.setSize(8)
                frmc.draw(frc)
                frcs = Image(Point(71, hfrc - 29.5), 'bt-seguinte.gif')
                frcs.draw(frc)
                for i in range(0, gr + 1):
                    cr.append(list())
                    cr[i].append(Entry(Point(100, hfrc - 27 - (43 + 38 * i)), 5))
                    cr[i][0].draw(frc)
                    cr[i].append(Text(Point(50, hfrc - 27 - (43 + 38 * i)), "a" + str(i) + " ="))
                    cr[i][1].setFace('courier')
                    cr[i][1].draw(frc)
                while True:
                    v1a = frc.checkKey()
                    v1b = frc.checkMouse()
                    if v1a == "Return" or (v1b is not None and (
                            12 < v1b.getX() < 130 and hfrc - 29.5 - 17.5 < v1b.getY() < hfrc - 29.5 + 17.5)):
                        vv = 0
                        for i in range(0, gr + 1):
                            txt = cr[i][0].getText()
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
                            for i in range(0, gr + 1):
                                txt = cr[i][0].getText()
                                cr[i].append(float(txt))
                            break
                frg.close()
                frc.close()
            elif code == 4:
                fmg = GraphWin("Função Módulo", 300, 100)
                fmg.setBackground(color_rgb(102, 108, 113))
                fmgm = Image(Point(110.5, 28), 'fpg-msg.gif')
                fmgm.draw(fmg)
                fmgs = Image(Point(209, 70.5), 'bt-seguinte.gif')
                fmgs.draw(fmg)
                fmge = Entry(Point(59, 61), 5)
                fmge.draw(fmg)
                while True:
                    v1a = fmg.checkKey()
                    v1b = fmg.checkMouse()
                    if v1a == "Return" or (v1b is not None and (150 < v1b.getX() < 268 and 53 < v1b.getY() < 88)):
                        txt = fmge.getText()
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
                            gm = int(txt)
                            break
                hfmc = 43 + 38 * gm + 70
                wfmc = wfc(gm)
                fmc = GraphWin("Função Módulo", wfmc, hfmc)
                fmc.setBackground(color_rgb(102, 108, 113))
                fmmsg = fmsg(gm)
                fmmc = Text(Point(wfmc / 2, 35 / 2), fmmsg)
                fmmc.setFace('courier')
                fmmc.setSize(8)
                fmmc.draw(fmc)
                fmcs = Image(Point(71, hfmc - 29.5), 'bt-seguinte.gif')
                fmcs.draw(fmc)
                for i in range(0, gm + 1):
                    cm.append(list())
                    cm[i].append(Entry(Point(100, hfmc - 27 - (43 + 38 * i)), 5))
                    cm[i][0].draw(fmc)
                    cm[i].append(Text(Point(50, hfmc - 27 - (43 + 38 * i)), "a" + str(i) + " ="))
                    cm[i][1].setFace('courier')
                    cm[i][1].draw(fmc)
                while True:
                    v1a = fmc.checkKey()
                    v1b = fmc.checkMouse()
                    if v1a == "Return" or (v1b is not None and (
                            12 < v1b.getX() < 130 and hfmc - 29.5 - 17.5 < v1b.getY() < hfmc - 29.5 + 17.5)):
                        vv = 0
                        for i in range(0, gm + 1):
                            txt = cm[i][0].getText()
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
                            for i in range(0, gm + 1):
                                txt = cm[i][0].getText()
                                cm[i].append(float(txt))
                            break
                fmg.close()
                fmc.close()
            elif code == 5:
                ftt = GraphWin("Função Trigonométrica", 200, 200)
                ftt.setBackground(color_rgb(102, 108, 113))
                fttm = Image(Point(99, 25), 'ft-msg.gif')
                fttm.draw(ftt)
                ftts = Image(Point(97, 69.5), 'ft-sin.gif')
                ftts.draw(ftt)
                fttc = Image(Point(97, 115.5), 'ft-cos.gif')
                fttc.draw(ftt)
                fttt = Image(Point(97, 161.5), 'ft-tg.gif')
                fttt.draw(ftt)
                while True:
                    st = ftt.checkMouse()
                    stx = sty = 0
                    if st is not None:
                        stx = st.getX()
                        sty = st.getY()
                    if st is not None and (38 < stx < 156 and 52 < sty < 87):
                        tt = 1
                        break
                    if st is not None and (38 < stx < 156 and 98 < sty < 133):
                        tt = 2
                        break
                    if st is not None and (38 < stx < 156 and 144 < sty < 179):
                        tt = 3
                        break
                ftt.close()
                ftg = GraphWin("Função Trigonométrica", 300, 100)
                ftg.setBackground(color_rgb(102, 108, 113))
                ftgm = Image(Point(110.5, 28), 'fpg-msg.gif')
                ftgm.draw(ftg)
                ftgs = Image(Point(209, 70.5), 'bt-seguinte.gif')
                ftgs.draw(ftg)
                ftge = Entry(Point(59, 61), 5)
                ftge.draw(ftg)
                while True:
                    v1a = ftg.checkKey()
                    v1b = ftg.checkMouse()
                    if v1a == "Return" or (v1b is not None and (150 < v1b.getX() < 268 and 53 < v1b.getY() < 88)):
                        txt = ftge.getText()
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
                            gt = int(txt)
                            break
                hftc = 43 + 38 * gt + 70
                wftc = wfc(gt)
                ftc = GraphWin("Função Polinomial", wftc, hftc)
                ftc.setBackground(color_rgb(102, 108, 113))
                ftmsg = fmsg(gt)
                ftmc = Text(Point(wftc / 2, 35 / 2), ftmsg)
                ftmc.setFace('courier')
                ftmc.setSize(8)
                ftmc.draw(ftc)
                ftcs = Image(Point(71, hftc - 29.5), 'bt-seguinte.gif')
                ftcs.draw(ftc)
                for i in range(0, gt + 1):
                    ct.append(list())
                    ct[i].append(Entry(Point(100, hftc - 27 - (43 + 38 * i)), 5))
                    ct[i][0].draw(ftc)
                    ct[i].append(Text(Point(50, hftc - 27 - (43 + 38 * i)), "a" + str(i) + " ="))
                    ct[i][1].setFace('courier')
                    ct[i][1].draw(ftc)
                while True:
                    v1a = ftc.checkKey()
                    v1b = ftc.checkMouse()
                    if v1a == "Return" or (v1b is not None and (
                            12 < v1b.getX() < 130 and hftc - 29.5 - 17.5 < v1b.getY() < hftc - 29.5 + 17.5)):
                        vv = 0
                        for i in range(0, gt + 1):
                            txt = ct[i][0].getText()
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
                            for i in range(0, gt + 1):
                                txt = ct[i][0].getText()
                                ct[i].append(float(txt))
                            break
                ftg.close()
                ftc.close()
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
            x0pos = -5
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
            y0pos = -5
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
            if xmin < 0 < xmax:
                if xdif < 40:
                    xex = xey = -5
                    xe = Text(Point(0, 0), '')
                    if y0pos > 250:
                        if x0pos >= 250:
                            xex = x0pos + ((x0pos * 1) / (0 - xmin))
                            xey = y0pos - 12
                            xe = Text(Point(xex, xey), '1')
                        elif x0pos < 250:
                            xex = x0pos - ((x0pos * 1) / (0 - xmin))
                            xey = y0pos + 12
                            xe = Text(Point(xex, xey), '-1')
                    elif y0pos <= 250:
                        if x0pos >= 250:
                            xex = x0pos + ((x0pos * 1) / (0 - xmin))
                            xey = y0pos - 12
                            xe = Text(Point(xex, xey), '1')
                        elif x0pos < 250:
                            xex = x0pos - ((x0pos * 1) / (0 - xmin))
                            xey = y0pos - 12
                            xe = Text(Point(xex, xey), '-1')
                    xe.setSize(8)
                    xe.draw(win)
            if ymin < 0 < ymax:
                if ydif < 40:
                    yex = yey = -5
                    ye = Text(Point(0, 0), '')
                    if x0pos > 250:
                        if y0pos > 250:
                            yex = x0pos - 12
                            yey = y0pos + ((y0pos * 1) / ymax)
                            ye = Text(Point(yex, yey), '-1')
                        elif y0pos <= 250:
                            yex = x0pos + 12
                            yey = y0pos - ((y0pos * 1) / ymax)
                            ye = Text(Point(yex, yey), '1')
                    elif x0pos <= 250:
                        if y0pos > 250:
                            yex = x0pos - 12
                            yey = y0pos + ((y0pos * 1) / ymax)
                            ye = Text(Point(yex, yey), '-1')
                        elif y0pos <= 250:
                            yex = x0pos + 12
                            yey = y0pos - ((y0pos * 1) / ymax)
                            ye = Text(Point(yex, yey), '1')
                    ye.setSize(8)
                    ye.draw(win)
            if xdif < 40:
                x = xmin
                contador = 1
                escx = list()
                while True:
                    xpos = 0
                    if x > xmax:
                        break
                    if xmin < 0:
                        ini = (0-xmin)//1
                        if contador == 1:
                            x = 0-ini
                    else:
                        ini = xmin//1
                        if contador == 1:
                            x = ini
                    if xmin < 0 < xmax:
                        if x < 0:            #
                            xpos = x0pos - ((x0pos*(0-x)) / (0 - xmin))
                        elif x > 0:         #
                            xpos = x0pos + ((x0pos * x) / (0 - xmin))
                    else:
                        if x < 0:            #
                            xpos = (x - xmin) * (500 / xdif)
                        elif x > 0:         #
                            xpos = (x - xmin) * (500 / xdif)
                    esc1 = Point(xpos, y0pos - 3)
                    esc2 = Point(xpos, y0pos + 3)
                    escx.append(Line(esc1, esc2))
                    escx[contador-1].setOutline('black')
                    escx[contador-1].draw(win)
                    if contador + 1 == 0:
                        contador += 2
                    else:
                        contador += 1
                    x += 1
            if ydif < 40:
                y = ymin
                contador1 = 1
                escy = list()
                while True:
                    ypos = 0
                    if y > ymax:
                        break
                    if ymin < 0:
                        ini = (0-ymin)//1
                        if contador1 == 1:
                            y = 0-ini
                    else:
                        ini = ymin//1
                        if contador1 == 1:
                            y = ini
                    if ymin < 0 < ymax:
                        if y < 0:
                            ypos = y0pos + ((y0pos * (0 - y)) / ymax)
                        if y > 0:
                            ypos = y0pos - ((y0pos * y) / ymax)
                    else:
                        ypos = 500 - ((y - ymin) * (500 / ydif))
                    escy1 = Point(x0pos+3, ypos)
                    escy2 = Point(x0pos-3, ypos)
                    escy.append(Line(escy1, escy2))
                    escy[contador1-1].setOutline('black')
                    escy[contador1-1].draw(win)
                    if contador1 + 1 == 0:
                        contador1 += 2
                    else:
                        contador1 += 1
                    y += 1
            x = xmin
            p1 = p2 = Point(0, 0)
            xpos = ypos = 0
            y = 0
            ress = rest = 0
            etan = True
            aetan = False
            naetan = 0
            while True:
                ys = xs = xt = 0
                y = 0
                n = d = 0
                exe = True

                if code == 1:               # code == 1
                    for i1 in range(g, -1, -1):
                        y += c[i1][2]*x**i1
                elif code == 2:             # code == 2
                    for i1 in range(gn, -1, -1):
                        n += cn[i1][2]*x**i1
                    for i2 in range(gd, -1, -1):
                        d += cd[i2][2]*x**i2
                    y = n / d
                elif code == 3:             # code == 3
                    res = 0
                    for i1 in range(gr, -1, -1):
                        res += cr[i1][2]*x**i1
                    if ir % 2 == 0:
                        if res >= 0:
                            y = (res ** (1.0 / float(ir))).real
                        else:
                            y = 0
                            exe = False
                    else:
                        if res >= 0:
                            y = (res ** (1.0 / float(ir)))
                        else:
                            y = -abs(res ** (1.0 / float(ir)))
                elif code == 4:             # code == 4
                    res = 0
                    for i1 in range(gm, -1, -1):
                        res += cm[i1][2] * x ** i1
                    y = abs(res)
                elif code == 5:             # code == 5
                    res = 0
                    for i1 in range(gt, -1, -1):
                        res += ct[i1][2] * x ** i1
                    if tt == 1:
                        y = sin(res)
                    elif tt == 2:
                        y = cos(res)
                    elif tt == 3:
                        if etan:
                            if (xdif <= 10 and ydif <= 10) or (xdif <= 10 and ydif <= 20) or (xdif <= 20 and ydif <= 10):
                                xs = x + 0.01
                            else:
                                xs = x + (0.01 * xdif * ydif) / 100
                            ress = rest = 0
                            for i1 in range(gt, -1, -1):
                                ress += ct[i1][2] * xs ** i1
                            if abs(tan(res) - tan(ress)) > ydif/2:
                                xt = x
                                while True:
                                    for i1 in range(gt, -1, -1):
                                        rest += ct[i1][2] * xt ** i1
                                    if (tan(res) >= 0 and (tan(rest) * tan(ress) > 0)) or (tan(res) <= 0 and (tan(rest) * tan(ress) > 0)):
                                        xt -= 0.0001
                                        etan = False
                                        break
                                    xt += 0.0001
                                x = xt
                                y = tan(rest)
                                exe = False
                            else:
                                y = tan(res)
                                etan = True
                        else:
                            y = tan(ress)
                            exe = False
                            etan = True
                        # ###
                        #if (tan(res) - ya) < ydif/2:
                        #    y = tan(res)
                        #    if isclose(tan(res), 0.0):
                        #        while isclose(tan(res), 0.0) is True:
                        #            if (xdif <= 10 and ydif <= 10) or (xdif <= 10 and ydif <= 20) or (
                        #                    xdif <= 20 and ydif <= 10):
                        #                x += 0.01
                        #            else:
                        #                x += (0.01 * xdif * ydif) / 100
                        #            res = 0
                        #            for i1 in range(gt, -1, -1):
                        #                res += ct[i1][2] * x ** i1
                        #else:
                        #    y = tan(ress)
                        #    exe = False
                        # ###
                        #if etan:
                        #    if (tan(res) < ymin) or (tan(res) > ymax):
                        #        y = 0
                        #        exe = False
                        #        etan = False
                        #    else:
                        #       y = tan(res)
                        #else:
                        #    if (tan(res) > ymin) and (tan(res) < ymax):
                        #        etan = True
                        #    else:
                        #        y = tan(ress)
                        #        exe = False
                if x > xmax:
                    break
                if xmin < 0 < xmax:
                    if x < 0:            #
                        # xpos = x0pos - ((x0pos*(0-x)) / (xdif/2))
                        xpos = x0pos - ((x0pos*(0-x)) / (0 - xmin))
                        if ymin < 0 < ymax:
                            if y.real < 0:
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
                            if y.real < 0:
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
                            if y.real < 0:
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
                            if y.real < 0:
                                ypos = y0pos + ((y0pos * (0 - y)) / ymax)
                            else:
                                ypos = y0pos - ((y0pos * y) / ymax)
                        else:
                            ypos = 500-((y - ymin) * (500 / ydif))
                        p2 = Point(xpos, ypos)
                        if x == xmin:
                            p1 = Point(xpos, ypos)
                if exe is True:
                    ln = Line(p1, p2)  #
                    ln.setOutline('blue')
                    ln.setWidth(3)
                    ln.draw(win)
                if etan:
                    if (xdif <= 10 and ydif <= 10) or (xdif <= 10 and ydif <= 20) or (xdif <= 20 and ydif <= 10):
                        x += 0.01
                    else:
                        x += (0.01*xdif*ydif)/100
                else:
                    x += 0.0001
                p1 = p2
            wins = Text(Point(80, 5), "Clicar na tela para voltar ao menu")
            wins.setSize(8)
            wins.draw(win)
            win.getMouse()
            win.close()
        if codes:
            break
    menu.close()


main()
