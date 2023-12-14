from UTIL.DbConnection import DBConnection
from UTIL.propertyUtil import PropertyUtil


class doctor(DBConnection):
    def __init__(self, doctor_id=None, first_name=None, last_name=None, specialization=None, contact_num=None):
        self.doctor_id = doctor_id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.contact_num = contact_num

    def create_table(self):
        create_query = '''create table if not exists doctor(
        doctor_id int,
        first_name varchar(30),
        last_name varchar(30),
        specialization varchar(30),
        contact_num varchar(10)
        )'''
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(create_query)
        print("Table created successfully")


    def insert_into(self):
        self.doctor_id = int(input("Enter the doctor id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.specialization = input("Enter the specialization: ")
        self.contact_num = input("Enter the contact number: ")

        insert_query = '''insert into doctor(doctor_id, first_name, last_name, specialization, contact_num) values(%s,%s,%s,%s,%s)'''
        data = [(self.doctor_id, self.first_name, self.last_name, self.specialization, self.contact_num)]
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Inserted Successfully")

    def update_table(self):
        self.doctor_id = int(input("Enter the doctor id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.specialization = input("Enter the specialization: ")
        self.contact_num = input("Enter the contact number: ")

        update_query = f'update doctor set first_name=%s, last_name=%s, specialization=%s, contact_num=%s where doctor_id=%s'
        data = [(self.first_name, self.last_name, self.specialization, self.contact_num, self.doctor_id)]
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.executemany(update_query, data)
        DBConnection.connection.commit()
        print("Updated Successfully")

    def delete_table(self):
        self.doctor_id = int(input("Enter the doctor id to delete record: "))
        delete_query = f'delete from doctor where doctor_id={self.doctor_id}'
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Deleted Successfully")

    def select_table(self):
        select_query = 'select * from doctor'
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(select_query)
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        print("Values successfully displayed")