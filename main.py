# streamlit hello --server.enableCORS false --server.enableXsrfProtection false

# Importan las librerias necesarias
import base64
import numpy as np
import sympy as sp
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import interpolate as numint
from st_cytoscape import cytoscape
from PIL import Image

# Configuracion de la pagina
st.set_page_config(page_title = "Tesis", page_icon = "🦅", layout = "wide", initial_sidebar_state = "collapsed")

# Funciones 
def f1_rpm(ne, tpo):
     if tpo == 'Escalonado':
          x1 = np.array([0, 300, 300, 700, 700, 800, 800, 700, 700, 300, 300, 0, 0])
          y1 = np.array([-50, -50, -125/2, -125/2, -50, -50, 50, 50, 125/2, 125/2, 50, 50, -50])
          x3 = np.array([0,0.0222,0.0444,0.0667,0.0889,0.1111,0.1333,0.1556,0.1778,0.2,0.2,0.2111,0.2222,0.2333,0.2444,0.2556,0.2667,0.2778,0.2889,0.3,0.3,0.3222,0.3444,0.3667,0.3889,0.4111,0.4333,0.4556,0.4778,0.5,0.5,0.5222,0.5444,0.5667,0.5889,0.6111,0.6333,0.6556,0.6778,0.7,0.7,0.7111,0.7222,0.7333,0.7444,0.7556,0.7667,0.7778,0.7889,0.8]) * 1000
          y3 = np.array([0,-0.000015454,-0.000030746,-0.000045714,-0.000060195,-0.000074029,-0.000087053,-0.000099105,-0.00011002,-0.00011964,-0.00011964,-0.00012392,-0.00012783,-0.00013135,-0.0001345,-0.00013725,-0.0001396,-0.00014155,-0.00014308,-0.0001442,-0.0001442,-0.00014566,-0.0001464,-0.0001464,-0.00014564,-0.00014409,-0.00014174,-0.00013855,-0.00013452,-0.00012961,-0.00012961,-0.00012382,-0.00011719,-0.00010981,-0.00010173,-0.00009302,-0.000083746,-0.000073973,-0.00006377,-0.000053201,-0.000053201,-0.000047749,-0.000042135,-0.000036379,-0.000030501,-0.000024522,-0.000018463,-0.000012342,-0.0000061812,-1.5847e-19]) * 1000 * 300 
          dt = np.array([100, 125, 100])
          lt = np.array([300, 400, 100])
          ls = np.array([0, 300, 700])
          nt = np.array([0, 300, 700, 800])

          x  = sp.symbols('x')
          f1 = (10737418240000 * x ** 3) / 4364154382556341 - (76005888753664 * x) / 109103859563908525;
          f2 = (10737418240000 * x ** 3) / 13092463147669023 + (4294967296000 * x ** 2) / 4364154382556341 - (97480725233664 * x) / 109103859563908525 + 171798691840 / 13092463147669023;
          f3 = (536870912000 * x ** 3) / 1598201067830691 + (214748364800 * x ** 2) / 532733689276897 - (220609904640 * x) / 532733689276897 - 5701196854941011 / 87283087651126804480;
          f4 = - (536870912000 * x ** 3) / 532733689276897 + (1288490188800 * x ** 2) / 532733689276897 - (757480816640 * x) / 532733689276897 + 54681141248 / 532733689276897;
          f5 = - (10737418240000 * x ** 3) / 4364154382556341 + (25769803776000 * x ** 2) / 4364154382556341 - (2327897013443625 * x) / 558611760967211648 + 7279083635225919/8937788175475386368;
          f  = [f1, f2, f3, f4, f5]
          p  = 7830.992242436808
          a  = np.pi * np.array([0.05, 0.05, 0.0625, 0.0625, 0.05]) ** 2
          li = np.array([0, 200, 300, 500, 700, 800]) / 1000
     else:
          x5 = np.array([0, 1500, 1500, 0, 0])
          y5 = np.array([-15, -15, 15, 15, -15])
          x1 = np.array([0, 1500, 1500, 0, 0])
          y1 = np.array([-25, -25, 25, 25, -25])
          x3 = np.array([0,0.0455,0.0909,0.1364,0.1818,0.2273,0.2727,0.3182,0.3636,0.4091,0.4545,0.5,0.5545,0.6091,0.6636,0.7182,0.7727,0.8273,0.8818,0.9364,0.9909,1.0455,1.1,1.1364,1.1727,1.2091,1.2455,1.2818,1.3182,1.3545,1.3909,1.4273,1.4636,1.5]) * 1000
          y3 = np.array([0,0.000046398,0.000092427,0.00013772,0.00018191,0.00022463,0.00026551,0.00030417,0.00034027,0.00037342,0.00040325,0.00042941,0.00045552,0.00047577,0.0004901,0.00049849,0.00050088,0.00049725,0.00048755,0.00047175,0.00044979,0.00042165,0.00038729,0.00036094,0.00033206,0.00030091,0.00026772,0.00023277,0.00019629,0.00015855,0.0001198,0.00008029,0.000040272,4.2574e-20]) * 1000 * 40 * -1
          dt = np.array([50, 50, 50])
          lt = np.array([500, 500, 500])
          ls = np.array([0, 500, 1000])
          nt = np.array([0, 500, 1000, 1500])

          x  = sp.symbols('x')
          f  = -0.0003041661947726438 * x ** 4 + 0.0009774450338568947 * x ** 3 - 0.00010769849260722366 * x ** 2 - 0.001009531675784642 * x - 3.392350409868671e-7
          p  = 7830.992242436808
          a  = np.pi * ((0.05 * 0.03) / 2) ** 2
          li = np.array([0, 500, 1100, 1500]) / 1000

     nc = ne - 1
     tc = np.array([])
     dc = np.array([])
     tp = np.array([])
     x2 = np.zeros((2, nc * 3))
     y2 = np.zeros((2, nc * 3))
     y4 = np.zeros((4, ne * 3))
     tv = np.array([])
     for i in range(3):
          nl = lt[i] / (nc + 1)
          lc = np.arange(1, nc + 1) * nl + ls[i]
          pe = np.arange(0, nc + 1) * nl + np.repeat(nl / 2, nc + 1) + ls[i]
          tc = np.concatenate((tc, lc))
          tp = np.concatenate((tp, pe))
          dc = np.concatenate((dc, np.repeat(dt[i] / 2, nc)))
          vo = np.repeat((np.pi * nl * dt[i] ** 2) / 4, ne)
          tv = np.concatenate((tv, vo))
     x2[0, :] = tc; x2[1, :] = tc
     y2[0, :] = dc; y2[1, :] = -dc
     x4 = np.repeat(np.sort(np.concatenate((tc, nt))), 4)[2:-2].reshape((4, ne * 3), order = 'F')
     y4[1, :] = np.interp(tp, x3, y3); y4[2, :] = np.interp(tp, x3, y3)
     centro_masa = tp / 1000
     volumen     = tv / 1e9
     peso        = 7830.992242436808 * volumen * 9.81
     sum1 = 0
     sum2 = 0

     if tpo == 'Escalonado':
          for i in range(5):
               sum1 += p * a[i] * abs(sp.integrate(f[i], (x, li[i], li[i + 1])))
               sum2 += p * a[i] * abs(sp.integrate(f[i] ** 2, (x, li[i], li[i + 1])))
          deflexion   = np.interp(tp, x3, y3 / 300) / 1000
          vel_dun_cla = (30 / np.pi) * np.sqrt(9.81 / max(abs(y3 / 300000)))
     else:
          for i in range(3):
               sum1 += p * a * abs(sp.integrate(f, (x, li[i], li[i + 1])))
               sum2 += p * a * abs(sp.integrate(f ** 2, (x, li[i], li[i + 1])))
          deflexion   = np.interp(tp, x3, y3 / 40) / 1000
          vel_dun_cla = (30 / np.pi) * np.sqrt(9.81 / max(abs(y3 / 40000)))

     vel_ray_cla = (30 / np.pi) * np.sqrt(9.81 * (np.sum(peso * abs(deflexion)) / np.sum(peso * deflexion ** 2)))
     vel_ray_mod = (30 / np.pi) * sp.sqrt(9.81 * (sum1 / sum2))
     table_data  = np.zeros((ne * 3, 4)); table_data[:, 0] = centro_masa * 1000; table_data[:, 1] = volumen * 1000000000; table_data[:, 2] = peso; table_data[:, 3] = deflexion * 1000
     data_frame  = pd.DataFrame(table_data, columns = ["Centro de masa (mm)", "Volumen (mm3)", "Peso (N)", "Deflexión (mm)"])
     
     fig, axs = plt.subplots(figsize = (8, 4))
     axs.plot(x1, y1, color = 'black', linestyle = 'solid', linewidth = 3)
     axs.plot(x2, y2, color = 'red', linestyle = 'dashed', linewidth = 1)
     axs.plot(x3, y3, color = 'green', linestyle = 'solid', linewidth = 2)
     axs.fill(x4, y4, color = 'blue', alpha = 0.3)
     axs.set_xlabel('x (mm)')
     axs.set_yticks([])
     axs.set_ylabel('')
     axs.spines['top'].set_visible(False)
     axs.spines['bottom'].set_visible(False)
     axs.spines['left'].set_visible(False)
     axs.spines['right'].set_visible(False)

     if tpo == 'Escalonado':
          axs.plot(np.array([[300, 700], [300, 700]]), np.array([[50, 50], [-50, -50]]), color = 'red', linestyle = 'dashed', linewidth = 1)
          axs.text(30, 20, r'$\frac{30}{\pi}\sqrt{\frac{g}{max(\delta_R)}}=$' + str(round(vel_dun_cla, 2)), fontsize = 11)
          axs.text(500, 30, r'$\frac{30}{\pi}\sqrt{g\frac{\sum m_i y_i}{\sum m_i y_{i}^{2}}}=$' + str(round(vel_ray_cla, 2)), fontsize = 11)
          axs.text(500, 10, r'$\frac{30}{\pi}\sqrt{g\frac{\sum \rho A\int y_{(x)}dx}{\sum \rho A\int y_{(x)}^{2}dx}}=$' + str(round(vel_ray_mod, 2)), fontsize = 11)
          axs.text(270, 20, r'$<V.C.R.<$', fontsize = 20)
     else:
          axs.plot(x5, y5, color = 'black', linestyle = 'dashed', linewidth = 1)
          axs.plot(np.array([[500, 1000], [500, 1000]]), np.array([[25, 25], [-25, -25]]), color = 'red', linestyle = 'dashed', linewidth = 1)
          axs.text(50, 6, r'$\frac{30}{\pi}\sqrt{\frac{g}{max(\delta_R)}}=$' + str(round(vel_dun_cla, 2)), fontsize = 11)
          axs.text(1000, 10, r'$\frac{30}{\pi}\sqrt{g\frac{\sum m_i y_i}{\sum m_i y_{i}^{2}}}=$' + str(round(vel_ray_cla, 2)), fontsize = 11)
          axs.text(1000, 3, r'$\frac{30}{\pi}\sqrt{g\frac{\sum \rho A\int y_{(x)}dx}{\sum \rho A\int y_{(x)}^{2}dx}}=$' + str(round(vel_ray_mod, 2)), fontsize = 11)
          axs.text(550, 6, r'$<V.C.R.<$', fontsize = 20)

     return fig, data_frame

