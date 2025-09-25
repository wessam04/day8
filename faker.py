from faker import Faker
import csv

fake = Faker()

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Job"])
    for _ in range(10):
        writer.writerow([fake.name(), fake.email(), fake.job()])