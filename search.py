"""
@Time   :2022-12-14
@Author :jobcher
@File   :search.py
"""
from http import HTTP


class Search:
    isbn_url = 'http://t.yushu.cim/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.cim/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword)
        result = HTTP.get(url)
        return result