def f2_img(x1, y1, img1):
     x  = np.array([5, 15, 25, 35])
     y  = np.array([20, 30, 50, 70, 100, 120, 150, 200, 300])
     z  = np.array([[0.1100, 0.1110, 0.1120, 0.1160],
                    [0.1140, 0.1158, 0.1190, 0.1240],
                    [0.1240, 0.1255, 0.1280, 0.1315],
                    [0.1300, 0.1310, 0.1330, 0.1355],
                    [0.1350, 0.1358, 0.1375, 0.1389],
                    [0.1370, 0.1379, 0.1390, 0.1405],
                    [0.1400, 0.1407, 0.1415, 0.1424],
                    [0.1420, 0.1425, 0.1430, 0.1435],
                    [0.1449, 0.1450, 0.1452, 0.1450]])
     fx = numint.interp1d([5, 35], [50, 550])
     fy = numint.interp1d([0.11, 0.148], [650, 20])
     fz = numint.interp2d(x, y, z)
     fg = np.round(fz(x1, y1)[0], 5)

     fig1, axe1 = plt.subplots()
     axe1.imshow(img1)
     axe1.plot([fx(x1), fx(x1)], [650, 20], 'red', linestyle = 'dashed')
     axe1.plot([50, 550], [fy(fz(x1, y1)), fy(fz(x1, y1))], 'red', linestyle = 'dashed')
     axe1.scatter(fx(x1), fy(fz(x1, y1)), 25, 'red')
     axe1.axis('off')

     return fg, fig1

def f3_des(rme, rma, lon, phi):
     tetha = np.linspace(0, 2 * np.pi, 50)
     x1 = 0
     y1 = 0
     x2 = lon * np.cos(phi * (np.pi / 180)) + x1
     y2 = lon * np.sin(phi * (np.pi / 180)) + y1
     d1 = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
     l1 = np.sqrt(d1 ** 2 - (rme - rma) ** 2)
     r1 = np.sqrt(l1 ** 2 + rma ** 2)
     s1 = 0.25 * np.sqrt((d1 + rme + r1) * (d1 + rme - r1) * (d1 - rme + r1) * (-d1 + rme + r1))
     r2 = np.sqrt(l1 ** 2 + rme ** 2)
     s2 = 0.25 * np.sqrt((d1 + rma + r1) * (d1 + rma - r1) * (d1 - rma + r1) * (-d1 + rma + r1))
     x3 = (x1 + x2) / 2 + ((x2 - x1) * (rme ** 2 - r1 ** 2)) / (2 * d1 ** 2) + 2 * ((y1 - y2) / d1 ** 2) * s1
     y3 = (y1 + y2) / 2 + ((y2 - y1) * (rme ** 2 - r1 ** 2)) / (2 * d1 ** 2) - 2 * ((x1 - x2) / d1 ** 2) * s1
     x4 = (x2 + x1) / 2 + ((x1 - x2) * (rma ** 2 - r2 ** 2)) / (2 * d1 ** 2) - 2 * ((y2 - y1) / d1 ** 2) * s2
     y4 = (y2 + y1) / 2 + ((y1 - y2) * (rma ** 2 - r2 ** 2)) / (2 * d1 ** 2) + 2 * ((x2 - x1) / d1 ** 2) * s2
     x5 = (x1 + x2) / 2 + ((x2 - x1) * (rme ** 2 - r1 ** 2)) / (2 * d1 ** 2) - 2 * ((y1 - y2) / d1 ** 2) * s1
     y5 = (y1 + y2) / 2 + ((y2 - y1) * (rme ** 2 - r1 ** 2)) / (2 * d1 ** 2) + 2 * ((x1 - x2) / d1 ** 2) * s1
     x6 = (x2 + x1) / 2 + ((x1 - x2) * (rma ** 2 - r2 ** 2)) / (2 * d1 ** 2) + 2 * ((y2 - y1) / d1 ** 2) * s2
     y6 = (y2 + y1) / 2 + ((y1 - y2) * (rma ** 2 - r2 ** 2)) / (2 * d1 ** 2) - 2 * ((x2 - x1) / d1 ** 2) * s2
     m1 = ((y4 - y3) / (x4 - x3))
     if phi >=0 and phi < 80:
          x7 = x2 - rma / (np.sqrt(m1 ** 2 + 1))
          y7 = y2 - (m1 * rma) / np.sqrt(m1 ** 2 + 1)
     elif phi >= 80 and phi <= 260:
          x7 = x2 + rma / (np.sqrt(m1 ** 2 + 1))
          y7 = y2 + (m1 * rma) / np.sqrt(m1 ** 2 + 1)
     else:
          x7 = x2 - rma / (np.sqrt(m1 ** 2 + 1))
          y7 = y2 - (m1 * rma) / np.sqrt(m1 ** 2 + 1)
     m2 = ((y6 - y5) / (x6 - x5))
     if phi >=0 and phi < 100:
          x8 = x2 - rma / (np.sqrt(m2 ** 2 + 1))
          y8 = y2 - (m2 * rma) / np.sqrt(m2 ** 2 + 1)
     elif phi >= 100 and phi <= 279:
          x8 = x2 + rma / (np.sqrt(m2 ** 2 + 1))
          y8 = y2 + (m2 * rma) / np.sqrt(m2 ** 2 + 1)
     else:
          x8 = x2 - rma / (np.sqrt(m2 ** 2 + 1))
          y8 = y2 - (m2 * rma) / np.sqrt(m2 ** 2 + 1)
     beta = np.round(np.arctan(m1) * (180 / np.pi), 2)
     alpa = np.round(np.arctan(m2) * (180 / np.pi), 2)

     fig2, axe2 = plt.subplots()
     axe2.plot(x1 + rme * np.cos(tetha), y1 + rme * np.sin(tetha), 'black')
     axe2.plot(x2 + rma * np.cos(tetha), y2 + rma * np.sin(tetha), 'black')
     axe2.plot([x3, x4], [y3, y4], 'red')
     axe2.plot([x5, x6], [y5, y6], 'blue')
     axe2.arrow(x2, y2, x7 - x2, y7 - y2, color = 'red', head_width = 0.02, width = 0.0025)
     axe2.arrow(x2, y2, x8 - x2, y8 - y2, color = 'blue', head_width = 0.02, width = 0.0025)
     axe2.plot([-50 * rma + x2, 50 * rma + x2], [y2, y2], color = 'green', linestyle = 'dotted')
     axe2.plot([x2, x2], [-50 * rma + y2, 50 * rma + y2], color = 'black', linestyle = 'dotted')
     axe2.set_xlim([-lon - 1.1 * rma, lon + 1.1 * rma])
     axe2.set_ylim([-lon - 1.1 * rma, lon + 1.1 * rma])
     axe2.set_aspect('equal', adjustable = 'box')
     axe2.axis('off')
     
     return fig2, beta, alpa
@st.cache_data
def f4_loa(resources):
     file_1   = open(r'Imagenes/Logo.gif', "rb")
     content1 = file_1.read()
     gif1     = base64.b64encode(content1).decode("utf-8")
     file_1.close()

     img1 = Image.open(r'Imagenes/forbo.png')
     img2 = Image.open(r'Imagenes/optibelt.png')
     img3 = Image.open(r'Imagenes/renold.png')
     img4 = Image.open(r'Imagenes/agma.png')
     img5 = Image.open(r'Imagenes/jack.png')
     img6 = Image.open(r'Imagenes/bandari.png')
     img7 = Image.open(r'Imagenes/logan.png')
     img8 = Image.open(r'Imagenes/maxelem.jpg')
     img9 = Image.open(r'Imagenes/maxelem1.jpg')
     img10 = Image.open(r'Imagenes/esfuerzoscf.jpg')
     img11 = Image.open(r'Imagenes/elem4.png')
     img12 = Image.open(r'Imagenes/FotografiaJR.png')

     imgn = mpimg.imread(f'Imagenes/carta1.png')

     return gif1, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, imgn
