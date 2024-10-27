import json
books = [
     {"title": "Тайна чёрного дракона ", "author": "Анна Джейн", "year": "2022"},
     {"title": "Наследница чёрного дракона", "author": "Анна Джейн ", "year": "2022"},
     {"title": "Двериндрариум. Мёртвое", "author": "Марина Суржевская", "year": "2023"},
     {"title": "Из крови и пепла", "author": "Дженнифер Арментроут", "year": "2020"},
     {"title": "Мара и Морок", "author": "Лия Арден", "year": "2022"}
]
json_str = json.dumps(books)
count = 0
for book in books:
    count += 1
    print( "-" * 20, f"Книга {count}" , "-" * 20,)
    print(f"Название: {book["title"]}, Автор: {book["author"]},")
    print("-" * 20, f"{book["year"]}" , "-" * 20)
