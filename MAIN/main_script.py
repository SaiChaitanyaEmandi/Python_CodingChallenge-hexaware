from ENTITY.PATIENT import patient
from ENTITY.DOCTOR import doctor
from ENTITY.APPOINTMENT import appointment
from DAO.HOSPITAL_SERVICE import hospitalService
from UTIL.DbConnection import DBConnection
from UTIL.propertyUtil import PropertyUtil
from mysql.connector import Error
from EXCEPTION.PATIENT_ID_NOT_FOUND import invalidPatientIdException

# Example usage
try:
    connObj = DBConnection()
    con = connObj.getConnection()

    patientObj = patient()
    patientObj.select_table()

    doctorObj = doctor()
    doctorObj.select_table()

    appointmentObj = appointment()
    appointmentObj.select_table()

except invalidPatientIdException as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Unhandled error: {e}")

finally:
    DBConnection.connection.close()
    print("Connection closed")
