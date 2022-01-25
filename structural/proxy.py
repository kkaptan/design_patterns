from abc import ABC
from abc import abstractmethod

import math 
import random

class Book(ABC):
    """Book"""

    @abstractmethod
    def pages(self) -> int:
        """returns number of pages in the book"""
        raise NotImplemented("page method is not implemented.")

    @abstractmethod
    def read_page(self, page: int) -> str:
        """return the contents of the page passed."""
        raise NotImplemented("read_page method is not implemented.")


class EagerLoadingBook(Book):
    
    @classmethod
    def alphabet(cls):
        upper = list(range(65, 90))
        lower = list(range(97, 122))
        punc  = [ord(i) for i in ('!', '.', ' ')]
        return upper + lower + punc

    
    def __init__(self, book_len: int,  page_size: int):
        #long initialization
        self._page_size = page_size
        self._book_len = book_len
        words = [chr(random.choice(self.alphabet())) for i in range(book_len)] 
        self._contents = ''.join(words)

    @property
    def pages(self):
        """returns the total number of pages in the book"""
        return math.ceil(len(self._contents) / self._page_size)

    def read_page(self, page):
        """returns the contents of the page passed. If the
        page is negative or greater than the number of pages a
        value error is raised.
        """ 
        if page < 0 or page > self.pages - 1:
            raise ValueError('No such page')

        start = self._page_size * page
        end = start + self._page_size

        return self._contents[start:end]



class LazyLoadingBookProxy(Book):

    def __init__(self, book_len: int, page_size: int):
        self._book_len = book_len
        self._page_size = page_size
        self._book = None
    
    def _init_book(self):
        """Initialise the book if not yet initialised.
        """
        if self._book:
            return
        self._book = EagerLoadingBook(self._book_len, self._page_size)

    def pages(self):
        """returns the total pages of the book"""
        self._init_book()
        return self._book.pages()

    def read_page(self, page):
        """returns the contents of page passed."""
        self._init_book()
        return self._book.read_page(page)

if __name__ == '__main__':
    print('Starts Loading Immediately. Then prints B.')
    b = EagerLoadingBook(10_000_000, 1_000)
    print('B')
    print(b.read_page(999))

    c = LazyLoadingBookProxy(10_000_000, 1_000)
    print('Prints C instantly. Starts loading when method is called.')
    print(c.read_page(999))
