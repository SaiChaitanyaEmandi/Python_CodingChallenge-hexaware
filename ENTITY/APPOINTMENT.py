from UTIL.DbConnection import DBConnection
from UTIL.propertyUtil import PropertyUtil


class appointment(DBConnection):
    def __init__(self, appointment_id=None, patient_id=None, doctor_id=None, appointment_date=None, description=None):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.description = description

    def create_table(self):
        create_query = '''create table if not exists appointment(
        appointment_id int,
        patient_id int,
        doctor_id int,
        appointment_date varchar(30),
        description varchar(100)
        )'''
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(create_query)
        print("Table created successfully")

    def insert_into(self):
        self.appointment_id = int(input("Enter the appointment id: "))
        self.doctor_id = int(input("Enter the doctor id: "))
        self.patient_id = int(input("Enter the patient id: "))
        self.appointment_date = input("Enter the appointment date: ")
        self.description = input("Enter the description: ")

        insert_query = '''insert into appointment(appointment_id, doctor_id, patient_id, appointment_date, description) values(%s,%s,%s,%s,%s)'''
        data = [(self.appointment_id, self.doctor_id, self.patient_id, self.appointment_date, self.description)]
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Inserted Successfully")

    def update_table(self):
        self.appointment_id = int(input("Enter the appointment id: "))
        self.doctor_id = int(input("Enter the doctor id: "))
        self.patient_id = int(input("Enter the patient id: "))
        self.appointment_date = input("Enter the appointment date: ")
        self.description = input("Enter the description: ")

        update_query = f'update appointment set doctor_id=%s, patient_id=%s, appointment_date=%s, description=%s where appointment_id=%s'
        data = [(self.doctor_id, self.patient_id, self.appointment_date, self.description, self.appointment_id)]
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.executemany(update_query, data)
        DBConnection.connection.commit()
        print("Updated Successfully")

    def delete_table(self):
        self.appointment_id = int(input("Enter the appointment id to delete record: "))
        delete_query = f'delete from appointment where appointment_id={self.appointment_id}'
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Deleted Successfully")

    def select_table(self):
        select_query = 'select * from appointment'
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(select_query)
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        print("Values successfully displayed")