import django
import os
import random
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentproject.settings')
django.setup()

from testapp.models import User, Student
faker = Faker()

# Create Admin Users
for i in range(2):
    user, created = User.objects.get_or_create(
        username=f"admin{i}",
        defaults={"password": "123", "role": "admin"}
    )

branches = ["CSE", "ECE", "EEE", "MECH", "CIVIL"]
gender_list = ["MALE", "FEMALE", "OTHER"]

def populate(n):
    existing_records=User.objects.filter(role="student").count()
    for i in range(existing_records,existing_records+n):
        user, created = User.objects.get_or_create(
            username=f"student{i}",
            defaults={"password": "111", "role": "student"}
        )

        Student.objects.get_or_create(
            user=user,
                roll_number= f"R{i+1}",
                name= faker.name(),
                father_name= faker.name_male(),
                branch= random.choice(branches),
                year= random.randint(1,4),
                attendance= random.randint(50,100),
                fees= random.randint(20000,60000),
                gender= random.choice(gender_list),
                fee_payment=random.choice(["PAID","NOT PAID"])

        )

n = int(input("Enter the number of records to be inserted: "))
populate(n)
