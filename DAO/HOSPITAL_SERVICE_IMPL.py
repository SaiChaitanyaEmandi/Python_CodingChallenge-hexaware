from UTIL.DbConnection import DBConnection
# from DAO.PATIENT import patient
# from DAO.DOCTOR import doctor
from DAO.APPOINTMENT import appointment
from ENTITY.IHOSPITALSERVICE import IHospitalService


class hospitalServiceImpl(IHospitalService, appointment, DBConnection):
    def getAppointmentById(self, appointment_id):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        DBConnection.connection.cursor()
        select_appointment_query = "SELECT * FROM appointment WHERE appointment_id = %s"
        self.stmt.execute(select_appointment_query, (appointment_id,))
        data = self.stmt.fetchall()
        for i in data:
            print(i)

    def getAppointmentsForPatient(self, patient_id):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        DBConnection.connection.cursor()
        select_patients_query = f'select * from appointment where patient_id={patient_id}'
        self.stmt.execute(select_patients_query)
        data = self.stmt.fetchall()
        for i in data:
            print(i)

    def getAppointmentsForDoctor(self, doctor_id):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        DBConnection.connection.cursor()
        select_doctor_query = f'select * from appointment where doctor_id={doctor_id}'
        self.stmt.execute(select_doctor_query)
        data = self.stmt.fetchall()
        for i in data:
            print(i)

    # We are making an appointment. So I have called the insert_into method of appointment class
    def scheduleAppointment(self):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.insert_into()

    # We are updating an appointment. So I have called the update_table method of appointment class.
    #  In that method it takes appointment id as input and updates the requires fields.
    def updateAppointment(self):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.update_table()

    # Cancelling the appointment means deleting. So I have called delete method of appointment class.
    def cancelAppointment(self):
        DBConnection.getConnection()
        self.stmt = DBConnection.connection.cursor()
        self.delete_table()
