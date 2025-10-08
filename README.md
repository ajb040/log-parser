# Log Parser

A Python-based log parser for Apache/Nginx access logs that extracts security-relevant information.

## Features
- Extracts IP addresses, timestamps, HTTP methods, status codes, and request paths
- Supports JSON and CSV output formats
- Command-line interface for easy automation
- Handles malformed log lines gracefully

## Usage
```bash
python log_parser.py <input_log> <output_file>