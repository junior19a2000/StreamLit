# streamlit hello --server.enableCORS false --server.enableXsrfProtection false

import base64
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import interpolate as numint
from st_cytoscape import cytoscape
from PIL import Image

st.set_page_config(page_title = "Tesis", page_icon = "🦅", layout = "wide", initial_sidebar_state = "collapsed")

st.markdown("<h1 style='text-align: center; color: black;'>Power System Transmission Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>Proyecto de tesis para obtener el grado de Ingeniero Mecánico</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>Universidad Nacional de San Agustin</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>Arequipa - 2023</h1>", unsafe_allow_html=True)
st.divider()

file_1   = open(r'Imagenes/Logo.gif', "rb")
content1 = file_1.read()
dataurl1 = base64.b64encode(content1).decode("utf-8")
file_1.close()
file_2   = open(r'Imagenes/tooht.gif', "rb")
content2 = file_2.read()
dataurl2 = base64.b64encode(content2).decode("utf-8")

col1, col2 = st.columns([1.5, 1], gap = 'large')
col1.header('Resumen')
tex1 = '''El presente proyecto de investigación se realizo con la finalidad de optimizar el proceso de diseño de un
          sistema de transmisión de potencia como el que se muestra en la imagen. Para ello se analizaron los
          componentes generales de dichos sistemas, tales como las correas, cadenas, engranajes, ejes y chavetas,
          en base a las distintas metodologias, criterios y normativas que existen en la actualidad.  \nUna vez establecido 
          el proceso de calculo para cada uno de ellos, se desarrollo una interfaz gráfica para que el usuario pueda
          mejorar su diseño mediante la variación de los parametros iniciales del sistema.  \nComo resultado final se
          creó Power System Transmission Calculator, una aplicación informática que permite cálcular los componentes previamente
          mencionados, de manera rapida, precisa y optima, cumpliendo asi con el proposito establecido en el proyecto de investigación.'''
# col1.write(tex1)
col1.markdown('''<div style="text-align: justify;">{}</div>'''.format(tex1), unsafe_allow_html = True)
col2.markdown(f'<img src = "data:image/gif;base64,{dataurl1}" width = "450">', unsafe_allow_html = True)

st.header('Marco Teórico')

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

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Correas planas', 'Correas trapezoidales', 'Cadenas', 'Engranajes', 'Ejes de transmisión', 'Chavetas y rodamientos', 'Elementos finitos'])
with tab1:
     st.subheader('Correas planas')
     col7, col8 = st.columns([1,3])
     with col7:
          st.image(Image.open(r'Imagenes/forbo.png').resize((600, 800)))
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
with tab2:
     st.subheader('Correas trapezoidales')
     col9, col10 = st.columns([1,3])
     with col9:
          st.image(Image.open(r'Imagenes/optibelt.png').resize((600, 800)))
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
with tab3:
     st.subheader('Cadenas')
     col11, col12 = st.columns([1,3])
     with col11:
          st.image(Image.open(r'Imagenes/renold.png').resize((600, 800)))
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
with tab4:
     st.subheader('Engranajes')
     col13, col14 = st.columns([1,3])
     with col13:
          st.image(Image.open(r'Imagenes/agma.png').resize((600, 800)))
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
          st.latex(r'\begin{array}{ccc} & \text{Falla por picadura} & \text{Falla por flexión} \\[6pt] \text{Esfuerzo} & \sigma_h = Z_e\sqrt{\frac{F_t K_o K_v K_s K_h Z_r}{d_{w1}bZ_i}} & \sigma_f = \frac{F_t K_o K_v K_s K_h K_b}{bm_t Y_j} \\[6pt] \text{Esfuerzo admisible} & \sigma_{ha} = \frac{\sigma_{hp}Z_n Z_w}{S_h Y_\theta Y_z} & \sigma_{fa} = \frac{\sigma_{fp}Y_n}{S_f Y_\theta Y_z} \\[6pt] \text{Potencia} & P_{az} = \frac{\pi \omega_1 bZ_i}{6.10^7 K_o K_v K_s K_h Z_r}\left(\frac{d_{w1} \sigma_{hp} Z_n Z_w}{Z_e S_h Y_\theta Y_z}\right)^2 & P_{ay} = \frac{\pi \omega_1 d_{w1} b m_t Y_j \sigma_{fp} Y_n}{6.10^7 K_o K_v K_s K_h K_b S_f Y_\theta Y_z} \end{array}')
