import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_task.settings")

import django
django.setup()

from faker import Faker
import random
from firstApp.models import AccessRecord, Webpage, Topic
# FAKE POP SCRIPT
fakegen = Faker()
topics = ['Search', 'Social', 'Markerplace', 'News']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=len(topics)):

    for entry in range(N):

        # Get the topic for the entry
        top = add_topic()

        # Create the fake data for this entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake acces record for that webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == "__main__":
    print("populating script is been running!")
    populate(20)
    print("populating complete")