@st.cache_data
def f5_cyt(resources):
     elements1 = [
     {"data": {"id": "n1", "label": "•Potencia\n•R.P.M\n•Diametros de las poleas\n•Distancia entre las poleas"}, "selectable": False},
     {"data": {"id": "n2", "label": "•Angulos de contacto\n•Velocidad de la correa\n•Fuerza tangencial a transmitir\n•Factores\n•Perfil"}, "selectable": False},
     {"data": {"id": "n3", "label": "•Dimensiones de\nla correa"}, "selectable": False},
     {"data": {"id": "n4", "label": "•Fuerzas y momentos\nsobre el eje"}, "selectable": False},
     {"data": {"source": "n1", "target": "n2"}},
     {"data": {"source": "n2", "target": "n3"}},
     {"data": {"source": "n2", "target": "n4"}},
     ]
     layout1 = {
     "name": "preset",
     "positions": {  
          "n1": {"x": -500, "y": 50},
          "n2": {"x": -200, "y": 50},
          "n3": {"x": 100, "y": 0},
          "n4": {"x": 100, "y": 100},
     }
     }
     stylesheet1 = [
     {"selector": "node", "style": {"label": "data(label)", "text-wrap": "wrap", "width": 10, "height": 10, "shape": "circle"}},
     {"selector": "edge", "style": {"width": 2, "curve-style": "bezier", "target-arrow-shape": "triangle"}},
     ]
     elements2 = [
     {"data": {"id": "n1", "label": "•Potencia\n•R.P.M\n•Diametros de las poleas\n•Distancia entre las poleas"}, "selectable": False},
     {"data": {"id": "n2", "label": "•Angulos de contacto\n•Velocidad de la correa\n•Fuerza tangencial a transmitir\n•Factores\n•Perfil"}, "selectable": False},
     {"data": {"id": "n3", "label": "•Dimensiones de\nla correa"}, "selectable": False},
     {"data": {"id": "n4", "label": "•Número de\ncorreas"}, "selectable": False},
     {"data": {"id": "n5", "label": "•Fuerzas y momentos\nsobre el eje"}, "selectable": False},
     {"data": {"source": "n1", "target": "n2"}},
     {"data": {"source": "n2", "target": "n3"}},
     {"data": {"source": "n2", "target": "n4"}},
     {"data": {"source": "n2", "target": "n5"}},
     ]
     layout2 = {
     "name": "preset",
     "positions": {  
          "n1": {"x": -500, "y": 50},
          "n2": {"x": -200, "y": 50},
          "n3": {"x": 100, "y": 0},
          "n4": {"x": 100, "y": 50},
          "n5": {"x": 100, "y": 100},
     }
     }
     stylesheet2 = [
     {"selector": "node", "style": {"label": "data(label)", "text-wrap": "wrap", "width": 10, "height": 10, "shape": "circle"}},
     {"selector": "edge", "style": {"width": 2, "curve-style": "bezier", "target-arrow-shape": "triangle"}},
     ]
     elements3 = [
     {"data": {"id": "n1", "label": "•Potencia\n•R.P.M\n•Dientes de los sprockets\n•Distancia entre los sprockets"}, "selectable": False},
     {"data": {"id": "n2", "label": "•Angulos de contacto\n•Velocidad de la cadena\n•Fuerza tangencial a transmitir\n•Factores\n•Perfil"}, "selectable": False},
     {"data": {"id": "n3", "label": "•Dimensiones de\nla cadena"}, "selectable": False},
     {"data": {"id": "n4", "label": "•Número de\ncadenas"}, "selectable": False},
     {"data": {"id": "n5", "label": "•Fuerzas y momentos\nsobre el eje"}, "selectable": False},
     {"data": {"source": "n1", "target": "n2"}},
     {"data": {"source": "n2", "target": "n3"}},
     {"data": {"source": "n2", "target": "n4"}},
     {"data": {"source": "n2", "target": "n5"}},
     ]
     layout3 = {
     "name": "preset",
     "positions": {  
          "n1": {"x": -500, "y": 50},
          "n2": {"x": -200, "y": 50},
          "n3": {"x": 100, "y": 0},
          "n4": {"x": 100, "y": 50},
          "n5": {"x": 100, "y": 100},
     }
     }
     stylesheet3 = [
     {"selector": "node", "style": {"label": "data(label)", "text-wrap": "wrap", "width": 10, "height": 10, "shape": "circle"}},
     {"selector": "edge", "style": {"width": 2, "curve-style": "bezier", "target-arrow-shape": "triangle"}},
     ]
     elements4 = [
     {"data": {"id": "n1", "label": "Tratamiento superficial"}, "selectable": False},
     {"data": {"id": "n2", "label": "Condiciones de operación"}, "selectable": False},
     {"data": {"id": "n3", "label": "Número de nodos"}, "selectable": False},
     {"data": {"id": "n4", "label": "Momentos"}, "selectable": False},
     {"data": {"id": "n5", "label": "Fuerzas"}, "selectable": False},
     {"data": {"id": "n6", "label": "Tipos de apoyo"}, "selectable": False},
     {"data": {"id": "n7", "label": "Densidad"}, "selectable": False},
     {"data": {"id": "n8", "label": "Esfuerzo de rotura"}, "selectable": False},
     {"data": {"id": "n9", "label": "Esfuerzo de fluencia"}, "selectable": False},
     {"data": {"id": "n10", "label": "Módulo de rigidez"}, "selectable": False},
     {"data": {"id": "n11", "label": "Módulo de elasticidad"}, "selectable": False},
     {"data": {"id": "n12", "label": "Redondeos y similares"}, "selectable": False},
     {"data": {"id": "n13", "label": "Longitud"}, "selectable": False},
     {"data": {"id": "n14", "label": "Diámetro externo"}, "selectable": False},
     {"data": {"id": "n15", "label": "Diámetro interno"}, "selectable": False},
     {"data": {"id": "n16", "label": "Area"}, "selectable": False},
     {"data": {"id": "n17", "label": "Momento polar de inercia"}, "selectable": False},
     {"data": {"id": "n18", "label": "Segundo momento de área"}, "selectable": False},
     {"data": {"id": "n19", "label": "Primer momento de área"}, "selectable": False},
     {"data": {"id": "n20", "label": "Esfuerzos dinámicos máximos"}, "selectable": False},
     {"data": {"id": "n21", "label": "Esfuerzos dinámicos"}, "selectable": False},
     {"data": {"id": "n22", "label": "Esfuerzos estáticos máximos"}, "selectable": False},
     {"data": {"id": "n23", "label": "Esfuerzos estáticos"}, "selectable": False},
     {"data": {"id": "n24", "label": "Desplazamientos"}, "selectable": False},
     {"data": {"id": "n25", "label": "Reacciones"}, "selectable": False},
     {"data": {"id": "n26", "label": "Velocidades Críticas"}, "selectable": False},
     {"data": {"id": "n27", "label": "F.S. dinamicos mínimos"}, "selectable": False},
     {"data": {"id": "n28", "label": "F.S. dinámicos"}, "selectable": False},
     {"data": {"id": "n29", "label": "F.S. estáticos mínimos"}, "selectable": False},
     {"data": {"id": "n30", "label": "F.S. estáticos"}, "selectable": False},
     {"data": {"source": "n6", "target": "n24"}},
     {"data": {"source": "n7", "target": "n24"}},
     {"data": {"source": "n10", "target": "n24"}},
     {"data": {"source": "n11", "target": "n24"}},
     {"data": {"source": "n13", "target": "n24"}},
     {"data": {"source": "n14", "target": "n24"}},
     {"data": {"source": "n16", "target": "n24"}},
     {"data": {"source": "n17", "target": "n24"}},
     {"data": {"source": "n25", "target": "n24"}},
     {"data": {"source": "n24", "target": "n25"}},
     {"data": {"source": "n24", "target": "n26"}},
     {"data": {"source": "n4", "target": "n25"}},
     {"data": {"source": "n5", "target": "n25"}},
     {"data": {"source": "n13", "target": "n25"}},
     {"data": {"source": "n25", "target": "n20"}},
     {"data": {"source": "n25", "target": "n21"}},
     {"data": {"source": "n25", "target": "n22"}},
     {"data": {"source": "n25", "target": "n23"}},
     {"data": {"source": "n25", "target": "n27"}},
     {"data": {"source": "n25", "target": "n28"}},
     {"data": {"source": "n25", "target": "n29"}},
     {"data": {"source": "n25", "target": "n30"}},
     {"data": {"source": "n1", "target": "n21"}},
     {"data": {"source": "n2", "target": "n21"}},
     {"data": {"source": "n8", "target": "n27"}},
     {"data": {"source": "n8", "target": "n28"}},
     {"data": {"source": "n9", "target": "n27"}},
     {"data": {"source": "n9", "target": "n28"}},
     {"data": {"source": "n9", "target": "n29"}},
     {"data": {"source": "n9", "target": "n30"}},
     {"data": {"source": "n12", "target": "n20"}},
     {"data": {"source": "n12", "target": "n22"}},
     {"data": {"source": "n12", "target": "n27"}},
     {"data": {"source": "n12", "target": "n29"}},
     {"data": {"source": "n14", "target": "n16"}},
     {"data": {"source": "n14", "target": "n17"}},
     {"data": {"source": "n14", "target": "n18"}},
     {"data": {"source": "n14", "target": "n19"}},
     {"data": {"source": "n15", "target": "n16"}},
     {"data": {"source": "n15", "target": "n17"}},
     {"data": {"source": "n15", "target": "n18"}},
     {"data": {"source": "n15", "target": "n19"}},
     {"data": {"source": "n18", "target": "n21"}},
     {"data": {"source": "n18", "target": "n23"}},
     {"data": {"source": "n19", "target": "n21"}},
     {"data": {"source": "n19", "target": "n23"}},
     ]
     layout4 = {
     "name": "preset",
     "positions": {  
          "n1": {"x": -500, "y": 0},
          "n2": {"x": -500, "y": 80},
          "n3": {"x": -500, "y": 160},
          "n4": {"x": -500, "y": 240},
          "n5": {"x": -500, "y": 320},
          "n6": {"x": -500, "y": 400},
          "n7": {"x": -200, "y": 40},
          "n8": {"x": -200, "y": 120},
          "n9": {"x": -200, "y": 200},
          "n10": {"x": -200, "y": 280},
          "n11": {"x": -200, "y": 360},
          "n12": {"x": 100, "y": 80},
          "n13": {"x": 100, "y": 160},
          "n14": {"x": 100, "y": 240},
          "n15": {"x": 100, "y": 320},
          "n16": {"x": 400, "y": 80},
          "n17": {"x": 400, "y": 160},
          "n18": {"x": 400, "y": 240},
          "n19": {"x": 400, "y": 320},
          "n20": {"x": 700, "y": 0},
          "n21": {"x": 700, "y": 80},
          "n22": {"x": 700, "y": 160},
          "n23": {"x": 700, "y": 240},
          "n24": {"x": 700, "y": 320},
          "n25": {"x": 700, "y": 400},
          "n26": {"x": 1000, "y": 40},
          "n27": {"x": 1000, "y": 120},
          "n28": {"x": 1000, "y": 200},
          "n29": {"x": 1000, "y": 280},
          "n30": {"x": 1000, "y": 360},
     }
     }
     stylesheet4 = [
     {"selector": "node", "style": {"label": "data(label)", "text-wrap": "wrap", "width": 220, "height": 30, "shape": "round-rectangle", "text-valign": "center", "text-halign": "center"}},
     {"selector": "edge", "style": {"width": 2, "curve-style": "unbundled-bezier", "target-arrow-shape": "triangle"}},
     ]
     return elements1, layout1, stylesheet1, elements2, layout2, stylesheet2, elements3, layout3, stylesheet3, elements4, layout4, stylesheet4

# Se cargan las imagenes y los datos para los diagramas
gif1, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, imgn = f4_loa('resources')
elements1, layout1, stylesheet1, elements2, layout2, stylesheet2, elements3, layout3, stylesheet3, elements4, layout4, stylesheet4 = f5_cyt('resoruces')

# Titulo y encabezado
st.markdown("<h1 style='text-align: center; color: black;'>Power System Transmission Calculator</h1>", unsafe_allow_html = True)
st.markdown("<h6 style='text-align: center; color: black;'>Proyecto de tesis para obtener el grado de Ingeniero Mecánico</h1>", unsafe_allow_html = True)
st.markdown("<h6 style='text-align: center; color: black;'>Universidad Nacional de San Agustin</h1>", unsafe_allow_html = True)
st.markdown("<h6 style='text-align: center; color: black;'>Arequipa - 2023</h1>", unsafe_allow_html = True)
st.divider()

# Resumen
col1, col2 = st.columns([1.5, 1], gap = 'large')
with col1:
     st.header('Resumen')
     st.markdown('''<div style="text-align: justify;">
          El presente proyecto de investigación se realizo con la finalidad de optimizar el proceso de diseño de un
          sistema de transmisión de potencia como el que se muestra en la imagen. Para ello se analizaron los
          componentes generales de dichos sistemas, tales como las correas, cadenas, engranajes, ejes y chavetas,
          en base a las distintas metodologias, criterios y normativas que existen en la actualidad.  \nUna vez establecido 
          el proceso de calculo para cada uno de ellos, se desarrollo una interfaz gráfica para que el usuario pueda
          mejorar su diseño mediante la variación de los parametros iniciales del sistema.  \nComo resultado final se
          creó Power System Transmission Calculator, una aplicación informática que permite cálcular los componentes previamente
          mencionados, de manera rapida, precisa y optima, cumpliendo asi con el proposito establecido en el proyecto de investigación.
     </div>''', unsafe_allow_html = True)
with col2:
     st.markdown(f'<img src = "data:image/gif;base64,{gif1}" width = "450">', unsafe_allow_html = True)

# Marco Teorico
st.header('Marco Teórico')
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Correas planas', 'Correas trapezoidales', 'Cadenas', 'Engranajes', 'Ejes de transmisión', 'Chavetas y rodamientos', 'Elementos finitos'])
# Correas planas
with tab1:
     st.subheader('Correas planas')
     col7, col8 = st.columns([1,3])
     with col7:
          st.image(img1.resize((600, 800)))
     with col8:
          st.markdown('''<div style="text-align: justify;">
               Se analizan bajo la metodología desarrollada por la empresa Forbo, la cual, mediante datos de entrada 
               conocidos como la potencia y revoluciones del motor, los diámetros de las poleas y la distancia entre 
               las mismas, permite calcular las dimensiones del tipo de correa elegida junto con las fuerzas que se 
               transmitirán al eje de transmisión de potencia.
          </div>''', unsafe_allow_html = True)
          st.markdown('#####')
          with st.expander("Diagrama", expanded = True):
               cytoscape(elements = elements1, stylesheet = stylesheet1, layout = layout1, selection_type = "single", key = "cyto1", 
               user_panning_enabled = True, user_zooming_enabled = True, min_zoom = 1, max_zoom = 1.75, width = "100%", height = "220px")
