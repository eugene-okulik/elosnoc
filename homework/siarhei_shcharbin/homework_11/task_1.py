class Book:
    material = 'Paper'
    is_there_a_text = 'Yes'

    def __init__(self, book_name, author, pages_count, isbn, is_reserved):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn
        self.is_reserved = bool(is_reserved)

    def book_details(self):
        if self.is_reserved:
            return (
                f"Book: {self.book_name}, Author: {self.author}, Pages: {self.pages_count},"
                f" Material: {self.material}" + ", Reserved"
            )
        else:
            return (
                f"Book: {self.book_name}, Author: {self.author}, Pages: {self.pages_count}, Material: {self.material}"
            )


book_1 = Book('Idiot', 'Fedor Dostoevskiy', 736, '978-5-9691-1577', True)
book_2 = Book('Hamlet', 'William Shakespeare', 224, '978-1-3988-0779-2', False)
book_3 = Book('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 416, '978-5-17-119245-7', True)
book_4 = Book('In Search of Lost Time', 'Marcel Proust', 1238, '978-5-9922-0403-2', False)
book_5 = Book('Odyssey', 'Homer', 312, '978-5-91181-827-2', False)
print(book_1.book_details())
print(book_2.book_details())
