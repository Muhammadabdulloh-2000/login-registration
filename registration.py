import os


class User:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
        self.repeat_password = None
        # self.registration()
        # self.login()

    def choose(self):
        self.clear_console()
        print("""
        Tizimga kirish:
        1. SignUp
        2. SignIn
        """)
        choose = input("Tanlovni kiriting [1/2]: ").strip()
        while choose == "" or choose not in ["1", "2"]:
            self.clear_console()
            print("Kiritishda qandaydur hatolik bor! iltmos takror kiriting")
            choose = input("Tanlovni kiriting [1/2]: ").strip()
        if choose == "1":
            self.registration()

        elif choose == "2":
            self.login()

    def registration(self):
        self.clear_console()
        print("Bu registratsiya qismi")
        input_email = input("Emailingizni kiriting: ").strip()
        input_password = input("Passwordingizni kiriting: ").strip()
        input_repeat_password = input("Passwordni takrorlang: ").strip()
        while input_password != input_repeat_password or input_password == "" or input_repeat_password == "":
            self.clear_console()
            input_password = input("Passwordingizni kiriting: ").strip()
            input_repeat_password = input("Passwordni takrorlang: ").strip()

        print("Ro'yxatdan muvoffaqiyatli o'tdingiz")
        """
        Bu ma'lumotlarni mysql ga ya'ni date base ga yozib qo'yishimiz kerak
        """


    def login(self):
        self.clear_console()
        print("Bu login qismi yani signin")

    @staticmethod
    def clear_console():
        os.system("clear")


user = User()
user.choose()