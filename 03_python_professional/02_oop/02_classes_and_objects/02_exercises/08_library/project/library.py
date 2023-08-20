from project.user import User


class Library:

    def __init__(self):
        self.user_records = list()
        self.books_available = dict()
        self.rented_books = dict()

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username] += {book_name: days_to_return}
            self.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user, book_info in self.rented_books.items():
            if book_name in book_info:
                final_days = self.rented_books[user][book_info]
                return f"The book {book_name} is already rented and will be available in {final_days} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            self.rented_books[user.username].remove(book_name)
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"

