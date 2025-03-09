# FILE: /OpenAIOps/OpenAIOps/log_ingestion/log_parser.py

import re

def parse_log_line(log_line):
    """
    Parse a single line of log data and extract relevant information.

    Args:
        log_line (str): A line from the log file.

    Returns:
        dict: A dictionary containing extracted log information.
    """
    log_pattern = r'(?P<timestamp>\S+) (?P<level>\S+) (?P<message>.*)'
    match = re.match(log_pattern, log_line)

    if match:
        return match.groupdict()
    else:
        return None

def parse_log_file(file_path):
    """
    Parse a log file and extract relevant information from each line.

    Args:
        file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries containing extracted log information.
    """
    parsed_logs = []

    with open(file_path, 'r') as file:
        for line in file:
            parsed_line = parse_log_line(line.strip())
            if parsed_line:
                parsed_logs.append(parsed_line)

    return parsed_logs