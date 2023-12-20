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

    while True:
        patientObj = patient()
        doctorObj = doctor()
        appointmentObj = appointment()
        hospitalServiceObj = hospitalServiceImpl()

        print("Select table to use functionalities")
        print("1.Patient\n2.Doctor\n3.Appointment\n4.Hospital Service Implementation\n5.exit")
        ch = int(input("enter your choice:"))

        if ch == 1:
            while True:
                print(
                    "1.create Patient\t2.insert Patient\t3.update Patient\n4.delete Patient\t5.select Patient\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    patientObj.create_table()
                elif choice == 2:
                    patientObj.insert_into()
                elif choice == 3:
                    patientObj.update_table()
                elif choice == 4:
                    patientObj.delete_table()
                elif choice == 5:
                    patientObj.select_table()
                elif choice == 6:
                    print("exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 2:
            while True:
                print(
                    "1.create Doctor\t2.insert doctor\t3.update doctor\n4.delete doctor\t5.select doctor\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    doctorObj.create_table()
                elif choice == 2:
                    doctorObj.insert_into()
                elif choice == 3:
                    doctorObj.update_table()
                elif choice == 4:
                    doctorObj.delete_table()
                elif choice == 5:
                    doctorObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 3:
            while True:
                print("1.create appointment\t2.insert appointment\t3.update appointment\n4.delete appointment\t5.select appointment\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    appointmentObj.create_table()
                elif choice == 2:
                    appointmentObj.insert_into()
                elif choice == 3:
                    appointmentObj.update_table()
                elif choice == 4:
                    appointmentObj.delete_table()
                elif choice == 5:
                    appointmentObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 4:
            while True:
                print(
                    "1.create hospital service impl\t2.insert hospital service impl\t3.update hospital service impl\n4.delete hospital service impl\t5.select hospital service impl\n6.Exit")
                choice = int(input("enter your choice:"))
                if choice == 1:
                    hospitalServiceObj.create_table()
                elif choice == 2:
                    hospitalServiceObj.insert_into()
                elif choice == 3:
                    hospitalServiceObj.update_table()
                elif choice == 4:
                    hospitalServiceObj.delete_table()
                elif choice == 5:
                    hospitalServiceObj.select_table()
                elif choice == 6:
                    print("Exited successfully")
                    break
                else:
                    print("Wrong choice")

        elif ch == 5:
            print("Exited successfully")
            break

        else:
            print("Wrong choice")


except invalidPatientIdException as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Unhandled error: {e}")

finally:
    DBConnection.connection.close()
    print("Connection closed")
