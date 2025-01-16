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


class SchoolBook(Book):
    def __init__(self, book_name, author, pages_count, isbn, is_reserved, school_subject, class_grade, has_practices):
        super().__init__(book_name, author, pages_count, isbn, is_reserved)
        self.school_subject = school_subject
        self.class_grade = class_grade
        self.has_practices = bool(has_practices)

    def book_details(self):
        if self.is_reserved:
            return (
                f"Book: {self.book_name}, Author: {self.author}, Pages: {self.pages_count},"
                f" Subject: {self.school_subject}, Class: {self.class_grade}" + ", Reserved"
            )
        else:
            return (
                f"Book: {self.book_name}, Author: {self.author}, Pages: {self.pages_count},"
                f" Subject: {self.school_subject}, Class: {self.class_grade}"
            )


book_1 = SchoolBook(
    'Algebra', 'Lobanov A. P.', 96, '555-5-9691-1577', True, 'Math', 5, True
)
book_2 = SchoolBook(
    'World History', 'Koshelev V. S.', 134, '555-1-3988-0779-2', False, 'History', 7, False
)
book_3 = SchoolBook(
    'English', 'Naumova E. G.', 126, '555-5-17-119245-7', True, 'English', 10, True
)
print(book_1.book_details())
print(book_2.book_details())
