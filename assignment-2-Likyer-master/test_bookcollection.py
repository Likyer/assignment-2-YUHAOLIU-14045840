"""(Incomplete) Tests for BookCollection class."""
from bookcollection import BookCollection
from book import Book


def run_tests():
    """Test BookCollection class."""

    # Test empty BookCollection (defaults)
    print("Test empty BookCollection:")
    book_collection = BookCollection()
    print(book_collection)
    assert not book_collection.books  # PEP 8 suggests not using len() to test for empty lists

    # Test loading books
    print("Test loading books:")
    book_collection.load_books('books.csv')
    print(book_collection)
    assert book_collection.books  # assuming CSV file is non-empty, length should be non-zero

    # Test adding a new Book with values
    print("Test adding new book:")
    book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    print(book_collection)

    # Test sorting books
    print("Test sorting - author:")
    book_collection.sort("author")
    print(book_collection)
    # TODO: Add more sorting tests
    print("Test sorting - title:")
    book_collection.sort("title")
    print(book_collection)

    print("Test sorting - number of pages:")
    book_collection.sort("number of pages")
    print(book_collection)

    # TODO: Test get_required_pages()
    print("Test get_required_pages():")
    new_book_collection = BookCollection()

    assert new_book_collection.get_required_pages() == 0
    new_book_collection.load_books('books.csv')
    assert new_book_collection.get_required_pages() == 594
    new_book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    assert new_book_collection.get_required_pages() == 1593

    # TODO: Test saving books (check CSV file manually to see results)
    new_book_collection.saving_books('test_saving.csv')

    # TODO: Add more tests, as appropriate
    # test descending order
    print("Test sorting - number of pages in descending order:")
    book_collection.sort("number of pages", descending=True)
    print(book_collection)

    # test the keys not in book attributes
    print("Test sorting - incorrect key:")
    try:
        book_collection.sort("pages")
    except AssertionError as e:
        print(str(e))


run_tests()
