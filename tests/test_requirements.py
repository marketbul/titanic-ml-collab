from pathlib import Path


def test_requirements_file_contains_only_dependency_specs():
    requirements_path = Path(__file__).resolve().parents[1] / "requirements.txt"
    lines = [line.strip() for line in requirements_path.read_text().splitlines() if line.strip()]

    assert lines
    assert all("==" in line for line in lines)
