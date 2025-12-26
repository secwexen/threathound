# ThreatHound

ThreatHound is a lightweight, machine learning–powered log anomaly detection tool designed for security analysts and defenders.  
It processes system and application logs, learns normal behavior patterns, and highlights suspicious entries for further investigation.

---

## Features

- **ML-based anomaly detection:** Uses unsupervised learning to detect unusual log patterns.
- **Log parsing layer:** Modular parsers for different log types (e.g., auth logs, web server logs).
- **CLI friendly:** Simple command-line interface for quick analysis.
- **JSON report output:** Easy to integrate with other tools or dashboards.
- **Extensible design:** Add your own parsers and detection rules.

---

## Use cases

- Detecting suspicious SSH login attempts.
- Identifying abnormal access patterns in web server logs.
- Highlighting rare or unexpected system events.
- Supporting incident response and threat hunting workflows.

---

## Project structure

```text
ThreatHound/
├─ .gitignore
├─ LICENSE
├─ README.md
├─ cli.py
├─ requirements.txt
├─ threathound/
   ├─ __init__.py
   ├─ parser.py
   ├─ detector.py
   └── report.py
```

- **`threathound/parser.py`** – Responsible for reading and transforming raw log lines into feature vectors.
- **`threathound/detector.py`** – Contains the anomaly detection logic (e.g., Isolation Forest).
- **`threathound/report.py`** – Generates human-readable and JSON reports.
- **`cli.py`** – Command-line entry point.

---

## Installation

```bash
git clone https://github.com/secwexen/threathound.git
cd threathound

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
# source venv/bin/activate

pip install -r requirements.txt
```

---

## Usage

Run ThreatHound against a log file:

```bash
python cli.py --log /var/log/auth.log --output report.json
```

Example arguments:

- `--log` – Path to the log file to analyze.
- `--output` – Output JSON report path (optional; if omitted, prints a summary to stdout).
- `--contamination` – Expected proportion of anomalies (for the Isolation Forest model).
- `--max-lines` – Limit the number of lines to process from the log file.

Example:

```bash
python cli.py --log /var/log/auth.log --output auth_report.json --contamination 0.03 --max-lines 50000
```

---

## Minimal example detector (concept)

Below is a simplified version of the anomaly detector used in this project:

```python
from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self, contamination=0.05, random_state=42):
        self.model = IsolationForest(
            contamination=contamination,
            random_state=random_state
        )

    def train(self, features: np.ndarray):
        self.model.fit(features)

    def detect(self, features: np.ndarray):
        # Returns 1 for normal, -1 for anomaly
        return self.model.predict(features)
```

---

## Disclaimer

ThreatHound is intended **only** for legitimate security testing, monitoring, and research on systems you own or are explicitly authorized to analyze.  
The author is not responsible for any misuse or illegal activity involving this tool.

---

## Roadmap

- Add more built-in log parsers (NGINX, Apache, Windows event logs).
- Export results to formats like CSV and HTML.
- Optional rules-based layer to complement ML detection.
- Docker image for easier deployment.

---

## License

This project is released under the Apache-2.0 License. See the `LICENSE` file for details.
