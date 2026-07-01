from datetime import datetime
import random

with open("activity.txt", "a") as file:
    file.write(f"Update {random.randint(1,100000)} - {datetime.now()}\n")