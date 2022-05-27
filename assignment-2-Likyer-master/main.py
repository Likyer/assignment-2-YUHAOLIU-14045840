"""
Name:LIU YUHAO
Date:27/5/2022
Brief Project Description:CP1404/CP5632 – Assignment 2
Reading Tracker 2.0
GitHub URL:https://github.com/Likyer/assignment-2-LIUYUHAO-14045840

# Create your main program in this file, using the ReadingTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from matplotlib.pyplot import text
from bookcollection import BookCollection
from book import Book
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
import os

GREEN = [0, 1, 0, 1]

class ReadingTrackerApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(ReadingTrackerApp, self).__init__(**kwargs)
        self.book_lib = BookCollection()

    def build(self):
        self.title = "Reading Tracker"
        self.root = Builder.load_file('app.kv')
        self.init_ui()
        return self.root

    def init_ui(self):
        file_path = 'books.csv'
        if not os.path.isfile(file_path):
            self.popup_message('Warning', 'No books.csv found!', 'continue')
        self.render(file_path)

    def render(self, file_path=None):
        self.root.ids.book_layout.clear_widgets()
        if file_path:
            self.book_lib.load_books(file_path)
        top_bar = Label(text='Pages to read: {}'.format(self.book_lib.get_required_pages()),
                center_x=True, center_y=True
                )
        self.root.ids.book_layout.add_widget(top_bar)
        for book in self.book_lib:
            if book.is_completed:
                txt = '{} by {}, {} pages(completed)'
            else:
                txt = '{} by {}, {} pages'
            label = Label(text=txt.format(book.title, book.author, book.number_of_pages),
                          center_x=True, center_y=True
                          )
            if not book.is_completed:
                label.color = GREEN
            self.root.ids.book_layout.add_widget(label)
        book_to_read = self.book_lib.book_to_read()
        if book_to_read:
            bot_txt = 'You need to read {}. Get Started!'.format(book_to_read.title)
        else:
            bot_txt = 'You have completed all the books!'
        bottom_bar = Label(text=bot_txt.format(self.book_lib.get_required_pages()),
                center_x=True, center_y=True
                )
        self.root.ids.book_layout.add_widget(bottom_bar)

    def press_add(self):
        title = self.root.ids.title_input.text.strip()
        author = self.root.ids.author_input.text.strip()
        pages = self.root.ids.pages_input.text.strip()
        if title == '' or author == '' or pages == '':
            self.popup_message(title='Warning', message='Please input title, author and number of pages',
                               button_tip='close')
        try:
            pages = int(pages)
            if pages < 1:
                self.popup_message(title='Warning', message='the number of pages shoule be an interge>=1')
            book = Book(title, author, pages)
            self.book_lib.add_book(book)
            self.book_lib.saving_books('books.csv')
            self.render('books.csv')
        except Exception as e:
            msg = str(e)
            self.popup_message(title='Error', message=msg, button_tip='close')

    def press_clear(self):
        self.root.ids.title_input.text = ''
        self.root.ids.author_input.text = ''
        self.root.ids.pages_input.text = ''

    def sort_books(self):
        key = self.root.ids.key_sp.text.lower()
        self.book_lib.sort(key)
        self.render()

    def popup_message(self, title, message, button_tip):
        """
        pop up a message
        Args:
            title (_type_): title
            message (_type_): message
            button_tip (_type_): button text
        """
        box = BoxLayout(orientation = 'vertical', padding = (10))
        box.add_widget(Label(text=message))
        btn1 = Button(text=button_tip,)
        box.add_widget(btn1)

        popup = Popup(title=title, title_size= (30),
                    title_align='center', content=box,
                    size_hint=(None, None), size=(700, 700),
                    auto_dismiss = False)

        btn1.bind(on_press = popup.dismiss)
        popup.open()





if __name__ == '__main__':
    ReadingTrackerApp().run()