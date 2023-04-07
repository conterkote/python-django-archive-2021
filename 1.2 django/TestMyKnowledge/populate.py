import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestMyKnowledge.settings")

import django
django.setup()

from faker import Faker
import random
from MyMeny.models import AccessRecord, Topic, Webpage
# FAKEPOP SCRIPT START
fakegen = Faker()
topics = ["Games", "News", "Entertainment", "Travel", "Social", "Random"]

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 6):
    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        webpg = Webpage.objects.get_or_create(name = fake_name, url = fake_url, topic = top)[0]

        accrec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == "__main__":
    print("populating script is been running!")
    populate(10)
    print("populating has been ended")
