import json
import csv


def convert_json_to_csv(json_file, csv_file):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(data[0].keys())
        for row in data:
            csv_writer.writerow(row.values())


convert_json_to_csv("file.json", "convert_json.csv")
