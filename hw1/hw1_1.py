class Book:
    def __init__(self, author: str, name: str, year: int, genre: str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.reviews = []

    def __str__(self, review: str):
        if self.reviews:
            review = ""
            for item in self.reviews:
                review += f"{item}\n"
            return (
                f"{self.author}, {self.name}, {self.year}, {self.genre} \nReviews: {self.review}"
            )
        else:
            return (
                f"{self.author}, {self.name}, {self.year}, {self.genre} \nReviews: none"
            )

    def add_review(self, review: str):
        self.reviews.append(review)


class Review:
    def __init__(self, review: str):
        self.review = review

    def __str__(self):
        return f"{self.review}"


book1 = Book("author1", "name1", 1, "genre1")
book2 = Book("author2", "name2", 2, "genre2")
book3 = Book("author3", "name3", 3, "genre3")
book4 = Book("author4", "name4", 4, "genre4")

book1.add_review(Review("review1.1"))
book1.add_review(Review("review1.2"))

book2.add_review(Review("review2.1"))

list_books = [book1, book2, book3, book4]

for book in list_books:
    print(f"{book}\n")
