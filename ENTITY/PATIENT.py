from UTIL.DbConnection import DBConnection
from UTIL.propertyUtil import PropertyUtil
from EXCEPTION.PATIENT_ID_NOT_FOUND import invalidPatientIdException


class patient(DBConnection):
    def __init__(self, patient_id=None, first_name=None, last_name=None, dob=None, gender=None, contact_num=None):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.contact_num = contact_num

    def create_table(self):
        create_query = '''create table if not exists patient(
        patient_id int,
        first_name varchar(30),
        last_name varchar(30),
        dob date,
        gender char,
        contact_num varchar(10)
        )'''
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(create_query)
        print("Table created successfully")

    def insert_into(self):
        self.patient_id = int(input("Enter the patient id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.dob = input("Enter the date of birth: ")
        self.gender = input("Enter the gender: ")
        self.contact_num = input("Enter the contact number: ")

        insert_query = '''insert into patient(patient_id, first_name, last_name, dob, gender, contact_num) values(%s,%s,%s,%s,%s,%s)'''
        data = [(self.patient_id, self.first_name, self.last_name, self.dob, self.gender, self.contact_num)]
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Inserted Successfully")

    def update_table(self):
        self.patient_id = int(input("Enter the patient id: "))
        self.first_name = input("Enter the first name: ")
        self.last_name = input("Enter the last name: ")
        self.dob = input("Enter the date of birth: ")
        self.gender = input("Enter the gender: ")
        self.contact_num = input("Enter the contact number: ")

        update_query = f'update patient set first_name=%s, last_name=%s, dob=%s, gender=%s, contact_num=%s where patient_id=%s'
        data = [(self.first_name, self.last_name, self.dob, self.gender, self.contact_num, self.patient_id)]
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.executemany(update_query, data)
        DBConnection.connection.commit()
        print("Updated Successfully")

    def delete_table(self):
        try:
            self.patient_id = int(input("Enter the patient id to delete record: "))
            if not self.patient_exists(self.patient_id):
                raise invalidPatientIdException("Patient number not found")
            delete_query = f'delete from patient where patient_id={self.patient_id}'
            DBConnection.getConnection()
            self.stmt = DBConnection.connection.cursor()
            self.stmt.execute(delete_query)
            DBConnection.connection.commit()
            print("Deleted Successfully")
        except invalidPatientIdException as e:
            print(e)
        except Exception as e:
            print(f"Error: {e}")

    def select_table(self):
        select_query = 'select * from patient'
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.stmt.execute(select_query)
        data = self.stmt.fetchall()
        for i in data:
            print(i)
        print("Values successfully displayed")

    def patient_exists(self, patient_id):
        try:
            DBConnection.getConnection()
            self.stmt = DBConnection.connection.cursor()
            select_query = f'SELECT COUNT(*) FROM patient WHERE patient_id = {patient_id}'
            self.stmt.execute(select_query)
            result = self.stmt.fetchone()
            if result and result[0] > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error checking patient existence: {e}")
            return False
