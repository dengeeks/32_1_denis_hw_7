import sqlite3 as sq


def create_connection(db_name):
    connection = None
    try:
        connection = sq.connect(db_name)
    except sq.Error as e:
        print(e)
    return connection

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sq.Error as e:
        print(e)


def insert_product(conn,product):
    sql = '''INSERT INTO products
    (product_title,price,quantity)
    VALUES (?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sq.Error as e:
        print(e)

def change_quantity_by_id(conn,product):
    sql = '''UPDATE products SET quantity = ?
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,product)
        conn.commit()
    except sq.Error as e:
        print(e)

def change_price_by_id(conn,product):
    sql = '''UPDATE products SET price = ?
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,product)
        conn.commit()
    except sq.Error as e:
        print(e)

def delete_product_by_id(conn,id):
    sql = '''DELETE FROM products
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(id,))
        conn.commit()
    except sq.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        lists = cursor.fetchall()
        for i in lists:
            print(i)
    except sq.Error as e:
        print(e)

def select_cheap_products(conn):
    sql = '''SELECT * FROM products
    WHERE price < 100 AND quantity > 5'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        cheap_prod = cursor.fetchall()
        for i in cheap_prod:
            print(i)
    except sq.Error as e:
        print(e)


def find_product_by_name(conn,product_name):
    sql = '''SELECT * FROM products
        WHERE product_title LIKE  ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(product_name,))
        cheap_prod = cursor.fetchall()
        for i in cheap_prod:
            print(i)
    except sq.Error as e:
        print(e)



sql_create_students_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price FLOAT(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''




connection_to_db = create_connection('hw.db')
if connection_to_db is not None:
    print('Successfully connected to DB!')
    # create_table(connection_to_db, sql_create_students_table)
    # insert_product(connection_to_db,('Apple',50,100))
    # insert_product(connection_to_db,('Pear',120,70))
    # insert_product(connection_to_db,('Orange',200,50))
    # insert_product(connection_to_db,('Watermelon',300,30))
    # insert_product(connection_to_db,('Strawberry',250,200))
    # insert_product(connection_to_db,('Apricot',150,90))
    # insert_product(connection_to_db,('Peach',320,65))
    # insert_product(connection_to_db,('Cucumber',40,150))
    # insert_product(connection_to_db,('Tomato',80,120))
    # insert_product(connection_to_db,('Potato',55,500))
    # insert_product(connection_to_db,('Onion',110,320))
    # insert_product(connection_to_db,('Carrot',50,100))
    # insert_product(connection_to_db,('Cabbage',80,140))
    # insert_product(connection_to_db,('Meat',700,10))
    # insert_product(connection_to_db,('Garlic',40,50))
    # change_quantity_by_id(connection_to_db,(238,2))
    # change_quantity_by_id(connection_to_db,(180,5))
    # change_price_by_id(connection_to_db,(75,1))
    # change_price_by_id(connection_to_db,(48,8))
    # delete_product_by_id(connection_to_db,15)
    # select_all_products(connection_to_db)
    # select_cheap_products(connection_to_db)
    # find_product_by_name(connection_to_db,('Meat'))
    connection_to_db.close()