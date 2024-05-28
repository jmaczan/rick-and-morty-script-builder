import argparse
import csv


def transform_csv_to_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        lines = []
        for row in reader:
            line_text = row["line"].strip('"')
            formatted_line = f"{row['name']}:\n{line_text}\n\n"
            lines.append(formatted_line)

    with open(output_file, "w", encoding="utf-8") as textfile:
        textfile.writelines(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Transform a CSV file into a single text file."
    )
    parser.add_argument("input", type=str, help="Path to the input CSV file")
    parser.add_argument("output", type=str, help="Path to the output text file")
    args = parser.parse_args()

    transform_csv_to_text(args.input, args.output)
