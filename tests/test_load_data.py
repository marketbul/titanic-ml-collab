import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from load_data import load_data


def test_load_data_reads_csv(tmp_path: Path) -> None:
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text("PassengerId,Survived\n1,0\n2,1\n", encoding="utf-8")

    df = load_data(str(csv_path))

    assert list(df.columns) == ["PassengerId", "Survived"]
    assert len(df) == 2
