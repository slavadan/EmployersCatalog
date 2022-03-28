from django_seed import Seed
from .models import Employee
from django.contrib.auth.models import User


seeder = Seed.seeder()

seeder.add_entity(User, 5)
seeder.add_entity(Employee, 5)

seeder.execute()
