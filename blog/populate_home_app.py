import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

import django

django.setup()

## FAKE POP SCRIPT
import random
from home.models import AccessRecord, Webpage, Topic
from faker import Faker

fakergen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Seeding Database!")
    populate(20)
    print("Seeding Complate!")
