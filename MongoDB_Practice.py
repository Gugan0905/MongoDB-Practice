from pymongo import MongoClient

# Establish a connection to the MongoDB instance
client = MongoClient('mongodb://localhost:27017/')
db = client['booksdb']  # Replace 'your_database_name' with your actual database name
collection = db['books']  # Assuming your collection is named 'books'

def find_books_by_category(category):
    # Find books by the specified category
    books = collection.find({"categories": category}, {"isbn": 1, "title": 1, "_id": 0})

    # Print the ISBN and titles of books in the category
    for book in books:
        print(f"ISBN: {book['isbn']}, Title: {book['title']}")

if __name__ == "__main__":
    category = input("Enter category: ").strip()
    print(category)
    find_books_by_category(category)
