import json
import pandas as pd
import numpy as np


def main():

    url = "https://www.data.gouv.fr/fr/datasets/r/dd0de5d9-b5a5-4503-930a-7b08dc0adc7c"
    df = pd.read_csv(url, sep=";", usecols=["jour", "cl_age90", "T"])

    df = (
        df[df.cl_age90 == 0]
        .rename(columns={"jour": "Date", "T": "Daily change in cumulative total"})
        .drop(columns=["cl_age90"])
    )

    df.loc[:, "Country"] = "France"
    df.loc[:, "Units"] = "people tested"
    df.loc[:, "Testing type"] = "PCR only"
    df.loc[:, "Cumulative total"] = np.nan
    df.loc[:, "Source URL"] = "https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/"
    df.loc[:, "Source label"] = "National Public Health Agency"
    df.loc[:, "Notes"] = np.nan

    df.to_csv("automated_sheets/France - people tested.csv", index=False)


if __name__ == '__main__':
    main()
