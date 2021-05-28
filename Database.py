import sqlite3 as sql

db_name = "database.db"
str_table_user = "users"
str_table_cars = "cars"


def removeDBfile():
    import os
    if os.path.exists(db_name):
        os.remove(db_name)


def createDB():
    conn = sql.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {str_table_user} " +
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)")
    cur.execute(f"CREATE TABLE IF NOT EXISTS {str_table_cars} " +
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, brand TEXT, model TEXT, owner INTEGER, "
                "FOREIGN KEY (owner) REFERENCES users(id) ON DELETE CASCADE)")
    conn.commit()
    conn.close()
    print("database created")


class table_user:
    def insert(Name, Email):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO {str_table_user} VALUES (NULL,?,?)", (Name, Email))
        conn.commit()
        conn.close()
        print(f"user '{Name}' added")

    def update(Id, Name, Email):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(
            f"UPDATE {str_table_user} SET name=?, email=? WHERE id=?", (Name, Email, Id))
        conn.commit()
        conn.close()

    def view():
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {str_table_user}")
        rows = cur.fetchall()
        conn.close()
        return rows

    def view(Item):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(f"SELECT {Item} FROM {str_table_user}")
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(id):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {str_table_user} WHERE id=?", (id,))
        cur.execute(f"DELETE FROM {str_table_cars} WHERE owner=?", (id,))
        conn.commit()
        conn.close()


class table_cars:
    def insert(Brand, Model, Owner):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO {str_table_cars} VALUES (NULL,?,?,?)", (Brand, Model, Owner))
        conn.commit()
        conn.close()
        print(f"car: '{Model}' added to user: {Owner}")

    def update(Id, Brand, Model, Owner):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(
            f"UPDATE {str_table_cars} SET brand=?, model=?, owner=? WHERE id=?", (Brand, Model, Owner, Id))
        conn.commit()
        conn.close()

    def view():
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {str_table_cars}")
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(id):
        conn = sql.connect(db_name)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {str_table_cars} WHERE id=?", (id,))
        conn.commit()
        conn.close()