# Correas trapezoidales
with tab2:
     st.subheader('Correas trapezoidales')
     col9, col10 = st.columns([1,3])
     with col9:
          st.image(img2.resize((600, 800)))
     with col10:
          st.write('''
               Se analizan bajo la metodología desarrollada por la empresa Optibelt, la cual, mediante datos de 
               entrada conocidos como la potencia y revoluciones del motor, los diámetros de las poleas y la distancia 
               entre las mismas, permite calcular el número de correas a emplear, las dimensiones del tipo de correa 
               elegida junto con las fuerzas que se transmitirán al eje de transmisión de potencia.
          ''')
          with st.expander("Diagrama"):
               cytoscape(elements = elements2, stylesheet = stylesheet2, layout = layout2, selection_type = "single", key = "cyto2", 
               user_panning_enabled = True, user_zooming_enabled = True, min_zoom = 1, max_zoom = 1.75, width = "100%", height = "220px")
# Cadenas
with tab3:
     st.subheader('Cadenas')
     col11, col12 = st.columns([1,3])
     with col11:
          st.image(img3.resize((600, 800)))
     with col12:
          st.write('''
               Se analizan bajo la metodología desarrollada por la empresa Renold, la cual, mediante datos de entrada 
               conocidos como la potencia y revoluciones del motor, el número de dientes de los sprokets y la distancia 
               entre los mismos, permite calcular el número de cadenas a emplear, las dimensiones del tipo de cadena 
               elegida junto con las fuerzas que se transmitirán al eje de transmisión de potencia.
          ''')
          with st.expander("Diagrama"):
               cytoscape(elements = elements3, stylesheet = stylesheet3, layout = layout3, selection_type = "single", key = "cyto3", 
               user_panning_enabled = True, user_zooming_enabled = True, min_zoom = 1, max_zoom = 1.75, width = "100%", height = "220px")
# Engranajes
with tab4:
     st.subheader('Engranajes')
     col13, col14 = st.columns([1,3])
     with col13:
          st.image(img4.resize((600, 800)))
     with col14:
          st.markdown('''
               Se analizan bajo la norma ANSI / AGMA 2101-D04, en la cual se definen cuatro tipos de fallas, 
               de las cuales las más importantes son la falla por picadura y la falla por flexión. La aplicación permite el cálculo 
               de los siguientes tipos de engranajes:

               + Engranajes rectos
               + Engranajes helicoidales y bihelicoidales
               + Engranajes conicos rectos

               Los cálculos se realizan aplicando las siguientes ecuaciones:
          ''')
          st.latex(r'\begin{array}{c|cc} & \text{Falla por picadura} & \text{Falla por flexión} \\\hline \\ \text{Esfuerzo} & \sigma_h = Z_e\sqrt{\frac{F_t K_o K_v K_s K_h Z_r}{d_{w1}bZ_i}} & \sigma_f = \frac{F_t K_o K_v K_s K_h K_b}{bm_t Y_j} \\ \text{Esfuerzo admisible} & \sigma_{ha} = \frac{\sigma_{hp}Z_n Z_w}{S_h Y_\theta Y_z} & \sigma_{fa} = \frac{\sigma_{fp}Y_n}{S_f Y_\theta Y_z} \\ \text{Potencia} & P_{az} = \frac{\pi \omega_1 bZ_i}{6.10^7 K_o K_v K_s K_h Z_r}\left(\frac{d_{w1} \sigma_{hp} Z_n Z_w}{Z_e S_h Y_\theta Y_z}\right)^2 & P_{ay} = \frac{\pi \omega_1 d_{w1} b m_t Y_j \sigma_{fp} Y_n}{6.10^7 K_o K_v K_s K_h K_b S_f Y_\theta Y_z} \end{array}')
# Ejes
with tab5:
     col15, col16 = st.columns([1, 3])
     with col15:
          st.subheader('Ejes de transmisión')
          st.image(img5.resize((600, 800)))
     with col16:
          with st.expander('Teorías', expanded = True):
               st.markdown('''
                    + Euler-Bernoulli: No toma en cuenta los efectos de las fuerzas cortantes 
                    en la deformación del eje, por lo que resulta adecuada para ejes largos ($L/D>10$).
                    + Timoshenko: Toma en cuenta los efectos de las fuerzas cortantes 
                    en la deformación del eje, por lo que resulta adecuada para ejes cortos ($L/D<10$). 
                    
                    Independientemente de la teoría que se elija, el analisis del eje se realiza bajo los siguientes criterios:
               ''')
               st.latex(r'\small \begin{array}{cccc} \text{Análisis estático} & \text{Análisis dinámico} & \text{Análisis vibracional} & \text{Análisis de rigidez}\\ \hline \\ \text{Von Misses} & \text{Soderberg} & \text{Dunkerley} & \text{Pendientes} \\\\ \text{Tresca} & \text{Goodman} & \text{Rayleigh} & \text{Deflexiones} \\\\ \text{Rankine} & \text{ASME} & & \\ \end{array}')               
          with st.expander('Diagrama'):
               cytoscape(elements = elements4, stylesheet = stylesheet4, layout = layout4, selection_type = "single", key = "cyto4", 
               user_panning_enabled = True, user_zooming_enabled = True, min_zoom = 0.5, max_zoom = 0.75, width = "100%", height = "310px")               
# Chavetas y rodamientos
with tab6:
     st.subheader('Chavetas')
     col17, col18 = st.columns([1, 3])
     with col17:
          st.image(img6.resize((600, 800)))
     with col18:
          st.write('''
               Se analizan bajo la metodología desarrollada en el libro "Diseño de elementos de máquinas" de Bhandari y unicamente se 
               computan las chavetas del tipo cuadradas. Por otra parte, los rodamientos se pueden diseñar por medio de una 
               herramienta gratuita proporcionada por la empresa [SKF](https://www.skfbearingselect.com/#/bearing-selection-start):
          ''')
# Elementos finitos
with tab7:
     st.subheader('Elementos finitos')
     col19, col20 = st.columns([1, 3])
     with col19:
          st.image(img7.resize((600, 800)))
     with col20:
          st.write('''
               Se utilzan los elementos triangulares de deformación constante (CST) para el analisis de componentes 
               bidimensionales sometidos a esfuerzos y deformaciones planas. Para ello, se establecen las siguientes 
               ecuaciones y matrices que permiten calcular los esfuerzos y deformaciones de cada elemento:
          ''')
          st.latex(r'\begin{align*} \beta_i=y_j-y_m \hspace{0.6cm}& \beta_j=y_m-y_i \hspace{0.3cm}& \beta_m=y_i-y_j\\ \gamma_i=x_m-x_j \hspace{0.6cm}& \gamma_j=x_i-x_m \hspace{0.3cm}& \gamma_m=x_j-x_i\\ \end{align*}')
          st.latex(r'[B]=\frac{1}{2A}\begin{bmatrix} \beta_i & 0 & \beta_j & 0 & \beta_m & 0 \\ 0 & \gamma_i & 0 & \gamma_j & 0 & \gamma_m \\ \gamma_i & \beta_i & \gamma_j & \beta_j & \gamma_m & \beta_m \\ \end{bmatrix} [D] = \frac{E}{1-v^2}\begin{bmatrix} 1 & v & 0 \\ v & 1 & 0 \\ 0 & 0 & \frac{1-v}{2} \\ \end{bmatrix}')
          st.latex(r'[k]=tA[B]^T[D][B]')
          st.latex(r'[F]=[K][d] → [\sigma_x, \sigma_y, \tau_{xy}] = [D][B][d]')

# Marco Metodologico
st.header('Marco Metodológico')
# Calculo de factores
st.subheader('Correas planas, correas trapezoidales, cadenas y engranajes')
col3, col4 = st.columns([1, 1])
with col3:
     with st.form('form1'):
          st.markdown('''<div style="text-align: justify;">
               En el proceso de cálculo de estos componentes resulta 
               indispensable hacer uso de parámetros numéricos exclusivos de cada uno de estos, los cuales por lo general, se representan y determinan 
               mediante el uso de gráficos y tablas. En este punto, resulta pertinente señalar que, mediante el procesamiento de imágenes se han extraido los datos de las gráficas 
               correspondientes a cada uno de estos parametros numéricos, para poder representarlos mediante tablas y, posteriormente, mediante 
               interpolaciones, poder calcular el parámetro numérico deseado de manera rapida y precisa. Para esto último, se hacen uso de las siguientes ecuaciones
          </div>''', unsafe_allow_html = True)
          st.markdown('#####')
          st.latex(r'{x_{{n_{a,b}}}} = \frac{{{x_{{n_{b,a}}}} - {x_{{1_{b,a}}}}}}{{{x_{{2_{b,a}}}} - {x_{{1_{b,a}}}}}}\left( {{x_{{2_{a,b}}}} - {x_{{1_{a,b}}}}} \right) + {x_{{1_{a,b}}}}')
          st.latex(r'{y_{{n_{a,b}}}} = \frac{{{y_{{n_{b,a}}}} - {y_{{1_{b,a}}}}}}{{{y_{{2_{b,a}}}} - {y_{{1_{b,a}}}}}}\left( {{y_{{2_{a,b}}}} - {y_{{1_{a,b}}}}} \right) + {y_{{1_{a,b}}}}')
          st.markdown('#####')
          st.write('Con los parametros numéricos ya tabulados, el cálculo se efectúa como sigue:')
          slider_1 = st.slider('Ángulo', 5, 35, 5, 1)
          slider_2 = st.slider('Dientes', 20, 300, 20, 1)
          col5, col6 = st.columns([1.55, 1])
          with col5:
               submitted1 = st.form_submit_button("Cálcular factor geométrico")
          with col6:
               fg, fig1 = f2_img(slider_1, slider_2, imgn)
               st.write('El factor geometrico es: ' + str(fg))
with col4:
     st.pyplot(fig1)
# Calculo de los angulos de descomposicion
col25, col26 = st.columns([1, 1])
with col26:
     with st.form('form2'):
          st.markdown('''<div style="text-align: justify;">
               Por otra parte, en la mayoría de casos, la trasmisión de potencia hacia el eje se dará de manera indirecta, es decir, 
               por medio de corras o cadenas, las cuales podrian ubicarse en distintas configuraciones geométricas.
               En concecuencia, para efectos de un análisis más realista, las fuerzas que actúan en el eje producto de la transmisión de 
               potencia, deben de descomponerse en ejes alineados en las direcciones paralela y perpendicular a la gravedad. Los ángulos 
               de descomposición son:
          </div>''', unsafe_allow_html = True)
          st.latex(r'\beta = 90 + \varphi  - \phi \hspace{3mm} \text{y} \hspace{3mm} \alpha = 2\varphi - \beta')
          st.latex(r'\text{donde} \hspace{10mm} \phi = \cos^{-1} \left( \frac{R - r}{a} \right)')
          col27, col28 = st.columns([1,1])
          with col27:
               number_input_1 = st.number_input('Radio menor (r)', 0.0, 1.05, 0.2, 0.05)
               number_input_2 = st.number_input('Radio mayor (R)', 0.0, 1.05, 0.1, 0.05)
               submitted2 = st.form_submit_button('Cálcular ángulos')
          with col28:
               number_input_3 = st.number_input('Distancia entre centros (a)', 0.0, 1.05, 0.4, 0.05)
               number_input_4 = st.number_input('Angulo de desfase (𝜑)', 0, 360, 45, 1)
          st.markdown('''<div style="text-align: justify;">
               Al momento de efectuar la descomposición de las fuerzas sobre el eje debe de tenerse en cuenta el sentido de giro del motor.
          </div>''', unsafe_allow_html = True)
          st.markdown('#####')
