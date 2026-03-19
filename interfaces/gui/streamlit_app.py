import streamlit as st
from my_app.services import LibroService
from my_app.storage import JsonStorage

storage_libros= JsonStorage('libros.json')
libro_service = LibroService(storage_libros)
service = LibroService(storage_libros)

storage_autores = JsonStorage('autores.json')
service_autores = LibroService(storage_autores)

storage_generos = JsonStorage('generos.json')
service_generos = LibroService(storage_generos)

st.title("Gestión de Libros")

# Formulario para agregar un nuevo libro
st.header("Agregar un nuevo libro")
with st.form("add_book_form"):
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    genero = st.text_input("Género")
    submit_button = st.form_submit_button("Agregar Libro")
    if submit_button:
        libro_service.agregar_libro(titulo, autor, genero)
        st.success("Libro agregado exitosamente")

# Formulario para buscar libros por título
st.header("Buscar libros por título")
with st.form("search_book_form"):
    search_title = st.text_input("Título a buscar")
    search_button = st.form_submit_button("Buscar")
    if search_button:
        libro = libro_service.buscar_libro_por_titulo(search_title)
        if libro:
            st.write(f"**Título:** {libro['titulo']}")
            st.write(f"**Autor:** {libro['autor']}")
            st.write(f"**Género:** {libro['genero']}")
        else:
            st.warning("No se encontró ningún libro con ese título")

# Formulario para eliminar un libro por título
st.header("Eliminar un libro por título")
with st.form("delete_book_form"):
    delete_title = st.text_input("Título a eliminar")
    delete_button = st.form_submit_button("Eliminar")
    if delete_button:
        libro_service.eliminar_libro(delete_title)
        st.success("Libro eliminado exitosamente")
# Formulario para buscar libros por autor
st.header("Buscar libros por autor")
with st.form("search_books_by_author_form"):
    search_author = st.text_input("Autor a buscar")
    search_button = st.form_submit_button("Buscar")
    if search_button:
        libros = libro_service.buscar_libros_por_autor(search_author)
        if libros:
            for libro in libros:
                st.write(f"**Título:** {libro['titulo']}")
                st.write(f"**Autor:** {libro['autor']}")
                st.write(f"**Género:** {libro['genero']}")
                st.write("---")
        else:
            st.warning("No se encontraron libros de ese autor")
# Formulario para buscar libros por género
st.header("Buscar libros por género")
with st.form("search_books_by_genre_form"):
    search_genre = st.text_input("Género a buscar")
    search_button = st.form_submit_button("Buscar")
    if search_button:
        libros = libro_service.buscar_libros_por_genero(search_genre)
        if libros:
            for libro in libros:
                st.write(f"**Título:** {libro['titulo']}")
                st.write(f"**Autor:** {libro['autor']}")
                st.write(f"**Género:** {libro['genero']}")
                st.write("---")
        else:
            st.warning("No se encontraron libros de ese género")
# Formulario para agregar un nuevo autor
st.header("Agregar un nuevo autor")
with st.form("add_author_form"):
    nombre_autor = st.text_input("Nombre del autor")
    submit_button = st.form_submit_button("Agregar Autor")
    if submit_button:
        service_autores.agregar_autor(nombre_autor)
        st.success("Autor agregado exitosamente")
# Formulario para agregar un nuevo género
st.header("Agregar un nuevo género")
with st.form("add_genre_form"):
    nombre_genero = st.text_input("Nombre del género")
    submit_button = st.form_submit_button("Agregar Género")
    if submit_button:
        service_generos.agregar_genero(nombre_genero)
        st.success("Género agregado exitosamente")
# Listado de autores 
st.header("Listado de autores")
autores = service_autores.listar_autores()
if autores:
    for autor in autores:
        st.write(f"**Nombre:** {autor['nombre']}")
        st.write("---")
else:
    st.info("No hay autores disponibles")
# Listado de libros
st.header("Listado de libros")
libros = libro_service.listar_libros()
if libros:
    for libro in libros:
        st.write(f"**Título:** {libro['titulo']}")
        st.write(f"**Autor:** {libro['autor']}")
        st.write(f"**Género:** {libro['genero']}")
        st.write("---")
else:
    st.info("No hay libros disponibles")

#Listado de géneros
st.header("Listado de géneros")
generos = service_generos.listar_generos()
if generos:
    for genero in generos:
        st.write(f"**Nombre:** {genero['nombre']}")
        st.write("---")
else:
    st.info("No hay géneros disponibles")

# Agregar review a un libro
st.header("Agregar una review a un libro")
with st.form("add_review_form"):
    review_title = st.text_input("Título del libro para la review")
    review_content = st.text_area("Contenido de la review")
    submit_button = st.form_submit_button("Agregar Review")
    if submit_button:
        libro_service.agregar_review(review_title, review_content)
        st.success("Review agregada exitosamente")
# Dar puntaje a un libro
st.header("Dar puntaje a un libro")
with st.form("rate_book_form"):
    rate_title = st.text_input("Título del libro para puntuar")
    rate_score = st.slider("Puntaje (1-5)", 1, 5)
    submit_button = st.form_submit_button("Dar Puntaje")
    if submit_button:
        libro_service.dar_puntaje(rate_title, rate_score)
        st.success("Puntaje dado exitosamente")

