import argparse
from tools.config import load_config
from tools.beam_design import BeamInput
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Civil Engineering Calculator")
    parser.add_argument("--input", required=True, help="YAML config path")
    args = parser.parse_args()

    cfg = load_config(args.input)
    b = cfg["beam"]

    inp = BeamInput(**b)
    result = design_beam(inp)

    # create dataframe result
    df = pd.DataFrame({
        "Parameter": ["Required As (mm²)"],
        "Value": [result.As_req]
    })

    # save output file
    output_file = "outputs/beam_output.xlsx"
    df.to_excel(output_file, index=False)

    print(f"✅ Calculation complete. Output saved to {output_file}")

if __name__ == "__main__":
    main()
