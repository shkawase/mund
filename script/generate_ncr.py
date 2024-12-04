import json
from validator import make_validator


def generate_ncr(
    *,
    dataset_id: str = "0",
    bib_id: str = "0",
    comment: str = "",
    dataset_type: str = "experiment",
    experimental_condition_id: str = "0",
    element: str = "H",
    mass: int = 0,
    isomer: int = 0,
    lifetime: float = None,
    unit: str = "us",
    uncertainty=0,
    uncertainty_source: str = "total",
    uncertainty_description: str = "total uncertainty",
    huff_factor: float = None
):
    entry = {
        "datasetId": dataset_id,
        "bibId": bib_id,
        "comment": comment,
        "datasetType": dataset_type,
        "experimentalConditionId": experimental_condition_id,
        "nuclide": {"element": element, "mass": mass, "isomer": isomer},
        "observable": {
            "kind": "lifetime",
            "lifetime": {
                "value": lifetime,
                "unit": unit,
                "uncertainties": [
                    {
                        "source": uncertainty_source,
                        "value": uncertainty,
                        "description": uncertainty_description,
                    }
                ],
                "huffFactor": huff_factor,
            },
        },
    }

    try:
        make_validator().validate(entry)
    except Exception as e:
        print("Validation failed:", e)
    else:
        return entry


if __name__ == "__main__":
    print(generate_ncr())
