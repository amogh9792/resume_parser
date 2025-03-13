import csv
import os

def export_to_csv(data):
    """Export parsed resume data to CSV file."""
    file_exists = os.path.isfile("parsed_resumes.csv")
    with open("parsed_resumes.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