with col25:
     fig2, beta, alpa = f3_des(number_input_1, number_input_2, number_input_3, number_input_4)
     st.pyplot(fig2, use_container_width = True)
col28.markdown(f':red[$\large β = {beta}$] $\quad$ :blue[$\large α = {alpa}$]')
# Calculo de ejes
st.subheader('Ejes de transmisión')
# Calculo de ejes - Analítico
st.markdown('#### Cálculo general de las reacciones y desplazamientos mediante ecuaciones análiticas (Euler - Bernoulli)')
st.markdown('''<div style="text-align: justify;">
     Mediante el uso del método de las integraciones concecutivas se pueden cálcular las reacciones y desplazamientos correspondientes a un eje 
     con propiedades geométricas y mecánicas no constantes, sometido a cualquier cantidad de fuerzas, momentos y apoyos. El procedimiento de
     cálculo inicia con la formulación de la ecuación analítica de las fuerzas cortantes (fuerzas puntuales y distribuidas en el diagrama de cuerpo libre), 
     para posteriormente realizar integraciones concecutivas de dicha ecuacíon, con lo cual se obtienen las siguientes ecuaciones: 
</div>''', unsafe_allow_html = True)
st.latex(r'''  
     \begin{array}{|c | c |c |}\hline\\
     \text{ Ecuación } & \text{ Representativa } & \text{ Aplicativa:}\hspace{5mm} para\;k = 1\; \to \;T\hspace{5mm}\text{ donde T es el numero de tramos del eje} \\\\\hline\\
     \text{Cortantes}       & {{V_T} = \int\limits_{{x_T}}^{{x_{T + 1}}} {{W_T}(x)dx} }           & {V_k}(x) =  - \sum\limits_{i = 1}^k {{F_i}}  - {w_k}(x - {x_k}) - \sum\limits_{i = 1}^{k} {{w_{i-1}}({x_{i}} - {x_{i-1}})}\\\\\hline\\
     \text{Momentos}      & {{M_T} = \int\limits_{{x_T}}^{{x_{T + 1}}} {{V_T}(x)dx} }              & {M_k}(x) =  - x\sum\limits_{i = 1}^k {{F_i}}  - \frac{1}{2}{w_k}{(x - {x_k})^2} - x\sum\limits_{i = 1}^k {{w_{i - 1}}({x_i} - {x_{i - 1}})}  + {C_{{1_k}}} + {M_k} \\\\\hline\\
     \text{Pendientes}     & {{\theta _T} = \frac{{\int\limits_{{x_T}}^{{x_{T + 1}}} {{M_T}(x)dx} }}{{{E_T}{I_T}}}}             & {E_k}{I_k}{\theta _k}(x) = { - \frac{{{x^2}}}{2}\sum\limits_{i = 1}^k {{F_i}}  - \frac{1}{6}{w_k}{{(x - {x_k})}^3} - \frac{{{x^2}}}{2}\sum\limits_{i = 1}^k {{w_{i - 1}}({x_i} - {x_{i - 1}})}  + {C_{{1_k}}}x + {M_k}x + {C_{{2_k}}}} \\\\\hline\\
     \hspace{2mm}\text{Deflexiones}\hspace{2mm}     & \hspace{4mm} {{y_T} = \int\limits_{{x_T}}^{{x_{T + 1}}} {{\theta _T}(x)dx} } \hspace{4mm} & \hspace{5mm} {E_k}{I_k}{y_k}(x) = { - \frac{{{x^3}}}{6}\sum\limits_{i = 1}^k {{F_i}}  - \frac{1}{{24}}{w_k}{{(x - {x_k})}^4} - \frac{{{x^3}}}{6}\sum\limits_{i = 1}^k {{w_{i - 1}}({x_i} - {x_{i - 1}})}  + \frac{{{C_{{1_k}}}{x^2}}}{2} + \frac{{{M_k}{x^2}}}{2} + {C_{{2_k}}}x + {C_{{3_k}}}} \hspace{5mm}\;\\\\\hline
     \end{array}
''')
col21, col22 = st.columns([2, 1], gap = 'large')
with col21:
     st.latex(r'''
          {\begin{array}{|c | c |c |c |c |}\hline
          \\\text{Tramo} & \text{Cortantes} & \text{Momentos} & \text{Sustitucion} & \text{Resultados} \\\\\hline\\
          {{x_1} \to {x_2}}& {{V_1}(x) = \int {{w_1}(x)} } & {{M_0}({x_1}) = \int {{V_1}(x) + {C_{{1_1}}} + {M_1}} } & {x = {x_1}} & {{C_{{1_1}}}} \\
          &   & {{M_1}(x) = \int {{V_1}(x) + {C_{{1_1}}} + {M_1}} } & {x = {x_2}} & {{M_1}({x_2})} \\\\\hline\\
          {{x_2} \to {x_3}} & {{V_2}(x) = \int {{w_2}(x)} } & {{M_1}({x_2}) = \int {{V_2}(x) + {C_{{1_2}}} + {M_2}} } & {x = {x_2}} & {{C_{{1_2}}}} \\              
          &   & {{M_2}(x) = \int {{V_2}(x) + {C_{{1_2}}} + {M_2}} } & {x = {x_3}} & {{M_2}({x_3})} \\\\\hline \\
          \vdots & \vdots & \vdots & \vdots & \vdots \\ 
          {{x_T} \to {x_{T + 1}}} & {{V_T}(x) = \int {{w_T}(x)} } & {{M_{T - 1}}({x_T}) = \int {{V_T}(x) + {C_{{1_T}}} + {M_T}} } & {x = {x_T}} & {{C_{{1_T}}}} \\          
          &  & {{M_T}(x) = \int {{V_T}(x) + {C_{{1_T}}} + {M_T}} } & {x = {x_{T + 1}}} & {{M_T}({x_{T + 1}})} \\\\\hline
          \end{array}}
     ''')
with col22:
     st.markdown('#####')
     st.markdown('####')
     st.markdown('''<div style="text-align: justify;">
          En las ecuaciones planteadas se observa que existen tres constantes de integración, las cuales junto con las reacciones en los apoyos, 
          actuan como incognitas a despejar; no obstante, 
          la primera de estas constantes de integración, se computa de manera simultanea con la integración de la ecuación de cortantes 
          para el cálculo de la ecuación de momentos, seguiendo el procedimiento que se describe en el cuadro de la izquierda.
          En concecuencia, el valor de dicha constante se cálcula mediante la siguiente expresión: 
     </div>''', unsafe_allow_html = True)
     st.markdown('#####')
     st.latex(r'''
          {{C_{{1_k}}} = {M_{k - 1}}({x_k}) - \int {{V_k}({x_k}) - {M_k}}}
     ''')
col23, col24 = st.columns([2.1, 1], gap = 'medium')
with col23:
     st.markdown('#')
     st.markdown('''<div style="text-align: justify;">
          Dado que las reacciones a cálcular dependen del tipo de apoyos presentes en el eje, se puede definir el número de incógnitas por 
          reacciones, en función al número y tipo de apoyos; mientras que el número de constantes de integración a cálcular se puede definir
          a partir del número de tramos del eje. Entonces, si [AS] representa el número de apoyos simples, [AE] representa el número de apoyos 
          elásticos, [AF] representa el número de apoyos fijos y [T] representa el número de tramos del eje, se concluye que:
     </div>''', unsafe_allow_html = True)
     st.markdown('#####')
     st.markdown('+ Número de reacciones a cálcular: $2AS + 3AE + 6AF$')
     st.markdown('+ Número de constantes de integración a cálcular: $4T$')
     st.markdown('+ Número total de incognitas a cálcular: $4T + 2AS + 3AE + 6AF$')
with col24:
     st.latex(r'''
          \begin{array}{|c | c |c |c |}\hline
          \hspace{2mm} \text{Apoyo} \hspace{2mm}& \hspace{2mm}\text{Simple} \hspace{2mm}& \text{Elastico} &\hspace{3mm} \text{Fijo} \hspace{3mm}\\\hline
          F_z & \checkmark & \checkmark & \checkmark \\\hline
          F_y & \checkmark & \checkmark & \checkmark \\\hline
          F_x & \times & \checkmark & \checkmark \\\hline
          M_z & \times & \times & \checkmark \\\hline
          M_y & \times & \times & \checkmark \\\hline
          M_x & \times & \times & \checkmark \\\hline
          \delta_z & \times & \times & \times \\\hline
          \delta_y & \times & \times & \times \\\hline
          \delta_x & \checkmark & \times & \times \\\hline
          \theta_z & \checkmark & \checkmark & \times \\\hline
          \theta_y & \checkmark & \checkmark & \times \\\hline
          \theta_x & \checkmark & \checkmark & \times \\\hline
          \end{array}
     ''')
