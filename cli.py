import argparse
import json
from threathound.parser import LogParser
from threathound.detector import AnomalyDetector
from threathound.report import ReportBuilder


def main():
    parser = argparse.ArgumentParser(
        description="ThreatHound - ML-powered log anomaly detection tool"
    )

    parser.add_argument(
        "--log",
        required=True,
        help="Path to the log file to analyze"
    )

    parser.add_argument(
        "--output",
        required=False,
        help="Path to save the JSON report (optional)"
    )

    parser.add_argument(
        "--contamination",
        type=float,
        default=0.05,
        help="Expected proportion of anomalies (default: 0.05)"
    )

    parser.add_argument(
        "--max-lines",
        type=int,
        default=50000,
        help="Maximum number of log lines to process (default: 50000)"
    )

    args = parser.parse_args()

    print("[+] Loading log file...")
    parser_engine = LogParser(max_lines=args.max_lines)
    features, raw_lines = parser_engine.parse(args.log)

    if features.size == 0:
        print("[-] No valid log entries found. Exiting.")
        return

    print("[+] Training anomaly detection model...")
    detector = AnomalyDetector(contamination=args.contamination)
    detector.train(features)

    print("[+] Detecting anomalies...")
    predictions = detector.detect(features)

    print("[+] Building report...")
    report = ReportBuilder.build(raw_lines, predictions)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(report, f, indent=4)
        print(f"[+] Report saved to {args.output}")
    else:
        print(json.dumps(report, indent=4))

    print("[+] Analysis complete.")


if __name__ == "__main__":
    main()
