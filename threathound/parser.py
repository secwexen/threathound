import numpy as np

class LogParser:
    def __init__(self, max_lines=50000):
        self.max_lines = max_lines

    def parse(self, file_path):
        raw_lines = []
        features = []

        try:
            with open(file_path, "r", errors="ignore") as f:
                for idx, line in enumerate(f):
                    if idx >= self.max_lines:
                        break

                    clean = line.strip()
                    if not clean:
                        continue

                    raw_lines.append(clean)
                    features.append(self._extract_features(clean))

        except FileNotFoundError:
            print(f"[-] Log file not found: {file_path}")
            return np.array([]), []

        return np.array(features), raw_lines

    def _extract_features(self, line):
        length = len(line)
        digit_count = sum(c.isdigit() for c in line)
        special_count = sum(not c.isalnum() and not c.isspace() for c in line)

        return [length, digit_count, special_count]
