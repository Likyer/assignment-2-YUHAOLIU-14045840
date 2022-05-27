"""..."""

from book import Book
import csv

# Create your BookCollection class in this file


class BookCollection:
    def __init__(self):
        self.books = []

    def load_books(self, csv_path):
        if len(self.books) != 0:
            self.books = []
        with open(csv_path, 'r') as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                title, author, pages, status = line.split(',')
                pages = int(pages)
                is_completed = status.lower() == 'c'
                book = Book(title, author, pages, is_completed)
                self.books.append(book)
            file.close()

    def add_book(self, book):
        self.books.append(book)

    def sort(self, key, descending=False):
        keys_list = ['title', 'author', 'number of pages']
        if key not in keys_list:
            raise AssertionError('the key should be in the {}'.format(keys_list))
        if key == 'title':
            self.books.sort(key=lambda x: x.title, reverse=descending)
        elif key == 'author':
            self.books.sort(key=lambda x: x.author, reverse=descending)
        elif key == 'number of pages':
            self.books.sort(key=lambda x: x.number_of_pages, reverse=descending)

    def get_required_pages(self):
        res = 0
        for book in self.books:
            if not book.is_completed:
                res += book.number_of_pages
        return res

    def saving_books(self, file_path):
        with open(file_path, 'w') as file:
            for book in self.books:
                line = '{},{},{},{}\n'.format(book.title, book.author,
                                              book.number_of_pages, 'c' if book.is_completed else 'r')
                file.write(line)
            file.close()

    def book_to_read(self):
        res = None
        max_pages = -1
        for book in self.books:
            if not book.is_completed:
                if book.number_of_pages > max_pages:
                    max_pages = book.number_of_pages
                    res = book
        return res

    def __iter__(self):
        for book in self.books:
            yield book

    def __str__(self):
        desc = 'There are {} books in the collection\n'.format(len(self.books))
        desc += 'The books list is following:\n'
        for book in self.books:
            desc += str(book)
            desc += '\n'
        return desc