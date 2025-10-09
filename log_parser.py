"""
Log Parser - Apache/Nginx Access Log Parser
Extracts security-relevant fields from web server logs and outputs to JSON or CSV.

Usage: python log_parser.py <input_log> <output_file>
Author: Andrew Bond
"""
import csv
import json
import re
import sys

if len(sys.argv) != 3:
    print("Usage: python log_parser.py <input_log> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

compiled_ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
compiled_timestamp_pattern = re.compile(r"\[(.*?)\]")
compiled_method_pattern = re.compile(r'"(GET|POST|PUT|DELETE)')
compiled_status_pattern = re.compile(r'"\s(\d{3})\s')
compiled_path_pattern = re.compile(r'"(?:GET|POST|PUT|DELETE)\s(.*?)\sHTTP')
logs = []

with open(input_file, "r") as file:
    for line in file:
        ip_match = compiled_ip_pattern.findall(line)
        timestamp_match = compiled_timestamp_pattern.findall(line)
        method_match = compiled_method_pattern.findall(line)
        status_match = compiled_status_pattern.findall(line)
        path_match = compiled_path_pattern.findall(line)
        line_dict = {
            "ip": ip_match[0] if ip_match else None,
            "timestamp": timestamp_match[0] if timestamp_match else None, 
            "method": method_match[0] if method_match else None, 
            "status": status_match[0] if status_match else None, 
            "path": path_match[0] if path_match else None
        }
        logs.append(line_dict)

if output_file.endswith('.json'):
    with open(output_file, "w") as f:
        json.dump(logs, f, indent = 2)
elif output_file.endswith('.csv'):
    with open(output_file, "w",newline='') as f:
        fieldnames = ['ip','timestamp','method','status','path']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(logs)
else:
    print("Error: Output file must be .json or .csv")
    sys.exit(1)
