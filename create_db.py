import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("""
INSERT INTO students (name, marks)
VALUES
('Arun', 92),
('Priya', 88),
('Kumar', 75),
('Divya', 95),
('Rahul', 65)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
INSERT INTO customers (name, city)
VALUES
('Ravi', 'Chennai'),
('Meena', 'Madurai'),
('Arjun', 'Chennai'),
('Karthik', 'Coimbatore')
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
)
""")

cursor.execute("""
INSERT INTO employees (name, salary)
VALUES
('Raj', 60000),
('Kumar', 45000),
('Priya', 70000),
('Divya', 55000)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    price INTEGER
)
""")

cursor.execute("""
INSERT INTO products (product_name, price)
VALUES
('Laptop', 55000),
('Mouse', 800),
('Keyboard', 1500),
('Monitor', 9000),
('Headphone', 2500)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_name TEXT,
    amount INTEGER
)
""")

cursor.execute("""
INSERT INTO orders (customer_name, amount)
VALUES
('Ravi', 5000),
('Meena', 12000),
('Arjun', 8000)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price INTEGER
)
""")

cursor.execute("""
INSERT INTO books (title, price)
VALUES
('Python Basics', 450),
('SQL Guide', 600),
('AI Fundamentals', 800)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS hospitals (
    id INTEGER PRIMARY KEY,
    hospital_name TEXT,
    city TEXT
)
""")

cursor.execute("""
INSERT INTO hospitals (hospital_name, city)
VALUES
('Apollo', 'Chennai'),
('KMCH', 'Coimbatore'),
('Meenakshi Hospital', 'Madurai')
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    movie_name TEXT,
    rating REAL
)
""")

cursor.execute("""
INSERT INTO movies (movie_name, rating)
VALUES
('Leo', 8.5),
('Jailer', 8.8),
('Vikram', 9.0)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY,
    airline TEXT,
    fare INTEGER
)
""")

cursor.execute("""
INSERT INTO flights (airline, fare)
VALUES
('IndiGo', 4500),
('Air India', 6500),
('SpiceJet', 5200)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS hotels (
    id INTEGER PRIMARY KEY,
    hotel_name TEXT,
    city TEXT
)
""")

cursor.execute("""
INSERT INTO hotels (hotel_name, city)
VALUES
('Taj', 'Chennai'),
('Le Meridien', 'Coimbatore'),
('Grand Palace', 'Madurai')
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    course_name TEXT,
    fee INTEGER
)
""")

cursor.execute("""
INSERT INTO courses (course_name, fee)
VALUES
('Python', 15000),
('Data Science', 30000),
('Machine Learning', 25000)
""")
conn.commit()

conn.close()

print("Database Created Successfully!")