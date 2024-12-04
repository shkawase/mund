import argparse
import json
import csv
import argparse
from validator import make_validator
from generate_ncr import generate_ncr
from helper import element_helper


def generate_ncr_from_csv(csvfilepath: str, options):
    json_out = []
    with open(csvfilepath) as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            row.pop("")
            if "Z" in row:
                row["element"] = element_helper(int(row.pop("Z")))
            row["mass"] = int(row["mass"])
            row["isomer"] = int(row["isomer"])
            row["lifetime"] = float(row["lifetime"])
            row["uncertainty"] = float(row["uncertainty"])
            json_row = generate_ncr(**(options | row))
            json_row["datasetId"] += f"/{i}"
            json_out.append(json_row)
    return json_out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=str, help="path to the input csv file.")
    parser.add_argument(
        "--dataset-id",
        type=str,
        default="",
        help="default datasetId in data.schema.json.",
    )
    parser.add_argument(
        "--bib-id", type=str, default="", help="[str] default bibId in data.schema.json"
    )
    parser.add_argument(
        "--comment",
        type=str,
        default="",
        help="[str] default comment in data.schema.json",
    )
    parser.add_argument(
        "--dataset-type",
        type=str,
        help='[str] default datasetType in data.schema.json. Options are: ["experiment", "theory", "evaluation"]',
    )
    parser.add_argument(
        "--experimental-condition-id",
        type=str,
        default="",
        help="[str] default experimentalConditionId in data.schema.json",
    )
    parser.add_argument(
        "--element", type=str, help="[str] default element in nuclide.schema.json"
    )
    parser.add_argument(
        "--mass", type=int, default=0, help="[int] default mass in nuclide.schema.json"
    )
    parser.add_argument(
        "--isomer",
        type=int,
        default=0,
        help="[int] default isomer in nuclide.schema.json",
    )
    parser.add_argument(
        "--unit",
        type=str,
        default="us",
        help="[str] default unit in lifetime.schema.json",
    )
    parser.add_argument(
        "--uncertainty_source",
        type=str,
        default="total",
        help='[str] default source in uncertainty.schema.json. Options are: ["total", "statistical", "systematic", "other"]',
    )
    parser.add_argument(
        "--uncertainty_description",
        type=str,
        default="",
        help="[str] default description in uncertainty.schema.json",
    )

    options = vars(parser.parse_args())
    print(
        json.dumps(generate_ncr_from_csv(options.pop("input_csv"), options), indent=2)
    )
