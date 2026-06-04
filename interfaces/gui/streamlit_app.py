import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Personal Library",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Personal Library Manager")

tab1, tab2, tab3 = st.tabs(
    ["Libros", "Autores", "Géneros"]
)

# ==========================
# AUTORES
# ==========================

with tab2:

    st.header("Agregar autor")

    with st.form("author_form"):
        name = st.text_input("Nombre")
        nationality = st.text_input("Nacionalidad")

        submitted = st.form_submit_button("Guardar")

        if submitted:
            response = requests.post(
                f"{API_URL}/authors/",
                json={
                    "name": name,
                    "nationality": nationality,
                },
            )

            if response.status_code == 200:
                st.success("Autor agregado")
            else:
                st.error(response.text)

    st.header("Autores")

    response = requests.get(
        f"{API_URL}/authors/"
    )

    if response.status_code == 200:
        authors = response.json()

        if authors:
            st.dataframe(authors)
        else:
            st.info("No hay autores")


# ==========================
# GENEROS
# ==========================

with tab3:

    st.header("Agregar género")

    with st.form("genre_form"):
        name = st.text_input("Nombre género")

        submitted = st.form_submit_button(
            "Guardar género"
        )

        if submitted:
            response = requests.post(
                f"{API_URL}/genres/",
                json={
                    "name": name,
                },
            )

            if response.status_code == 200:
                st.success("Género agregado")
            else:
                st.error(response.text)

    st.header("Géneros")

    response = requests.get(
        f"{API_URL}/genres/"
    )

    if response.status_code == 200:
        genres = response.json()

        if genres:
            st.dataframe(genres)
        else:
            st.info("No hay géneros")


# ==========================
# LIBROS
# ==========================

with tab1:

    st.header("Agregar libro")

    title = st.text_input("Título")

    author_id = st.number_input(
        "ID Autor",
        min_value=1,
        step=1,
    )

    genre_id = st.number_input(
        "ID Género",
        min_value=1,
        step=1,
    )

    published_year = st.number_input(
        "Año publicación",
        value=2024,
    )

    total_pages = st.number_input(
        "Total páginas",
        min_value=1,
        value=100,
    )

    read_pages = st.number_input(
        "Páginas leídas",
        min_value=0,
        value=0,
    )

    score = st.slider(
        "Puntaje",
        1,
        5,
        3,
    )

    review = st.text_area(
        "Review"
    )

    if st.button(
        "Crear libro",
        key="create_book"
    ):

        response = requests.post(
            f"{API_URL}/books/",
            json={
                "title": title,
                "author_id": int(author_id),
                "genre_id": int(genre_id),
                "published_year": int(
                    published_year
                ),
                "total_pages": int(
                    total_pages
                ),
                "read_pages": int(
                    read_pages
                ),
                "score": int(score),
                "review": review,
            },
        )

        if response.status_code == 200:
            st.success("Libro creado")
        else:
            st.error(response.text)

    st.divider()

    st.header("Actualizar progreso de lectura")

    progress_book_id = st.number_input(
        "ID del libro",
        min_value=1,
        step=1,
        key="progress_book_id",
    )

    progress_pages = st.number_input(
        "Páginas leídas",
        min_value=0,
        step=1,
        key="progress_pages",
    )

    if st.button(
        "Actualizar progreso",
        key="update_progress",
    ):

        response = requests.patch(
            f"{API_URL}/books/{progress_book_id}/progress",
            json={
                "read_pages": int(
                    progress_pages
                )
            },
        )

        if response.status_code == 200:
            st.success(
                "Progreso actualizado"
            )
        else:
            st.error(response.text)

    st.divider()


    st.header("Actualizar review")

    review_book_id = st.number_input(
        "ID libro para review",
        min_value=1,
        step=1,
        key="review_book_id",
    )

    new_review = st.text_area(
        "Nueva review",
        key="new_review",
    )

    if st.button(
        "Actualizar review",
        key="update_review",
    ):

        response = requests.patch(
            f"{API_URL}/books/{review_book_id}/review",
            json={
                "review": new_review
            },
        )

        if response.status_code == 200:
            st.success(
                "Review actualizada"
            )
        else:
            st.error(response.text)
    
    st.divider()

    st.divider()

    st.header("Actualizar puntaje")

    score_book_id = st.number_input(
        "ID libro para puntaje",
        min_value=1,
        step=1,
        key="score_book_id",
    )

    new_score = st.slider(
        "Nuevo puntaje",
        1,
        5,
        3,
        key="new_score",
    )

    if st.button(
        "Actualizar puntaje",
        key="update_score",
    ):

        response = requests.patch(
            f"{API_URL}/books/{score_book_id}/score",
            json={
                "score": int(new_score)
            },
        )

        if response.status_code == 200:
            st.success(
                "Puntaje actualizado"
            )
        else:
            st.error(response.text)

    st.divider()


    st.header("Buscar libros por autor")

    author_search_id = st.number_input(
        "ID autor",
        min_value=1,
        step=1,
        key="author_search",
    )

    if st.button(
        "Buscar libros del autor",
        key="author_books",
    ):

        response = requests.get(
            f"{API_URL}/books/author/{author_search_id}"
        )

        if response.status_code == 200:

            books = response.json()

            if books:

                for book in books:

                    st.write(
                        f"📚 {book['title']}"
                    )

            else:
                st.info(
                    "Este autor no tiene libros"
                )
    st.divider()


    st.header("Buscar libros por género")

    genre_search_id = st.number_input(
        "ID género",
        min_value=1,
        step=1,
        key="genre_search",
    )

    if st.button(
        "Buscar libros del género",
        key="genre_books",
    ):

        response = requests.get(
            f"{API_URL}/books/genre/{genre_search_id}"
        )

        if response.status_code == 200:

            books = response.json()

            if books:

                for book in books:

                    st.write(
                        f"📚 {book['title']}"
                    )

            else:
                st.info(
                    "No hay libros en este género"
                )

    st.divider()

    st.header("Listado de libros")

    response = requests.get(
        f"{API_URL}/books/"
    )

    if response.status_code == 200:

        books = response.json()

        if books:

            for book in books:

                st.subheader(
                    book["title"]
                )

                st.write(
                    f"ID: {book['id']}"
                )

                st.write(
                    f"Autor ID: {book['author_id']}"
                )

                st.write(
                    f"Género ID: {book['genre_id']}"
                )

                st.write(
                    f"Año: {book['published_year']}"
                )

                st.write(
                    f"Páginas: "
                    f"{book['read_pages']} / "
                    f"{book['total_pages']}"
                )

                porcentaje = (
                    book["read_pages"]
                    / book["total_pages"]
                )

                st.progress(
                    min(
                        porcentaje,
                        1.0
                    )
                )

                st.write(
                    f"Puntaje: "
                    f"{book.get('score')}"
                )

                st.write(
                    f"Review: "
                    f"{book.get('review')}"
                )

                st.divider()

        else:
            st.info(
                "No hay libros"
            )


