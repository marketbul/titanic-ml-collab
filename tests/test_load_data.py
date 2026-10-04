from src.load_data import load_data


def test_load_data():
    df = load_data("data/raw/titanic.csv")

    assert len(df) == 891
    assert "Survived" in df.columns
    assert "PassengerId" in df.columns
