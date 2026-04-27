import pandas as pd


def load_sounding_csv(filename):
    """
    Load sounding data from a CSV file.

    The CSV should include:
    temperature, dewpoint, height, pressure

    Parameters
    ----------
    filename : str
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        Sounding data as a DataFrame.
    """
    try:
        data = pd.read_csv(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find this file: {filename}")

    if data.empty:
        raise ValueError("The CSV file is empty.")

    required_columns = ["temperature", "dewpoint", "height"]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing the required column: {column}")

    return data