st.markdown('''<div style="text-align: justify;">
     En línea con lo anterior, es necesario establecer un sistema de ecuaciones con dimensión igual al numero de incognitas calculado. 
     Las ecuaciones para dicho sistema, se formulan a partir de las condiciones de frontera presentes en cada uno de los apoyos, de las condiciones 
     de continuidad en las ecuaciones analíticas de pendientes y deflexiones, y de las condiciones que establece el equilibrio 
     estático paras las fuerzas y momentos. El sistema de ecuaciones es el siguiente:
</div>''', unsafe_allow_html = True)
st.latex(r'''\large
     \begin{array}{|c | c |c |}\hline\\
     \text{Condición} & \text{Ecuación} & \text{Número de ecuaciones} \\\\\hline\\ 
     \delta_x=0 & \sum_{i=1}^{T}\frac{F_{x_i}(x_{i+1}-x_i)}{E_iA_i}=0 & AE+AF-1 \\\\\hline\\ 
     \delta_y=0 & y_{(x)_T}=0 & AS+AE+AF \\\\\hline\\ 
     \delta_z=0 & z_{(x)_T}=0 & AS+AE+AF\\\\\hline\\ 
     \theta_x=0 & \sum_{i=1}^{T}\frac{M_{x_i}(x_{i+1}-x_i)}{J_iG_i}=0 & AF-1 \\\\\hline\\ 
     \theta_y=0 & \alpha_{(x)_T}=0 & AF \\\\\hline\\ 
     \theta_z=0 & \beta_{(x)_T}=0 & AF \\\\\hline\\ 
     \delta_{T_2}=\delta_{T+1_1} & y_{(x_2)_T}=y_{(x_1)_{T+1}} & T-1 \\ 
     & z_{(x_2)_T}=z_{(x_1)_{T+1}} & T-1 \\\\\hline\\ 
     \theta_{T_2}=\theta_{T+1_1} & \alpha_{(x_2)_T}=\alpha_{(x_1)_{T+1}} & T-1 \\ 
     & \beta_{(x_2)_T}=\beta_{(x_1)_{T+1}} & T-1 \\\\\hline\\ 
     \sum F_x=0 & \sum_{i=1}^TF_{x_i}=0 & 1\\\\\hline\\ 
     \sum F_y=0 & \sum_{i=1}^{T+1} F_{y_i}+\sum_{i=1}^T w_{y_i}(x_{i+1}-x_i)=0 & 1\\\\\hline\\ 
     \sum F_z=0 & \sum_{i=1}^{T+1} F_{z_i}+\sum_{i=1}^T w_{z_i}(x_{i+1}-x_i)=0 & 1\\\\\hline\\ 
     \sum M_x=0 & \sum_{i=1}^TM_{x_i}=0 & 1\\\\\hline\\ 
     \sum M_y=0 & \sum_{i=1}^{T+1} M_{y_i}+ \sum_{i=1}^{T} x_{i+1}F_{y_{i+1}} + \sum_{i=1}^{T}\frac{w_{y_i}(x_{i+1}-x_i)(x_{i+1}+x_i)}{2}=0& 1\\\\\hline\\ 
     \hspace{10.5mm} \sum M_z=0 \hspace{10.5mm} & \hspace{10mm} \sum_{i=1}^{T+1} M_{z_i}+ \sum_{i=1}^{T} x_{i+1}F_{z_{i+1}} + \sum_{i=1}^{T}\frac{w_{z_i}(x_{i+1}-x_i)(x_{i+1}+x_i)}{2}=0 \hspace{10mm} & 1\\\\\hline\\  
     & \text{Número total de ecuaciones } & 4T+2AS+3AE+6AF\\\\\hline
     \end{array}
''')
st.markdown('''<div style="text-align: justify;">
     Dado que el número de ecuaciones que se pueden establecer es igual al número de incógnitas que se deben de calcular, se infiere 
     que, sin importar el tipo o la cantidad de apoyos y cargas presentes, o que las propiedades geométricas y mecánicas varien, 
     siempre será posible calcular todas las reacciones y desplazamientos a los que se encuentre sometido un eje de transmisión de 
     potencia, lo cual valida la metodología de cálculo general de ejes, desarrollada para el modelo de Euler y Bernoully.
</div>''', unsafe_allow_html = True)
st.markdown('#### Cálculo general de las reacciones y desplazamientos mediante elementos finitos (Timoshenko)')
# Calculo de ejes - Numerico
st.markdown('''<div style="text-align: justify;">
     Mediante el uso de matrices se pueden cálcular las reacciones y desplazamientos correspondientes a un eje 
     con propiedades geométricas y mecánicas no constantes, sometido a cualquier cantidad de fuerzas, momentos y apoyos. 
     El procedimiento de cálculo inicia con la formulación de la matriz de rigidez local para cada elemento del eje, para posteriormente 
     ensamblarlas y establecer la matriz de rigidez global, la cual junto con las matrices de cargas y deformaciones, permiten cálcular 
     todas las incognitas, siempre y cuando se hayan pre establecido las condiciones de frontera de manera apropiada, en cada una de las 
     matrices previamente mencionadas.  
</div>''', unsafe_allow_html = True)
st.markdown('#####')
col29, col30 = st.columns([2, 1], gap = 'large')
with col29:
     equation = r"""
     $$
     \large \begin{matrix} 
     \text{Matriz de } f \text{ y } m & \text{Matriz de rigidez local } k & \text{Matriz de } \delta \text{ y } \theta \\ \hline \\
     \begin{bmatrix} \hspace{0.85mm} F_{{1_X}} \hspace{0.85mm} \\ F_{{2_X}} \\ \vdots \end{bmatrix} & \frac{{AE}}{{L}}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} & \begin{bmatrix} \hspace{0.25mm} \delta _{{1_X}} \hspace{0.25mm} \\ \delta _{{2_X}} \\ \vdots \end{bmatrix} \\ \\
     \begin{bmatrix} M_{{1_X}} \\ M_{{2_X}} \\ \vdots \end{bmatrix} & \frac{{JG}}{{L}}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} & \begin{bmatrix} \theta _{{1_X}} \\ \theta _{{2_X}} \\ \vdots \end{bmatrix} \\ \\
     \begin{bmatrix} \hspace{1.6mm} F_1 \hspace{1.6mm} \\ M_1 \\ F_2 \\ M_2 \\ \vdots \end{bmatrix} & \frac{{EI}}{{L^3(1 + \varphi)}}\begin{bmatrix} 12 & 6L & -12 & 6L \\ 6L & (4 + \varphi)L^2 & -6L & (2 - \varphi)L^2 \\ -12 & -6L & 12 & -6L \\ 6L & (2 - \varphi)L^2 & -6L & (4 + \varphi)L^2 \end{bmatrix} & \begin{bmatrix} \hspace{1mm} \delta _1 \hspace{1mm} \\ \theta _1 \\ \delta _2 \\ \theta _2 \\ \vdots \end{bmatrix} \\
     \end{matrix}
     $$
     """
     st.markdown(equation, unsafe_allow_html = True)
with col30:
     st.markdown('''<div style="text-align: justify;">
          A diferencia de la teoría de Euler y Bernoulli, la teoría de Timoshenko toma en cuenta los efectos de las cargas cortantes 
          por medio del coeficiente 𝜑, el cual se cálcula con:  
     </div>''', unsafe_allow_html = True)
     st.latex(r'\varphi=\frac{12EI}{K_sAGL^2}')
     st.markdown('''<div style="text-align: justify;">
          En esta ecuacíon aparece un nuevo termino conocido como factor de area, el cual depende del area de la sección del eje de transmisión y se computa 
          mediante la siguiente expresión: 
     </div>''', unsafe_allow_html = True)
     st.latex(r'K_s=\frac{6(1+\nu)(1+m^2)^2}{(7+6\nu)(1+m^2)^2+(20+12\nu)m^2}')
     st.write('Donde:')
     st.latex(r'm = \frac{r}{R} \quad v = \text{Coeficiente de Poisson (0.3)}')
url4 = 'https://junior19a2000.github.io/Jupywidgets/lab?path=ShaftDemo.ipynb'
st.markdown(f'<iframe src={url4} height="760" width="100%"></iframe>', unsafe_allow_html = True)
# Analisis estatico de ejes
st.markdown('#### Análisis estático')
col31, col32 = st.columns([1, 1], gap = 'medium')
with col31:
     st.markdown('''<div style="text-align: justify;">
          El módulo de ejes tiene como objetivo calcular los resultados mas críticos en todo el dominio del eje, por lo que resulta 
          necesario, establecer un elemento en específico para cada punto de análisis, en el cual estén presentes dichos resultados. 
          A priori, teniendo en cuenta las ecuaciones para el cálculo de los esfuerzos, se infiere que tal elemento 
          se encontrara en el contorno de la sección que se analice, no obstante, analizar todos los elementos del contorno de la 
          sección para determinar cual es el más crítico, se traduce en un elevado costo computacional y tiempo; por lo que es 
          imprescindible definir con antelación cual será el elemento a analizar, lo cual no implica necesariamente 
          que se deba conocer su posición exacta. 
     </div>''', unsafe_allow_html = True)
with col32:
     st.image(img8.resize((600, 230)))
col33, col34 = st.columns([1, 2.3], gap = 'medium')
with col33:
     st.markdown('##')
     st.markdown('#####')
     st.image(img9.resize((400, 400)))
with col34:
     st.write('Los esfuerzos que se analizaran en dicho elemento son:')
     st.latex(r'\small \sigma_x=\frac{F_x}{A} \quad \sigma_y=\frac{M_yc}{I} \quad \sigma_z=\frac{M_zc}{I} \quad \tau_x=\frac{M_xc}{J} \quad \tau_y=\frac{F_yQ}{It} \quad \tau_z=\frac{F_zQ}{It}')
     st.write('Las propiedades geómetricas para un eje de transmisión hueco se calculan con:')
     st.latex(r'\small A=\pi (R^2-r^2) \quad J = \frac{\pi (R^4 - r^4)}{2} \quad I = \frac{\pi (R^4 - r^4)}{4} \quad Q=\frac{2(R^3 - r^3)\sin^3\alpha}{3} \quad t = 2(R - r)\sin\alpha')
     st.write('Particularmente, los esfuerzos flexionantes correspondientes a un elemento en el contorno de la sección se computan con:')
     st.latex(r'\small \sigma_y=\frac{4M_yR\cos\alpha}{\pi (R^4-r^4)} \quad \sigma_z=\frac{4M_zR\cos\beta}{\pi (R^4-r^4)} \quad \sigma_{yz}=\frac{4R(M_y\sin\beta + M_z\cos\beta)}{\pi (R^4-r^4)}')
     st.write('Asi mismo, los esfuerzos cortantes correspondientes a un elemento en el contorno de la sección se computan con:')
     st.latex(r'\small \tau_y=\frac{4F_y(R^2+Rr+r^2)\sin^2\beta}{3\pi (R^4-r^4)} \quad \tau_z=\frac{4F_z(R^2+Rr+r^2)\sin^2\alpha}{3\pi (R^4-r^4)} \quad \tau_{yz}=\frac{4(R^2+Rr+r^2)(F_y\sin^2\beta +F_z\cos^2\beta)}{3\pi (R^4-r^4)}')
     st.markdown('#####')
