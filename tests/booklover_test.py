import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        bl = BookLover("Alice", "alice@example.com", "mystery")
        bl.add_book("The Hound of the Baskervilles", 5)
        self.assertIn("The Hound of the Baskervilles", bl.book_list['book_name'].values)

    def test_2_add_book(self):
        bl = BookLover("Bob", "bob@example.com", "fantasy")
        bl.add_book("The Hobbit", 4)
        bl.add_book("The Hobbit", 4)  # Adding the same book again
        self.assertEqual(len(bl.book_list), 1)  # Should only be 1 book

    def test_3_has_read(self):
        bl = BookLover("Charlie", "charlie@example.com", "historical fiction")
        bl.add_book("War and Peace", 5)
        self.assertTrue(bl.has_read("War and Peace"))

    def test_4_has_read(self):
        bl = BookLover("Diana", "diana@example.com", "scifi")
        self.assertFalse(bl.has_read("Dune"))

    def test_5_num_books_read(self):
        bl = BookLover("Ethan", "ethan@example.com", "thriller")
        bl.add_book("Gone Girl", 4)
        bl.add_book("The Girl with the Dragon Tattoo", 5)
        self.assertEqual(bl.num_books_read(), 2)

    def test_6_fav_books(self):
        bl = BookLover("Fiona", "fiona@example.com", "romance")
        bl.add_book("Pride and Prejudice", 5)
        bl.add_book("Twilight", 2)
        bl.add_book("The Fault in Our Stars", 4)
        fav_books = bl.fav_books()
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    
    unittest.main(verbosity=3)