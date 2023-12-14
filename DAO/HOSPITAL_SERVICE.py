from UTIL.DbConnection import DBConnection
from ENTITY.PATIENT import patient
from ENTITY.DOCTOR import doctor
from ENTITY.APPOINTMENT import appointment


class hospitalService(appointment, doctor, patient, DBConnection):
    def get_appointment_by_id(self, appointment_id):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        DBConnection.connection.cursor()
        select_appointment_query = "SELECT * FROM appointment WHERE appointment_id = %s"
        self.stmt.execute(select_appointment_query, (appointment_id,))
        data = self.stmt.fetchall()
        for i in data:
            print(i)

    def get_appointments_for_patients(self, patient_id):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        DBConnection.connection.cursor()
        select_patients_query = f'select * from appointment where patient_id={patient_id}'
        self.stmt.execute(select_patients_query)
        data = self.stmt.fetchall()
        for i in data:
            print(i)

    def get_appointments_for_doctors(self, doctor_id):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        DBConnection.connection.cursor()
        select_doctor_query = f'select * from appointment where doctor_id={doctor_id}'
        self.stmt.execute(select_doctor_query)
        data = self.stmt.fetchall()
        for i in data:
            print(i)

    def schedule_appointment(self):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.insert_into()

    def update_appointment(self):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.update_table()

    def cancel_appointment(self):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.delete_table()
