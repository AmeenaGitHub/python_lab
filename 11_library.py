# 11 Library Catalogue
FILE = "C:/Users/user/Desktop/Python/library.txt"

def load_books():
    try:
        with open(FILE) as f:
            return [line.strip().split("|") for line in f if line.strip()]
    except FileNotFoundError:
        return []


def add_book():
    book_id = len(load_books()) + 1  # next ID = number of books + 1
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    with open(FILE, "a") as f:  # "a" appends, so old entries are kept
        f.write(f"{book_id}|{title}|{author}\n")
    print(f"Book added with ID {book_id}.")


def show(books):
    if not books:
        print("No books found.")
    for book_id, title, author in books:
        print(f"[{book_id}] {title} by {author}")


def search():
    key = input("Search title or author: ").lower()
    show([b for b in load_books() if key in b[1].lower() or key in b[2].lower()])


def total_report():
    print("Total books:", len(load_books()))


def author_report():
    author = input("Author name: ").lower()
    show([b for b in load_books() if author in b[2].lower()])


menu = {"1": add_book, "2": search, "3": total_report, "4": author_report}

while True:
    choice = input("\n1.Add  2.Search  3.Total Books  4.Books by Author  5.Exit > ")
    if choice == "5":
        break
    menu.get(choice, lambda: print("Invalid choice"))()