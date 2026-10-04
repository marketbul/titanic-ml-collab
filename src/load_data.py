import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


if __name__ == "__main__":
    df = load_data("data/raw/titanic.csv")
    print(df.head())
    print(f"Rows: {len(df)}")
