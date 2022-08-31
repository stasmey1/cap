import random
import datetime


class Password:
    __password = None
    __time_count = datetime.datetime.now()

    def __init__(self):
        self.date_create = datetime.datetime.now().date()
        self.__password = self.generate_password()

    def generate_password(self):
        if not self.__password:
            smal = [chr(i) for i in range(ord('a'), ord('z') + 1)]
            big = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
            digits = [i for i in range(1, 10)]
            password = [str(random.choice(random.choice([smal, big, digits]))) for i in range(random.randint(8, 10))]
            return ''.join(password)
        return self.__password

    def get_password(self):
        counter = 3
        while True:
            if input('введите код\n') == '0000':
                return self.__password
            else:
                counter -= 1
                if not counter:
                    print('попыток не осталось, ждите 10 сек и повторите запрос')
                    break
                else:
                    print(f'еще, осталось попыток - {counter}')


p1 = Password()
p2 = Password()
print(p1.get_password())
