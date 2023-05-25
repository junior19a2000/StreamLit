import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title = "Junior 19", page_icon = "👑", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_n7kzkgjp.json")

with st.container():
    st.subheader("Bienvenido al sitio personal de ... :wave:")
    st.title("Junior Joel Aguilar Hancco")
    st.write(
        "Ingeniero Mecánico de profesión y apasionado a la programación =)"
    )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("¿Qué encontrare aqui?")
        st.write("##")
        st.write(
            """
            Bueno, basicamente las cosas de mi vida que me gustaria compartir con otros, tales como:
            
            - Proyectos desarrollados antes, ahora y despues.
            - Fotos y videos de los lugares que visite, de las personas que aprecie y de los momentos memorables.
            - Listas de mis libros, canciones, peliculas y otros favoritos.
            - Planes y metas a futuro.

            El desarrollo de esta pagina esta en progreso, asi que se actualizara constamente en el futuro.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")
