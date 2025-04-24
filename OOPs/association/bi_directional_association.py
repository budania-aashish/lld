class Library:
    def __init__(self, name, location, books):
        self.name = name
        self.location = location
        self.books = books

    def get_name(self):
        return self.name

    def get_details(self):
        print(f"In library {self.name} situated in {self.location}")
        for book in self.books:
            print(f"Title : {book.get_title()} published_year : {book.get_published_year()}")
        print("\n")
    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, published_year, library_obj):
        self.title = title
        self.published_year = published_year
        self.library = library_obj

    def get_title(self):
        return self.title

    def get_published_year(self):
        return self.published_year

    def get_library_name(self):
        return self.library.get_name()

    def get_details(self):
        return f"title : {self.title}, published_year : {self.published_year}, library_name: {self.get_library_name()}"

if __name__ == '__main__':
    library = Library("Central Library", "Delhi", [])
    library.get_details()
    book1 = Book("Wings of Fire", 2002, library)
    book2 = Book("The power of Habit", 1998, library)
    print(book1.get_details())
    print(book2.get_details())
    library.add_book(book1)
    library.add_book(book2)
    library.get_details()


