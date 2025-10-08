"""
Log Parser - Apache/Nginx Access Log Parser
Extracts security-relevant fields from web server logs and outputs to JSON or CSV.

Usage: python log_parser.py <input_log> <output_file>
Author: Andrew Bond
"""

from datetime import datetime, timedelta
from faker import Faker
import random

fake = Faker()
methods = ["GET", "POST", "PUT", "DELETE"]
endpoints = ["/", "/index.html", "/login", "/dashboard", "/api/data", "/contact"]
status_codes = [200, 404, 500, 403, 301]

with open("access.log","w") as f:
    for i in range(1000):
        ip = fake.ipv4()
        time = (datetime.now() - timedelta(seconds=random.randint(0,100000))).strftime("%d/%b/%Y:%H:%M:%S -0400")
        method = random.choice(methods)
        endpoint = random.choice(endpoints)
        status = random.choice(status_codes)
        size = random.randint(200,5000)
        line = f'{ip} - - [{time}] "{method} {endpoint} HTTP/1.1" {status} {size}\n'
        f.write(line)

print("access.log generated")