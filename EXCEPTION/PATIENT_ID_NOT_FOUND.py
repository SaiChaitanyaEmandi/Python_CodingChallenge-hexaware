class invalidPatientIdException(Exception):
    def __init__(self, msg="Patient id should be an positive integer value"):
        self.msg = msg
        super().__init__(msg)
