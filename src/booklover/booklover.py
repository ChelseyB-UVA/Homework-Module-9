import pandas as pd

class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list: pd.DataFrame = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame(columns=['book_name', 'book_rating'])
        else:
            self.book_list = book_list

    def add_book(self, book_name: str, rating: int):
        if not isinstance(rating, int) or rating < 0 or rating > 5:
            print("Rating must be an integer between 0 and 5.")
            return
        
        if book_name in self.book_list['book_name'].values:
            print(f"You have already added the book '{book_name}'.")
            return
        
        new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [rating]
        })

        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1

    def has_read(self, book_name: str) -> bool:
        return book_name in self.book_list['book_name'].values

    def num_books_read(self) -> int:
        return self.num_books

    def fav_books(self) -> pd.DataFrame:
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("The Popol Vuh", 5)
    
    print("Number of books read:", test_object.num_books_read())
    print("Has read 'War of the Worlds':", test_object.has_read("War of the Worlds"))
    print("Favorite books:\n", test_object.fav_books())