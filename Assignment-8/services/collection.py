import json
import os
from models.book import Book

class BookCollection:
    def __init__(self, filepath="books.json"):
        self.books = []
        self.filepath = filepath
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                try:
                    data = json.load(f)
                    self.books = [Book(**book) for book in data]
                except json.JSONDecodeError:
                    self.books = []

    def save_books(self):
        with open(self.filepath, "w") as f:
            json.dump([book.__dict__ for book in self.books], f, indent=2)

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def show_books(self):
        if not self.books:
            print("📭 No books in the collection yet.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")

    def remove_book(self, index: int):
        if 0 < index <= len(self.books):
            removed = self.books.pop(index - 1)
            self.save_books()
            print(f"❌ Removed: {removed}")
        else:
            print("⚠️ Invalid index.")
