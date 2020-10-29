from kahoot import client
import json
import random
from time import sleep

bot = client()
pin = int(input("Enter Game Pin: "))
count = int(input("Enter number of bots: "))


def joinHandle():
    pass


while count > 0:
    names = json.loads(open('names.json').read())
    name = random.choice(names) + " " + random.choice(names)
    bot.join(pin, name)
    bot.on("joined", joinHandle)
    print("Joined!")
    sleep(0.1)
    count -= 1
    if count == 0:
        break
