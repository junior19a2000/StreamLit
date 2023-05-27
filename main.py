# streamlit hello --server.enableCORS false --server.enableXsrfProtection false

import base64
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from scipy import interpolate as numint

st.set_page_config(page_title = "Tesis", page_icon = "🦅", layout = "wide")

st.markdown("<h1 style='text-align: center; color: black;'>Power System Transmission Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>Proyecto de tesis para obtener el grado de Ingeniero Mecánico</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>Universidad Nacional de San Agustin</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: black;'>Arequipa - 2023</h1>", unsafe_allow_html=True)
st.divider()

file_    = open(r'Imagenes/Logo.gif', "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
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
col1.write(tex1)
col2.markdown(f'<img src = "data:image/gif;base64,{data_url}" width = "450">', unsafe_allow_html = True)

st.header('Marco Teórico')
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Correas planas', 'Correas trapezoidales', 'Cadenas', 'Engranajes', 'Ejes de transmisión', 'Chavetas'])
with tab1:
     st.subheader('Correas planas')
     col7, col8 = st.columns([1,3])
     with col7:
          st.image(Image.open(r'Imagenes/forbo.png').resize((600, 800)))
     with col8:
          st.write('''
          Se analizan bajo la metodología desarrollada por la empresa Forbo, la cual, mediante datos de entrada 
          conocidos como la potencia y revoluciones del motor, los diámetros de las poleas y la distancia entre 
          las mismas, permite calcular las dimensiones del tipo de correa elegida junto con las fuerzas que se 
          transmitirán al eje de transmisión de potencia.
          ''')
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
     st.subheader('Ejes de transmisión')
     col15, col16 = st.columns([1,3])
     with col15:
          st.image(Image.open(r'Imagenes/logan.png').resize((600, 800)))
     with col16:
          st.write('''
          Se analizan bajo la metodología desarrollada por la empresa Forbo, la cual, mediante datos de entrada 
          conocidos como la potencia y revoluciones del motor, los diámetros de las poleas y la distancia entre 
          las mismas, permite calcular las dimensiones del tipo de correa elegida junto con las fuerzas que se 
          transmitirán al eje de transmisión de potencia.
          ''')
with tab6:
     st.subheader('Chavetas')
     col17, col18 = st.columns([1,3])
     with col17:
          st.image(Image.open(r'Imagenes/bandari.png').resize((600, 800)))
     with col18:
          st.write('''
          Se analizan bajo la metodología desarrollada por la empresa Forbo, la cual, mediante datos de entrada 
          conocidos como la potencia y revoluciones del motor, los diámetros de las poleas y la distancia entre 
          las mismas, permite calcular las dimensiones del tipo de correa elegida junto con las fuerzas que se 
          transmitirán al eje de transmisión de potencia.
          ''')

st.header('Marco Metodológico')
st.subheader('Correas planas, Correas trapezoidales, Cadenas y Engranajes')
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
tex2 = '''El calculo de estos componentes se efectúa segun la metodólogía de cálculo establecida por cada fabricante y normativa, 
          en este caso: Forbo, Optibelt, Renold, AGMA, respectivamente. Por otra parte, en el proceso de cálculo de estos componentes resulta 
          indispensable hacer uso de parámetros numéricos exclusivos de cada uno de estos, los cuales por lo general, se representan y determinan 
          mediante el uso de gráficos y tablas. En este punto, resulta pertinente señalar que, mediante el procesamiento de imágenes se han extraido los datos de las gráficas 
          correspondientes a cada uno de estos parametros numéricos, para poder representarlos mediante tablas y, posteriormente, mediante 
          interpolaciones, calcular el parámetro numérico deseado de manera rapida y precisa.
        '''
col3, col4 = st.columns([1, 1])
with col3:
    with st.form('form1'):
        st.write(tex2)
        st.latex(r'{x_{{n_{a,b}}}} = \frac{{{x_{{n_{b,a}}}} - {x_{{1_{b,a}}}}}}{{{x_{{2_{b,a}}}} - {x_{{1_{b,a}}}}}}\left( {{x_{{2_{a,b}}}} - {x_{{1_{a,b}}}}} \right) + {x_{{1_{a,b}}}}')
        st.latex(r'{y_{{n_{a,b}}}} = \frac{{{y_{{n_{b,a}}}} - {y_{{1_{b,a}}}}}}{{{y_{{2_{b,a}}}} - {y_{{1_{b,a}}}}}}\left( {{y_{{2_{a,b}}}} - {y_{{1_{a,b}}}}} \right) + {y_{{1_{a,b}}}}')
        x1 = st.slider('Ángulo', 5, 35, 5, 1)
        y1 = st.slider('Dientes', 20, 300, 20, 1)
        # st.latex(r'''\text{El factor geometrico es:} \hspace{1mm}''' + rf'''{np.round(fz(x1, y1)[0], 5)}''')
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

col19, col20 = st.columns([1, 1])
with col19:
     with st.form('form2'):
          data1 = {'Parametro': ['Densidad', 'Diamentro externo', 'Diametro interno', 'Longitud', 'Fuerza', 'Momento', 'Apoyo inicial', 'Apoyo final', 'Elementos'], 'Valor': ['0'] * 9}
          df1   = pd.DataFrame(data = data1, index = ['-'] * 9)
          st.experimental_data_editor(df1, key = 'table1')
          submitted2 = st.form_submit_button("Calcular eje")
v = st.session_state.table1
st.write(v['edited_cells']['0:2'])
#st.components.v1.html(f'<iframe src={i}> </iframe>')
#url1 = 'https://junior19.starboard.host/v1/embed/0.15.3/cbljq1i23akg00a8j9b0/n529MY4/'
#st.markdown(f'<iframe src={url1} height="660" width="50%"></iframe>', unsafe_allow_html = True)

st.divider()
foto = Image.open(r'Imagenes/FotografiaJR.png')
col1, col2 = st.columns([3, 1], gap = 'large')
col1.header('Sobre mí ...')
desc = 'Cuando elegí la carrera de Ingeniería Mecánica no estaba seguro si en verdad era lo que queria estudiar,\
        pero a medida que avanzaba me di cuenta que me encontraba en el lugar correcto, dado que me considero una persona a la cual le\
        gusta aprender de todo, y esta carrera es tan amplia que me permite involucrarme en distintas ramas tales\
        como el diseño mecánico, energías renovables y automatización (mis preferidas, obviamente hay mas). Por otra parte, otra de mis pasiones \
        es la programación, sobre todo el desarrollo de aplicaciones web, lo cual cabe decir, me ha ayudado bastante, tando en la\
        universidad como en el mundo laboral. Este proyecto es un claro ejemplo de lo que menciono, ya que para su desarrollo han sido\
        necesarios mis conocimientos en ingeniería mecánica y programación, y del cual me siento muy orgulloso, ya que en comparación con otros\
        proyectos similares, humildemente considero que el mío es mucho mejor.'
col1.write(desc)
col2.image(foto, caption = 'Junior Joel Aguilar Hancco')
