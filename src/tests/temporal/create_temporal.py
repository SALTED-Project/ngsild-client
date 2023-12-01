import sys
sys.path.append("../../../src")
from ngsildclient.entity import Entity
from ngsildclient.client import Client
import asyncio
import random
import time

import datetime
import random

# Generate a random datetime between two dates
client_obj = Client("10.10.26.101", "9090")
def randam_date():
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime(2023, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

# generate randon number 
def generate_random_number():
    random_number = random.randint(1999, 1000000)
    return random_number

# publish data on scorpio broker

def publish(entity):
    response = client_obj.temporal_create(entity)
    print(response)

async def create_entity():
    entity_obj = Entity("Vehicle", "urn:ngsi-ld:Vehicle:A135")
    random_value = generate_random_number()
    randaom_date = randam_date()
    entity_obj.add_prop("speed", random_value, observedAt=randaom_date)
    publish(entity_obj.to_dict())

async def main():
    for i in range(10):
        t = asyncio.create_task(create_entity())
    await asyncio.gather(t)
    print("Created all entity")

asyncio.run(main())