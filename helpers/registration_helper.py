import random

class RegistrationHelper:
    @staticmethod
    def generate_test_email():
        """Генерация тестового email"""
        return f'petrashov_danya_20_{random.randint(100,999)}@yandex.ru'