with tab5:
     col15, col16 = st.columns([1, 3])
     with col15:
          st.subheader('Ejes de transmisión')
          st.image(Image.open(r'Imagenes/jack.png').resize((600, 800)))
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
with tab6:
     st.subheader('Chavetas')
     col17, col18 = st.columns([1,3])
     with col17:
          st.image(Image.open(r'Imagenes/bandari.png').resize((600, 800)))
     with col18:
          st.write('''
          Se analizan bajo la metodología desarrollada en el libro "Diseño de elementos de máquinas" de Bhandari y unicamente se 
          computan las chavetas del tipo cuadradas. Por otra parte, los rodamientos se pueden diseñar por medio de una 
          herramienta gratuita proporcionada por la empresa [SKF](https://www.skfbearingselect.com/#/bearing-selection-start):
          ''')
with tab7:
     st.subheader('Elementos finitos')
     col19, col20 = st.columns([1,3])
     with col19:
          st.image(Image.open(r'Imagenes/logan.png').resize((600, 800)))
     with col20:
          st.write('''
          Se utilzan los elementos triangulares de deformación constante (CST) para el analisis de componentes 
          bidimensionales sometidos a esfuerzos y deformaciones planas. Para ello, se establecen las siguientes 
          ecuaciones y matrices que permiten calcular los esfuerzos y deformaciones de cada elemento:
          ''')
          # col21, col22 = st.columns([2, 1], gap = 'large')
          # with col21:
          st.latex(r'\begin{align*} \beta_i=y_j-y_m \hspace{0.6cm}& \beta_j=y_m-y_i \hspace{0.3cm}& \beta_m=y_i-y_j\\ \gamma_i=x_m-x_j \hspace{0.6cm}& \gamma_j=x_i-x_m \hspace{0.3cm}& \gamma_m=x_j-x_i\\ \end{align*}')
          st.latex(r'[B]=\frac{1}{2A}\begin{bmatrix} \beta_i & 0 & \beta_j & 0 & \beta_m & 0 \\ 0 & \gamma_i & 0 & \gamma_j & 0 & \gamma_m \\ \gamma_i & \beta_i & \gamma_j & \beta_j & \gamma_m & \beta_m \\ \end{bmatrix} [D] = \frac{E}{1-v^2}\begin{bmatrix} 1 & v & 0 \\ v & 1 & 0 \\ 0 & 0 & \frac{1-v}{2} \\ \end{bmatrix}')
          st.latex(r'[k]=tA[B]^T[D][B]')
          st.latex(r'[F]=[K][d] → [\sigma_x, \sigma_y, \tau_{xy}] = [D][B][d]')
          # with col22:
          #      st.markdown('#') 
          #      st.markdown(f'<img src = "data:image/gif;base64,{dataurl2}" width = "240">', unsafe_allow_html = True)

