from collections import Counter
import numpy as np

class LogError:
    def __init__(self, path):
        self.path = path
        self.list_logs = []

    def read_logs(self):
        logs = open(self.path)
        self.list_logs = []
        for lines in logs.readlines():
            self.list_logs.append(lines)

    def parse_logs(self):
        parsed_logs = []

        for log in self.list_logs:
            aux = []
            array = log.split(" ")
            aux.append(array[2])
            if aux[0] == "ERROR":
                aux.append(" ".join(array[4:]))
                aux.append("null")
            else:
                aux.append("null")
                agent = log.split("Agent Response: ")
                aux.append(agent[1])

            parsed_logs.append(aux)

        return np.array(parsed_logs)

    def log_summary(self, parsed_logs):
        d_msg = Counter(parsed_logs[:, 0])
        print("\nLog Summary:")
        for key in ["INFO", "ERROR", "WARNING"]:
            print(f"- {key} messages: {d_msg.get(key, 0)}")

    def top_3_msg(self, parsed_logs):
        d_msg = Counter(parsed_logs[:, 2]).most_common(3)
        print("\nTop 3 AI Responses:")
        for i, (response, count) in enumerate(d_msg, start=1):
            if response == "null":
                continue
            print(f"{i}. \"{response}\" ({count} times)")

    def top_error(self, parsed_logs):
        d_msg = Counter(parsed_logs[:, 1]).most_common(3)
        print("\nMost Common Errors:")
        for i, (error, count) in enumerate(d_msg, start=1):
            if error == "null":
                continue
            print(f"{i}. {error} ({count} times)")

    def process_logs(self):
        self.read_logs()
        parsed_logs = self.parse_logs()
        self.log_summary(parsed_logs)
        self.top_3_msg(parsed_logs)
        self.top_error(parsed_logs)

log_parser = LogError("logfile.txt")
log_parser.process_logs()
