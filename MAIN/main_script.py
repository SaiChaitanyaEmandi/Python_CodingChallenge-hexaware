from DAO.PATIENT import patient
from DAO.DOCTOR import doctor
from DAO.APPOINTMENT import appointment
from DAO.HOSPITAL_SERVICE_IMPL import hospitalServiceImpl
from UTIL.propertyUtil import PropertyUtil
from UTIL.DbConnection import DBConnection
from mysql.connector import Error
from EXCEPTION.PATIENT_ID_NOT_FOUND import invalidPatientIdException

# Example usage
try:
    connObj = DBConnection()
    con = connObj.getConnection()

    hospitalServiceObj = hospitalServiceImpl()
    appointmentId = int(input("Enter id to get appointments: "))
    hospitalServiceObj.getAppointmentById(appointmentId)

    patientId = int(input("Enter patient id to get appointment: "))
    hospitalServiceObj.getAppointmentsForPatient(patientId)

    # patientObj = patient()
    # patientObj.select_table()
    #
    # doctorObj = doctor()
    # doctorObj.select_table()
    #
    # appointmentObj = appointment()
    # appointmentObj.select_table()

except invalidPatientIdException as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Unhandled error: {e}")

finally:
    DBConnection.connection.close()
    print("Connection closed")
