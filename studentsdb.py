import sqlite3

class Database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("students.db", check_same_thread=False)
        self.curr = self.conn.cursor()
        self.create_db()
    
    def create_db(self):
        sql = '''CREATE TABLE if not exists students (
	            id	INTEGER NOT NULL,
	            name	TEXT,
	            surname	TEXT,
	            math	INTEGER DEFAULT 0,
	            history	INTEGER DEFAULT 0,
	            html	INTEGER DEFAULT 0,
	            PRIMARY KEY(id)
            )'''
        self.curr.execute(sql)
        self.conn.commit()

    def register_st(self, name, surname):
        self.curr.execute(f'insert into students(name, surname) values (?,?)', (name, surname))
        self.conn.commit()

    def update_students(self, student_id, name, surname, math, history, html):
        self.curr.execute(f'Update students set name= "{name}", surname= "{surname}", math = {math}, history = {history}, html = {html} where id = {student_id}')
        self.conn.commit()
    
    def delete_student(self, student_id):
        self.curr.execute(f'''DELETE FROM students where id = {student_id}''')
        self.conn.commit()
          
    def select_user_for_update(self, st_id):
        self.curr.execute(f'SELECT * FROM students WHERE id = {st_id}')
        return self.curr.fetchall()

    def select(self):
        self.curr.execute('''Select * from students''')
        return self.curr.fetchall()

