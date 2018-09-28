class MyErr(Exception):
    pass

class CanNotAddErr(MyErr):

    def __init__(self, err_msg: str):
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg
