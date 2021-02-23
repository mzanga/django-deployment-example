# config the settings for the project
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstProject.settings')

import django
django.setup()

# fake population script
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=20):
    for _ in range(N):
        # create fake data for entry
        fake_fn = fakegen.first_name()
        fake_ln = fakegen.last_name()
        fake_email = fakegen.email()

        entry = User.objects.get_or_create(first_name=fake_fn,
                                            last_name=fake_ln,
                                            email_address=fake_email)

if __name__ == "__main__":
    print("populating the database")
    populate(20)
    print("database is populated")
