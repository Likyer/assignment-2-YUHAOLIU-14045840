"""..."""


# Create your Book class in this file


class Book:
    def __init__(self, title='', author='', number_of_pages=0, is_completed=False):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_completed = is_completed

    def mark_required(self):
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def is_long(self):
        return self.number_of_pages >= 500

    def __str__(self):
        desc = 'Book Info:\nTitle: {}\nAuthor: {}\nNumber of Pages: {}\nCompleted: {}\n' \
                        .format(self.title, self.author, self.number_of_pages, self.is_completed)
        return desc