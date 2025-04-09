import mysql.connector

# Step 1: Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",       # ← replace with your MySQL username (e.g., root)
    password="pratham@2005",   # ← replace with your MySQL password
    database="bookstore"
)

cursor = db.cursor()

# Step 2: INSERT (Create)
def create_book(title, author, price):
    cursor.execute("INSERT INTO books (title, author, price) VALUES (%s, %s, %s)", (title, author, price))
    db.commit()
    print("Book added!")

# Step 3: SELECT (Read)
def read_books():
    cursor.execute("SELECT * FROM books")
    for book in cursor.fetchall():
        print(book)

# Step 4: UPDATE
def update_price(book_id, new_price):
    cursor.execute("UPDATE books SET price = %s WHERE id = %s", (new_price, book_id))
    db.commit()
    print("Price updated!")

# Step 5: DELETE
def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    db.commit()
    print("Book deleted!")

# Try the functions:
create_book("The Alchemist", "Paulo Coelho", 10.99)
read_books()
update_price(1, 12.99)
delete_book(1)

# Step 6: Close connection
cursor.close()
db.close()