col35, col36 = st.columns([1, 1], gap = 'medium')
with col35:
     st.markdown('''<div style="text-align: justify;">
          Si bien, en el presente proyecto de investigación no se esta ignorando a los esfuerzos cortantes, esto no altera el 
          hecho de que no sean tan relevantes en comparación con los otros esfuerzos, por lo que para determinar la ubicación 
          del elemento a analizar, se hará mayor énfasis en los esfuerzos flectores.
          En consecuencia, el elemento a analizar sera aquel en el cual este presente el esfuerzo flector máximo: 
     </div>''', unsafe_allow_html = True)
     st.latex(r'\frac{d\sigma_{yz}}{d\beta}=0 \hspace{5mm} M_y\cos\beta-M_z\sin\beta = 0 \hspace{5mm} \beta=\arctan \frac{M_y}{M_z}')
     st.write('Finalmente, los esfuerzos que se analizaran en dicho elemento se establecen como:')
     st.latex(r'\sigma_{\text{flexionante}} = \sigma_{yz} \quad \tau_{\text{cortante}} = \tau_{yz} \quad \sigma_{\text{axial}} = \sigma_x \quad \tau_{\text{torsional}} = \tau_x')
     st.markdown('''<div style="text-align: justify;">
          Ahora bien, para determinar el valor del esfuerzo máximo al cual estará sometido el elemento seleccionado, es necesario tomar en 
          cuenta el sentido de los esfuerzos previamente establecidos de manera conjunta. Al respecto, se puede afirmar que, 
          siempre existirá un caso en el cual los esfuerzos normales y transversales tendrán la misma orientación, aunque no 
          necesariamente de manera simultánea.
     </div>''', unsafe_allow_html = True)
     st.latex(r'''
          \begin{array}{ccc}
          \sigma_{\text{n}}=\sigma_{\text{flexionante}}+\sigma_{\text{axial}} & \sigma_{\text{n}}=\sigma_{\text{flexionante}}\pm\sigma_{\text{axial}}\\
          \tau_{\text{t}}=\tau_{\text{torsional}}\pm\tau_{\text{cortante}} & \tau_{\text{t}}=\tau_{\text{torsional}}+\tau_{\text{cortante}}\\
          \end{array}
     ''')
     st.markdown('''<div style="text-align: justify;">
          Considerando un enfoque conservador, los esfuerzos normales y transversales combinados se calcularán con las siguientes ecuaciones:.
     </div>''', unsafe_allow_html = True)
     st.latex(r'''\sigma_{\text{n}}=\sigma_{\text{flexionante}}+\sigma_{\text{axial}} \quad \tau_{\text{t}}=\tau_{\text{torsional}}+\tau_{\text{cortante}}''')
     st.markdown('''<div style="text-align: justify;">
          Dado que se está incurriendo en un error voluntario, se ha comparado el error de considerar al esfuerzo cortante con el 
          error de ignorarlo, en el cálculo de los esfuerzos combinados bajo el criterio de Von Mises, al ser dicho criterio el más 
          usado para el diseño de ejes. De las gráficas de la derecha, se aprecia que, en promedio, para ambos casos previamente 
          descritos, el error es muy similar, es decir, que a pesar de estar considerando a los esfuerzos cortantes en el cálculo 
          del esfuerzo de Von Mises, esto no ha significado un incremento considerable en el error en el que se incurría al 
          ignorarlos para dicho cálculo. Por otra parte, se advierte que cuando la relación entre el esfuerzo torsional y el 
          esfuerzo cortante es mayor a 20 (lo cual sucede casi siempre), el error en el cálculo del esfuerzo de Von Mises 
          disminuye por debajo del 10% a medida que dicha relación se incrementa.
     </div>''', unsafe_allow_html = True)
     st.markdown('#####')
     st.markdown('''<div style="text-align: justify;">
          En línea con lo anterior y considerando 
          a los factores de concentración de esfuerzos, el cálculo del esfuerzo máximo 
          combinado (esfuerzos normales y transversales), bajo tres tipos de criterios de falla, se realizará mediante las siguientes expresiones:
     </div>''', unsafe_allow_html = True)
     st.latex(r'\sigma_{k}=K_{a}\sigma_{\text{axial}}+K_{f}\sigma_{\text{flexionante}}\quad\tau_{k}=K_{t}\tau_{\text{torsional}}+\tau_{\text{cortante}}')
     st.latex(r'\text{Criterio de falla según Von Mises}=\sqrt{\sigma_{\text{k}}^{2}+3\tau_{\text{k}}^{2}}')
     st.latex(r'\text{Criterio de falla según Tresca}=\sqrt{\sigma_{\text{k}}^{2}+4\tau_{\text{k}}^{2}}')
     st.latex(r'\text{Criterio de falla según Rankine}=\frac{1}{2}(\sigma_{\text{k}}+\sqrt{\sigma_{\text{k}}^{2}+4\tau_{\text{k}}^{2}})')
with col36:
     st.image(img10.resize((600, 300)))
     st.markdown('#####')
     st.image(img11.resize((600, 230)))
     st.markdown('#####')
     url1 = 'https://junior19.starboard.host/v1/embed/0.15.3/cbljq1i23akg00a8j9b0/nCzetdj/'
     st.markdown(f'<iframe src={url1} height="655" width="100%"></iframe>', unsafe_allow_html = True)
# Analisis dinamico de ejes
st.markdown('#### Análisis dinámico')
col37, col38 = st.columns([1, 1], gap = 'medium')
with col37:
     st.markdown('''<div style="text-align: justify;">
          En los ejes de transmisión de potencia, algunos de los esfuerzos que actúan sobre este fluctúan en relación al tiempo, 
          debido al comportamiento de las cargas que los generan. Si se analiza al elemento seleccionado, en su recorrido alrededor 
          del contorno circular del eje, se entiende que, 
          para el caso de los esfuerzos axiales y torsionales, estos presentan un comportamiento constante, es decir que, tanto 
          su magnitud como sentido no se alteran a medida que el eje da un giro entero. En contraste, 
          para el caso de los esfuerzos flexionantes y cortantes, estos presentan un comportamiento fluctuante, dado que tanto 
          su magnitud como sentido se alteran a medida que el eje de un giro entero.
     </div>''', unsafe_allow_html = True)
     st.markdown('#####')
     st.markdown('''<div style="text-align: justify;">
          Considerando lo previamente expuesto, 
          se establecen las siguientes ecuaciones en relación a los componentes medio y alternante de cada uno de los esfuerzos 
          presentes en el eje:
     </div>''', unsafe_allow_html = True)
     equation = r"""
     $$
     \begin{array}{|c|c|c|} \hline \\
     \text{Esfuerzo} & \text{Medio} & \text{Alternante}  \\ \\\hline\\
     \text{Axial} & \sigma_{\text{axial}} & 0  \\ \\\hline\\
     \text{Torsional} & \tau_{\text{torsional}} & 0  \\ \\\hline\\
     \text{Flexionante} & 0 & \sigma_{\text{flexionante}}  \\ \\\hline\\
     \text{Cortante} & \hspace{3.5mm} \frac{{\tau_{\text{cortante máximo}} + \tau_{\text{cortante mínimo}}}}{2} \hspace{3mm} & \hspace{3mm} \left| \frac{{\tau_{\text{cortante máximo}} - \tau_{\text{cortante mínimo}}}}{2} \right| \hspace{3.5mm} \\ \\\hline
     \end{array}
     $$
     """
     st.markdown(equation, unsafe_allow_html = True)
     st.markdown('''<div style="text-align: justify;">
          A diferencia de los esfuerzos flexionantes, los esfuerzos cortantes no presentan un comportamiento sinusoidal completamente 
          invertido, lo cual conlleva a que para este caso, se deban cálcular los valores máximos y mínimos para dicha función:
     </div>''', unsafe_allow_html = True)
     st.latex(r'\frac{{d{\tau _{yz}}}}{{d\beta }} = 0 \quad 2\sin \beta \cos \beta ({F_y} - {F_z}) \quad \beta = \frac{{k\pi }}{2} \rightarrow k = \mathbb{N}')
     st.markdown('''<div style="text-align: justify;">
          De conformidad con el resultado anterior, se obtiene que los valores máximo y mínimo de la función del esfuerzo cortante son:
     </div>''', unsafe_allow_html = True)
     st.latex(r'{\tau _{{\text{cortante m\'a ximo}}}} = \frac{{4({R^2} + Rr + {r^2})\max ([{F_y},{F_z}])}}{{3\pi ({R^4} - {r^4})}}')
     st.latex(r'{\tau _{{\text{cortante m\'a ximo}}}} = \frac{{4({R^2} + Rr + {r^2})\min ([{F_y},{F_z}])}}{{3\pi ({R^4} - {r^4})}}')
     st.markdown('''<div style="text-align: justify;">
          En consecuencia, los componentes de los esfuerzos medio y alternante de los esfuerzos cortantes se establecen como:
     </div>''', unsafe_allow_html = True)
     st.latex(r'{\tau _{{\text{medio cortante}}}} = \frac{{2({R^2} + Rr + {r^2})({F_y} + {F_z})}}{{3\pi ({R^4} - {r^4})}}')
     st.latex(r'{\tau _{{\text{alternante cortante}}}} = \frac{{2({R^2} + Rr + {r^2})\left| {{F_y} - {F_z}} \right|}}{{3\pi ({R^4} - {r^4})}}')
     st.markdown('''<div style="text-align: justify;">
          Por lo expuesto, los esfuerzos medio y alternante para cada uno de los esfuerzos analizados se definen mediante las 
          siguientes expresiones:
     </div>''', unsafe_allow_html = True)
     equation = r"""
     $$
     \begin{array}{|c|c|c|} \hline \\
     \text{Esfuerzo} & \text{Medio} & \text{Alternante} \\ \\\hline\\
     \text{Axial} & \sigma _{{m_a}} = \sigma _{{\text{axial}}} & \sigma _{{a_a}} = 0 \\ \\\hline\\
     \text{Torsional} & \tau _{{m_t}} = \tau _{{\text{torsional}}} & \tau _{{a_t}} = 0 \\ \\\hline\\
     \text{Flexionante} & \sigma _{{m_f}} = 0 & \sigma _{{a_f}} = \sigma _{{\text{flexionante}}} \\ \\\hline\\
     \hspace{4.5mm} \text{Cortante} \hspace{4mm} & \hspace{3.5mm} \tau _{{m_c}} = \tau _{{\text{medio cortante}}} \hspace{3.5mm} & \hspace{3.5mm} \tau _{{a_c}} = \tau _{{\text{alternante cortante}}} \hspace{4mm} \\ \\\hline
     \end{array}
     $$
     """
     st.markdown(equation, unsafe_allow_html = True)
with col38:
     url2 = 'https://junior19.starboard.host/v1/embed/0.15.3/cbljq1i23akg00a8j9b0/n4za9UC/'
     st.markdown(f'<iframe src={url2} height="925" width="100%"></iframe>', unsafe_allow_html = True)
     st.markdown('''<div style="text-align: justify;">
          Con los valores de los esfuerzos medios y alternante ya calculados para cada uno de los esfuerzos presentes en el eje de 
          manera individual, se pueden calcular los esfuerzos medio y alternante de los esfuerzos combinados bajo los criterios de 
          falla utilizados en el análisis estático. Considerando a los factores de concentración de los esfuerzos dinámicos, dichos esfuerzos son:
     </div>''', unsafe_allow_html = True)
     equation = r"""
     $$
     \text{Von Mises}\left\{ \begin{array}{c}
     \sigma_a = \left[ {{{({K_{f_f}}\sigma_{a_f}})}^2} + 3\tau_{a_c}^2 \right]^{\frac{1}{2}} \\
     \sigma_m = \left[ {{{({K_{f_a}}\sigma_{m_a}})}^2} + 3{{({K_{f_t}}\tau_{m_t}} + \tau_{m_c})}^2 \right]^{\frac{1}{2}}
     \end{array} \right.
     $$
     """
     st.markdown(equation, unsafe_allow_html=True)
     equation = r"""
     $$
     \text{Tresca}\left\{ \begin{array}{c}
     \sigma_a = \left[ {{{({K_{f_f}}\sigma_{a_f}})}^2} + 4\tau_{a_c}^2 \right]^{\frac{1}{2}} \\
     \sigma_m = \left[ {{{({K_{f_a}}\sigma_{m_a}})}^2} + 4{{({K_{f_t}}\tau_{m_t}} + \tau_{m_c})}^2 \right]^{\frac{1}{2}}
     \end{array} \right.
     $$
     """
     st.markdown(equation, unsafe_allow_html=True)
     equation = r"""
     $$
     \text{Rankine}\left\{ \begin{matrix}
     \sigma_a = 0.5\left\{ ({K_{f_f}}\sigma_{a_f}) + \left[ {{{({K_{f_f}}\sigma_{a_f}})}^2} + 4\tau_{a_c}^2 \right]^{\frac{1}{2}} \right\}  \\
     \sigma_m = 0.5\left\{ ({K_{f_a}}\sigma_{m_a}) + \left[ {{{({K_{f_a}}\sigma_{m_a}})}^2} + 4{{({K_{f_t}}\tau_{m_t}} + \tau_{m_c})}^2 \right]^{\frac{1}{2}} \right\}
     \end{matrix} \right.
     $$
     """
     st.markdown(equation, unsafe_allow_html=True)
     st.markdown('''<div style="text-align: justify;">
          Finalmente, los esfuerzos dinámicos se calculan en base al criterio de falla estático que se considere conveniente y 
          bajo los siguientes criterios de falla dinámicos:
     </div>''', unsafe_allow_html = True)
     st.latex(r'''
     {\text{Soderberg}}:\quad \frac{{{\sigma _a}}}{{{{\text{S}}_e}}}{\text{ + }}\frac{{{\sigma _m}}}{{{{\text{S}}_y}}}{\text{ = }}\frac{{\text{1}}}{n}
     ''')
     st.latex(r'''
     {\text{Goodman}}:\quad \frac{{{\sigma _a}}}{{{{\text{S}}_e}}}{\text{ + }}\frac{{{\sigma _m}}}{{{{\text{S}}_u}}}{\text{ = }}\frac{{\text{1}}}{n}
     ''')
     st.latex(r'''
     {\text{ASME}}:\quad {\left( {\frac{{{\sigma _a}}}{{{{\text{S}}_e}}}} \right)^2}{\text{ + }}{\left( {\frac{{{\sigma _m}}}{{{{\text{S}}_y}}}} \right)^2}{\text{ = }}\frac{{\text{1}}}{{{n^{\text{2}}}}}
     ''')
