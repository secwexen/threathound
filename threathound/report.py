class ReportBuilder:
    @staticmethod
    def build(raw_lines, predictions):
        report = {
            "total_entries": len(raw_lines),
            "anomalies": [],
            "normal": []
        }

        for line, pred in zip(raw_lines, predictions):
            entry = {"log": line}

            if pred == -1:
                report["anomalies"].append(entry)
            else:
                report["normal"].append(entry)

        return report
