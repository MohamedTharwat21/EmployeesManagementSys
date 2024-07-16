import sqlite3 

class Database:
    def __init__(self, db):

        # self refers to the current employee to 
        # be stored 

        # to connect to the DB
        self.con = sqlite3.connect (db)

        # to pass anything to the DB

        self.cur = self.con.cursor()

        # QUERY
        # create table called employees
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
            id Integer Primary Key,
            name text,
            age text,
            job text,
            email text,
            gender text,
            mobile text ,
            address text
        )
        """

        # create the table
        self.cur.execute(sql)
        # make sure to connect 
        self.con.commit()




    def insert (self, name, age, job, email, gender, mobile, address): 
        self.cur.execute( "insert into employees values (NULL,?, ? ,?, ? ,?, ?,? ) "
                         , (name, age, job, email, gender, mobile, address) )
        self.con.commit()


    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        # to return all the values of the table
        rows = self.cur.fetchall()
        return rows


    def remove(self , id):
        self.cur.execute("delete from employees where id=?", (id,) )
        self.con.commit()



    def update(self,id, name, age, job, email, gender, mobile, address) : 
        self.cur.execute("update employees set name=?, age=?, job=? , job=? , email=? , gender=? , mobile=? , address=?  where id=?" 
                         ,(name, age, job, email, gender, mobile, address , id) )
        self.con.commit()