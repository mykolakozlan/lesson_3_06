MAX_STUDENTS_NUM = ("Max number of students reached", 400)


class MaxStudentsReachedError(Exception):
    def __init__(self, message=MAX_STUDENTS_NUM):
        self.message = message
        super().__init__(self.message)
