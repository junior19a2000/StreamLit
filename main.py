import base64
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from scipy import interpolate as numint

st.set_page_config(page_title = "Tesis", page_icon = "🦅", layout = "wide")

st.latex(r'\Huge \text{Power System Transmission Calculator}')
st.latex(r'\footnotesize \text{Proyecto de tesis para obtener el grado de ingeniero mecánico en la Universidad Nacional de San Agustin} \\ \text{Arequipa - 2023}')
st.divider()

file_    = open(r'D:\Programs\Python\Logo.gif', "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
col1, col2 = st.columns([1.5, 1], gap = 'large')
col1.header('Resumen')
tex1 = 'El presente proyecto de investigación se realizo con la finalidad de optimizar el proceso de diseño de un\
        sistema de transmisión de potencia como el que se muestra a la derecha. Para ello se analizaron los\
        componentes generales de dichos sistemas, tales como las correas, cadenas, engranajes, ejes y chavetas,\
        en base a las distintas metodologias, criterios y normativas que existen en la actualidad.  \nCon el proceso\
        de calculo establecido para cada uno de ellos, se desarrollo una interfaz gráfica para que el usuario pueda\
        mejorar su diseño mediante la variación de los parametros iniciales del sistema.  \nComo producto final se\
        creó Power System Transmission Calculator, el cual permite cálcular los componenetes previamente\
        mencionados, de manera rapida, precisa y optima, cumpliendo asi con el proposito establecido para el proyecto de investigación.'
col1.write(tex1)
col2.markdown(f'<img src = "data:image/gif;base64,{data_url}" width = "450">', unsafe_allow_html = True)
st.divider()

st.header('Marco Metodológico')

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
col3, col4 = st.columns([1, 1])
with col3:
    x1 = st.slider('Ángulo', 5, 35, 5, 1)
    y1 = st.slider('Dientes', 20, 300, 20, 1)
    st.latex(r'''\text{El factor geometrico es:} \hspace{1mm}''' + rf'''{np.round(fz(x1, y1)[0], 5)}''')
img2 = mpimg.imread(f'D:\Programs\Python\carta1.png')
img3 = plt.imshow(img2)
plt.plot([[fx(x1), 50], [fx(x1), fx(x1)]], [[650, fy(fz(x1, y1))], [fy(fz(x1, y1)), fy(fz(x1, y1))]], 'red', linestyle = 'dashed')
plt.scatter(fx(x1), fy(fz(x1, y1)), 25, 'red')
plt.axis('off')
col4.pyplot(plt.gcf())

#st.components.v1.html(f'<iframe src={i}> </iframe>')
#url1 = 'https://junior19.starboard.host/v1/embed/0.15.3/cbljq1i23akg00a8j9b0/n529MY4/'
#st.markdown(f'<iframe src={url1} height="660" width="50%"></iframe>', unsafe_allow_html = True)

st.divider()
foto = Image.open(r'D:\Programs\Python\FotografiaJR.png')
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
