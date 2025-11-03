
import argparse
import pandas as pd
from pathlib import Path

def clean_csv(input_file: str, output_file:str):
    # Read CSV: treat empty strings as NaN
    df = pd.read_csv(input_file,na_values=[""," "])

    # Forward fill down blank rows
    df = df.ffill()

    # Save cleaned CSV
    df.to_csv(output_file,index=False)
    print(f"❤️ Cleaned file written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Fill blank rows in CSV using values from the row above")
    parser.add_argument("--input", required=True, help = "Path to input CSV")
    parser.add_argument("--out", default = "cleaned.csv", help = "Path to output CSV")
    args = parser.parse_args()

    clean_csv(args.input, args.out)

if __name__ == "__main__":
    main()