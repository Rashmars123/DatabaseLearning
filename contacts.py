import sqlite3

db = sqlite3.connect("contacts.sqlite") # Creates the contacts sqlite database
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall()) # get all the data in the database in a list

print(cursor.fetchone()) # Return the next item in a row
print(cursor.fetchone())
print(cursor.fetchone()) # Returns none because there is not a third Item

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()

db.commit()
db.close()
