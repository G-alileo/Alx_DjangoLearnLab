## Using the api endpoints
API Features: Filtering, Searching, and Ordering

## Filtering:
- Filter books by title: `?title=Atomic`
- Filter books by author name: `?author=John`
- Filter books by publication year: `?publication_year=2020`

## Searching:
- Search books by title or author: `?search=magic`

## Ordering:
- Order by title: `?ordering=title`
- EX: `http://127.0.0.1:8000/api/books/?ordering=title`

- Order by publication year (ascending): `?ordering=publication_year`
- EX: `http://127.0.0.1:8000/api/books/?ordering=publication_year`

- Order by publication year (descending): `?ordering=-publication_year`
- EX: `http://127.0.0.1:8000/api/books/?ordering=-publication_year`
