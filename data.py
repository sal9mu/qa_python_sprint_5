import pytest
import random
import string


class DataHelper:
    @staticmethod
    def generate_name() -> str:
        name_length = random.randint(3, 8)
        name = ''.join(
            random.choice(string.ascii_letters)
            for _ in range(name_length)
        )
        return name

    @staticmethod
    def generate_login() -> str:
        login_length = random.randint(3, 10)
        login = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(login_length)
        )
        domains = ['ya.ru', 'gmail.com', 'mail.ru', 'yandex.ru']
        domain = random.choice(domains)
        return f'{login}@{domain}'.lower()

    @staticmethod
    def generate_password(min_lenght=6, max_lenght=12) -> str:
        lengt = random.randint(min_lenght, max_lenght)
        characters = string.ascii_letters + string.digits
        password = ''.join(
            random.choice(characters)
            for _ in range(lengt)
        )
        return password


class UserData:
    name = 'Павел'
    email = 'pavel_bazhenov_123@ya.ru'
    password = '1q2w3e4r'
    incorrect_password = '1qaz'