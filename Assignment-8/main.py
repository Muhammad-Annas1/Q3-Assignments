from models.book import Book
from services.collection import BookCollection

def main():
    collection = BookCollection()
    

    while True:
        print("\n📚 Book Collection CLI")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Remove Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")

            new_book = Book(title, author, year)
            collection.add_book(new_book)
            print(f"✅ Added: {new_book}")
        
        elif choice == "2":
            collection.show_books()
        
        elif choice == "3":
            collection.show_books()
            try:
                index = int(input("Enter the index to remove: "))
                collection.remove_book(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        
        elif choice == "4":
            print("👋 Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
