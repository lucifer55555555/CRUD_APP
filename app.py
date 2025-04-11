import mysql.connector

# ----------------------------
# Database Connection
# ----------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",         # your MySQL username
    password="pratham@2005",         # your password, often blank with XAMPP
    database="crud_app"
)
cursor = db.cursor()
print("Connected to MySQL database!")

# ----------------------------
# CRUD Functions
# ----------------------------

def create_user(name, email):
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(query, values)
    db.commit()
    print("✅ User added successfully!")

def read_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print("\n📄 All Users:")
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

def update_user(user_id, name, email):
    query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    values = (name, email, user_id)
    cursor.execute(query, values)
    db.commit()
    print("✏️ User updated successfully!")

def delete_user(user_id):
    query = "DELETE FROM users WHERE id = %s"
    value = (user_id,)
    cursor.execute(query, value)
    db.commit()
    print("🗑️ User deleted successfully!")

# ----------------------------
# Menu Loop
# ----------------------------

while True:
    print("\n========== User Management ==========")
    print("1. Add User")
    print("2. Show All Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    print("=====================================")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        email = input("Enter email: ")
        create_user(name, email)

    elif choice == '2':
        read_users()

    elif choice == '3':
        user_id = input("Enter user ID to update: ")
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        update_user(user_id, name, email)

    elif choice == '4':
        user_id = input("Enter user ID to delete: ")
        delete_user(user_id)

    elif choice == '5':
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 5.")
