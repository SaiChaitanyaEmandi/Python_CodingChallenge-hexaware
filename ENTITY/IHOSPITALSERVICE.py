from abc import ABC, abstractmethod


class IHospitalService(ABC):

    @abstractmethod
    def getAppointmentById(self, appointment_id):
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patient_id):
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctor_id):
        pass

    @abstractmethod
    def scheduleAppointment(self):
        pass

    @abstractmethod
    def updateAppointment(self):
        pass

    @abstractmethod
    def cancelAppointment(self):
        pass



