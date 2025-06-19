import random
import string

def generate_registration_data():
    email_length = random(5, 7)
    email = ''.join(random.choice(string.ascii_lowercase + string.digits, k=email_length)) + '@ya.ru'
    
    password_length = random(6, 8)
    password = ''.join(random.choice(string.ascii_lowercase + string.digits, k=password_length))
    return email, password  # Возвращаем кортеж (email, password)