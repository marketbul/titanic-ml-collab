import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.load_data import load_data


def test_load_data(tmp_path):
    csv_path = tmp_path / "titanic.csv"
    csv_path.write_text("PassengerId,Survived\n1,0\n2,1\n", encoding="utf-8")
    df = load_data(str(csv_path))

    assert len(df) == 2
    assert "Survived" in df.columns
    assert "PassengerId" in df.columns
