import random
import string

def generate_registration_data():
    name_lenght = random(5, 7)
    name = ''.join(random.choice(string.ascii_lowercase, k=name_lenght) + random.choice(string.digits, k=3))

    email_length = random(5, 7)
    email = ''.join(random.choice(string.ascii_lowercase + string.digits, k=email_length)) + '@ya.ru'
    
    password_length = random(6, 8)
    password = ''.join(random.choice(string.ascii_lowercase + string.digits, k=password_length))
    return name, email, password  # Возвращаем кортеж (name, email, password)