# Analisis de rigidez de ejes
st.markdown('#### Análisis de rigidez')
col39, col40 = st.columns([1, 1], gap = 'medium')
with col39:
     st.markdown('''<div style="text-align: justify;">
          Las deformaciones lineales y angulares resultantes, se calculan haciendo uso de las deflexiones y pendientes ya 
          calculadas, por medio de las siguientes ecuaciones:
     </div>''', unsafe_allow_html = True)
with col40:
     st.latex(r'\delta_R = \sqrt{\delta _x^2 + \delta _y^2 + \delta _z^2} \quad\quad \theta_R = \sqrt {\theta _x^2 + \theta _y^2 + \theta _z^2}')
# Analisis vibracional de ejes
st.markdown('#### Análisis vibracional')
col41, col42 = st.columns([1, 1], gap = 'medium')
with col41:
     st.markdown('''<div style="text-align: justify;">
          El cálculo de los límites del rango de operación en el cual estará situada la velocidad critica fundamental del eje de transmisión 
          de potencia, se efectúa siguiendo las ecuaciones de Rayleigh y Ritz:
     </div>''', unsafe_allow_html = True)
     st.latex(r'''
     \begin{array}{|c|c|}
     \hline \\
     \hspace{1.31cm} \text{Límite inferior} \hspace{1.31cm} & \hspace{1.31cm} \text{Límite superior} \hspace{1.31cm} \\ \\
     \hline \\
     \text{RPM} = \frac{30}{\pi}\sqrt{\frac{g}{\max(\delta_R)}} & \text{RPM} = \frac{30}{\pi}\sqrt{g\frac{\sum\limits_{i = 1}^T {m_i y_i}}{\sum\limits_{i = 1}^T {m_i y_i^2}}} \\ \\
     \hline
     \end{array}
     ''')
     col43, col44 = st.columns([1, 1])
     with col43:
          number_input_5 = st.number_input('Número de elementos en cada tramo:', 1, 100, 1, 1, label_visibility = 'visible')
     with col44:
          selectbox_1 = st.selectbox('Tipo de eje a analizar:', ('Escalonado', 'Hueco'), label_visibility = 'visible')
     fig3, df = f1_rpm(number_input_5, selectbox_1)
     st.pyplot(fig3)
     st.dataframe(df, use_container_width = True, height = 150)
with col42:
     st.markdown('''<div style="text-align: justify;">
          Para el cálculo del límite superior, resulta necesario primeramente dividir al eje en sectores, luego calcular la masa de cada uno 
          de ellos y finalmente determinar la deflexión en el punto medio de cada uno de estos sectores. Una vez calculados estos valores, 
          recién se puede hallar el valor deseado, sin embargo, la precisión de este resultado depende del número de divisiones del eje, lo 
          cual significa que, a mayor número de divisiones, mayor precisión en el resultado, sin embargo, esto a su vez implica mayores cálculos 
          debido a los pasos comentados previamente. Teniendo en cuenta lo anterior, se ha visto por conveniente modificar la ecuación en cuestión, 
          de la siguiente manera:
     </div>''', unsafe_allow_html = True)
     st.latex(r'''
     \text{Límite superior:}\quad \text{RPM} = \frac{30}{\pi}\sqrt{g\frac{\sum\limits_{i = 1}^T {\sum\limits_{j = 1}^n {m_{i_j} y_{i_j}} }}{\sum\limits_{i = 1}^T {\sum\limits_{j = 1}^n {m_{i_j} y_{i_j}^2} } }}
     ''')
     st.markdown('''<div style="text-align: justify;">
          Llevando al límite el número de divisiones del eje y reemplazando el valor de la masa correspondiente a cada una de estas divisiones:
     </div>''', unsafe_allow_html = True)
     st.latex(r'''
     \sum\limits_{j = 1}^n {m_j y_j} = \lim_{{n \to \infty}} \sum\limits_{j = 1}^n \Delta m_j \cdot y_j = \rho A \lim_{{n \to \infty}} \sum\limits_{j = 1}^n \Delta x_j \cdot y_j = \rho_T A_T \int y_T dx
     ''')
     st.latex(r'''
     \sum\limits_{j = 1}^n {m_j y_j^2} = \lim_{{n \to \infty}} \sum\limits_{j = 1}^n \Delta m_j \cdot y_j^2 = \rho A \lim_{{n \to \infty}} \sum\limits_{j = 1}^n \Delta x_j \cdot y_j^2 = \rho_T A_T \int y_T^2 dx
     ''')
     st.markdown('''<div style="text-align: justify;">
          Finalmente, reemplazando en la ecuación inicial, el limite superior se computa con:
     </div>''', unsafe_allow_html = True)
     st.latex(r'''
     \text{Límite superior:}\quad \text{RPM} = \frac{30}{\pi}\sqrt{g\frac{\sum\limits_{i = 1}^T \rho_i A_i \int y_i dx}{\sum\limits_{i = 1}^T \rho_i A_i \int y_i^2 dx}}
     ''')
     st.markdown('''<div style="text-align: justify;">
          Esta ecuación ofrece un resultado más preciso, dado que el número de divisiones se ha elevado al infinito, lo cual ha 
          permitido convertir las sumatorias en integrales, y que, por otra parte, resulta conveniente en este caso, toda vez que las deflexiones 
          en el eje han sido calculadas mediante funciones analíticas y numéricas que se pueden integrar de manera rápida y precisa.
     </div>''', unsafe_allow_html = True)
# Elementos finitos
st.subheader('Elementos bidimensionales')
col45, col46 = st.columns([1, 1], gap = 'medium')
with col45:
     st.markdown('''<div style="text-align: justify;">
          Se utilzan elementos triangulares de deformación constante (CST), donde cada uno de estos estará definido geométricamente por tres pares 
          de coordenadas, a partir de los cuales se pueden establecer las siguientes expresiones:
     </div>''', unsafe_allow_html = True)
     st.latex(r'\begin{align*} \beta_i=y_j-y_m \hspace{0.6cm}& \beta_j=y_m-y_i \hspace{0.3cm}& \beta_m=y_i-y_j\\ \gamma_i=x_m-x_j \hspace{0.6cm}& \gamma_j=x_i-x_m \hspace{0.3cm}& \gamma_m=x_j-x_i\\ \end{align*}')
     st.markdown('''<div style="text-align: justify;">
          Ahora bien, considerando estas expresiones junto con el área, módulo de elasticidad y el coeficiente de Poisson correspondientes a 
          cada uno de los elementos, se describen las siguientes matrices:
     </div>''', unsafe_allow_html = True)
     st.latex(r'[B]=\frac{1}{2A}\begin{bmatrix} \beta_i & 0 & \beta_j & 0 & \beta_m & 0 \\ 0 & \gamma_i & 0 & \gamma_j & 0 & \gamma_m \\ \gamma_i & \beta_i & \gamma_j & \beta_j & \gamma_m & \beta_m \\ \end{bmatrix} \quad [D] = \frac{E}{1-v^2}\begin{bmatrix} 1 & v & 0 \\ v & 1 & 0 \\ 0 & 0 & \frac{1-v}{2} \\ \end{bmatrix}')
     st.markdown('''<div style="text-align: justify;">
          A partir de estas y considerando el espesor de cada elemento, se puede formular la matriz de rigidez respectiva mediante la siguiente ecuación:
     </div>''', unsafe_allow_html = True)
     st.latex(r'[k]=tA[B]^T[D][B]')
     st.markdown('''<div style="text-align: justify;">
          Con las matrices de rigidez individuales se plantea la matriz de rigidez global, la cual, junto con las matrices de fuerzas y desplazamientos, 
          se redimensionan en base a las condiciones de frontera, para posteriormente resolver el sistema general y determinar asi, las reacciones y desplazamientos 
          en cada nodo de la malla, lo cual asu vez, permite calcular los esfueroz en cada elemento de la malla, mediante las siguientes expresiones:
     </div>''', unsafe_allow_html = True)
     st.latex(r'[F]=[K][d] → [\sigma_x, \sigma_y, \tau_{xy}] = [D][B][d]')
with col46:
     url3 = 'https://junior19.starboard.host/v1/embed/0.15.3/cbljq1i23akg00a8j9b0/n529MY4/'
     st.markdown(f'<iframe src={url3} height="655" width="100%"></iframe>', unsafe_allow_html = True)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Sobre el autor
with st.sidebar:
     st.markdown('# Sobre el autor ...')
     st.markdown('''<div style="text-align: justify;">
          Cuando elegí la carrera de Ingeniería Mecánica no estaba seguro si en verdad era lo que queria estudiar,\
          pero a medida que avanzaba me di cuenta que me encontraba en el lugar correcto, dado que me considero una persona a la cual le\
          gusta aprender de todo, y esta carrera es tan amplia que me permite involucrarme en distintas ramas tales\
          como el diseño mecánico, energías renovables y automatización (mis preferidas, obviamente hay mas). Por otra parte, otra de mis pasiones \
          es la programación, sobre todo el desarrollo de aplicaciones web, lo cual cabe decir, me ha ayudado bastante, tanto en la\
          universidad como en el mundo laboral. Este proyecto es un claro ejemplo de lo que menciono, ya que para su desarrollo han sido\
          necesarios mis conocimientos en ingeniería mecánica y programación, y del cual me siento muy orgulloso, ya que en comparación con otros\
          proyectos similares, humildemente considero que el mío es mucho mejor.
     </div>''', unsafe_allow_html = True)
     st.markdown('#')
     st.image(img12, caption = 'Junior Joel Aguilar Hancco')
