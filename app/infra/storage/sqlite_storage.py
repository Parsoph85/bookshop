from domain.book import Book
from infra.storage.db import db_work


class SQLiteStorage:

    def add(self, book):
        db_string = (f"INSERT INTO books (title, description, publish_year, pages_count, created_at) VALUES ('{book.title}','{book.description}','{book.publish_year}','{book.pages_count}','{book.created_at}')")
        db_work(db_str=db_string)

    def delete(self, id):
        db_string = f"DELETE FROM books WHERE id='{int(id)}'"
        db_work(db_str=db_string)


    def get(self):
        outp = []
        db_string = f"SELECT * FROM books"
        answer = db_work(db_str=db_string)

        for line in answer:
            n_book = Book(line[1], line[2], line[3], line[4], line[5])
            outp.append(n_book)
        return (outp)

