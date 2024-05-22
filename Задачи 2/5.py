class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print('Книга добавлена в список')

    def remove_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            print('Книга удалена из списка')

    def search_book(self, title):
        for book in self.book_list:
            if book == title:
                return 'Книга найдена в списке'
        return 'Книга не найдена в списке'