st.header('Marco Metodológico')
st.subheader('Correas planas, correas trapezoidales, cadenas y engranajes')
# plt.close('all')
x = np.array([5, 15, 25, 35])
y = np.array([20, 30, 50, 70, 100, 120, 150, 200, 300])
z = np.array([[0.1100, 0.1110, 0.1120, 0.1160],
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
tex2 = '''En el proceso de cálculo de estos componentes resulta 
          indispensable hacer uso de parámetros numéricos exclusivos de cada uno de estos, los cuales por lo general, se representan y determinan 
          mediante el uso de gráficos y tablas. En este punto, resulta pertinente señalar que, mediante el procesamiento de imágenes se han extraido los datos de las gráficas 
          correspondientes a cada uno de estos parametros numéricos, para poder representarlos mediante tablas y, posteriormente, mediante 
          interpolaciones, poder calcular el parámetro numérico deseado de manera rapida y precisa. Para esto último, se hacen uso de las siguientes ecuaciones
        '''
col3, col4 = st.columns([1, 1])
with col3:
     with st.form('form1'):
        st.markdown('''<div style="text-align: justify;">{}</div>'''.format(tex2), unsafe_allow_html = True)
        st.markdown('#####')
        st.latex(r'{x_{{n_{a,b}}}} = \frac{{{x_{{n_{b,a}}}} - {x_{{1_{b,a}}}}}}{{{x_{{2_{b,a}}}} - {x_{{1_{b,a}}}}}}\left( {{x_{{2_{a,b}}}} - {x_{{1_{a,b}}}}} \right) + {x_{{1_{a,b}}}}')
        st.latex(r'{y_{{n_{a,b}}}} = \frac{{{y_{{n_{b,a}}}} - {y_{{1_{b,a}}}}}}{{{y_{{2_{b,a}}}} - {y_{{1_{b,a}}}}}}\left( {{y_{{2_{a,b}}}} - {y_{{1_{a,b}}}}} \right) + {y_{{1_{a,b}}}}')
        st.markdown('#####')
        st.write('Con los parametros numéricos ya tabulados, el cálculo se efectúa como sigue:')
        x1 = st.slider('Ángulo', 5, 35, 5, 1)
        y1 = st.slider('Dientes', 20, 300, 20, 1)
        col5, col6 = st.columns([1.55, 1])
        with col5:
             submitted1 = st.form_submit_button("Calcular factor geométrico")
        with col6:
             st.write('El factor geometrico es: ' + str(np.round(fz(x1, y1)[0], 5)))
        # if submitted1:
        #      st.write("x1", x1, "y1", y1)
fig1, axe1 = plt.subplots()
img1 = mpimg.imread(f'Imagenes/carta1.png')
axe1.imshow(img1)
axe1.plot([fx(x1), fx(x1)], [650, 20], 'red', linestyle = 'dashed')
axe1.plot([50, 550], [fy(fz(x1, y1)), fy(fz(x1, y1))], 'red', linestyle = 'dashed')
axe1.scatter(fx(x1), fy(fz(x1, y1)), 25, 'red')
axe1.axis('off')
col4.pyplot(fig1)

st.subheader('Ejes de transmisión')
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
with st.container():
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
# st.components.v1.html(f'<iframe src={i}> </iframe>')
# url1 = 'https://junior19a2000.github.io/Jupywidgets/lab?path=Numesym.ipynb'
# url1 = 'https://junior19.starboard.host/v1/embed/0.15.3/cbljq1i23akg00a8j9b0/n529MY4/'
# st.markdown(f'<iframe src={url1} height="760" width="100%"></iframe>', unsafe_allow_html = True)


# st.divider()
# col1, col2 = st.columns([3, 1])
# col1.header('Sobre mí ...')
desc = 'Cuando elegí la carrera de Ingeniería Mecánica no estaba seguro si en verdad era lo que queria estudiar,\
        pero a medida que avanzaba me di cuenta que me encontraba en el lugar correcto, dado que me considero una persona a la cual le\
        gusta aprender de todo, y esta carrera es tan amplia que me permite involucrarme en distintas ramas tales\
        como el diseño mecánico, energías renovables y automatización (mis preferidas, obviamente hay mas). Por otra parte, otra de mis pasiones \
        es la programación, sobre todo el desarrollo de aplicaciones web, lo cual cabe decir, me ha ayudado bastante, tanto en la\
        universidad como en el mundo laboral. Este proyecto es un claro ejemplo de lo que menciono, ya que para su desarrollo han sido\
        necesarios mis conocimientos en ingeniería mecánica y programación, y del cual me siento muy orgulloso, ya que en comparación con otros\
        proyectos similares, humildemente considero que el mío es mucho mejor.'
with st.sidebar:
     st.markdown('# Sobre el autor ...')
     st.markdown('''<div style="text-align: justify;">{}</div>'''.format(desc), unsafe_allow_html = True)
     st.markdown('#')
     st.image(Image.open(r'Imagenes/FotografiaJR.png'), caption = 'Junior Joel Aguilar Hancco')
