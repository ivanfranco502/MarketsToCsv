import json
import csv
import sys

def process_json_to_csv(json_file_path, output_file_path='output.csv'):
    # Load the JSON data
    with open(json_file_path) as f:
        data = json.load(f)

    # Open the CSV file for writing
    with open(output_file_path, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the header row
        writer.writerow(["MarketName, MarketCName, GroupCName, TypeCName"])

        for market in data['markets']:
             # Write the row to the CSV file
            writer.writerow([market['marketName'], market['marketCName'], market['groupCName'], market['typeCName']])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python json2csv.py <json_file_path> [output_file_path]")
        sys.exit(1)

    json_file_path = sys.argv[1]
    output_file_path = 'output.csv' if len(sys.argv) < 3 else sys.argv[2]

    process_json_to_csv(json_file_path, output_file_path)
