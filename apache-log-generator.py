"""
Apache Log Generator - Apache Access Log Mock Generation
Randomly selects aspects of an Apache access log to create fake logs

Usage: python apache-log-generator <output_file>
Author: Andrew Bond
"""

from datetime import datetime, timedelta
from faker import Faker
import random
import sys

if len(sys.argv) != 2:
    print("Usage: python apcache-log-generator.py <output file>")
    sys.exit(1)

output_file = sys.argv[1]

if output_file.endswith('.log'):
    pass
else:
    print("Error: Output file must be .log")
    sys.exit(1)

fake = Faker()
methods = ["GET", "POST", "PUT", "DELETE"]
endpoints = ["/", "/index.html", "/login", "/dashboard", "/api/data", "/contact"]
status_codes = [200, 404, 500, 403, 301]

with open(output_file,"w") as f:
    for i in range(1000):
        ip = fake.ipv4()
        time = (datetime.now() - timedelta(seconds=random.randint(0,100000))).strftime("%d/%b/%Y:%H:%M:%S -0400")
        method = random.choice(methods)
        endpoint = random.choice(endpoints)
        status = random.choice(status_codes)
        size = random.randint(200,5000)
        line = f'{ip} - - [{time}] "{method} {endpoint} HTTP/1.1" {status} {size}\n'
        f.write(line)

print(f"{output_file} generated")