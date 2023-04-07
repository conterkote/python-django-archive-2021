import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "НАЗВАНИЕ ПРОЕКТА.settings")

import django
django.setup()

from faker import Faker
import random
from НАЗВАНИЕ ПРОЕКТА.models import МОДЕЛИ БАЗЫ ДАННЫХ
# FAKE POP SCRIPT
fakegen = Faker()
topics = ['Search', 'Social', 'Markerplace', 'News']


def add_topic():
    t = ТОПИК.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=значение по умолчанию):

    for entry in range(N):

        # Get the topic for the entry
        top = add_topic()

        # Create the fake data for this entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry

        webpg = НАЗВАНИЕ МОДЕЛИ.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake acces record for that webpage

        acc_rec = НАЗВАНИЕ МОДЕЛИ.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == "__main__":
    print("populating script is been running!")
    populate(20)
    print("populating complete")