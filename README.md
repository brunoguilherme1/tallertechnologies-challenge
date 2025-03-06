# tallertechnologies-challenge
# LogError: Log Parsing and Analysis

## Description

This Python script reads and processes log files, extracting key information such as log types, AI agent responses, and errors. It then summarizes the data and displays the most frequent AI responses and error messages.

## Code Overview

The `LogError` class handles log processing with the following methods:

- **`read_logs()`**: Reads logs from a file and stores them in a list.
- **`parse_logs()`**: Splits log entries, extracting log type, AI responses, and errors.
- **`log_summary(parsed_logs)`**: Counts and displays the number of `INFO`, `ERROR`, and `WARNING` messages.
- **`top_3_msg(parsed_logs)`**: Finds and prints the top three most common AI responses.
- **`top_error(parsed_logs)`**: Identifies and prints the three most common error messages.
- **`process_logs()`**: Runs all methods sequentially for a complete analysis.

## How to Run

1. Save the logs in a text file, e.g., `logfile.txt`, in the following format:

