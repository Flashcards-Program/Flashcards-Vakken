import json
from pathlib import Path

ROOT: Path = Path(__file__).resolve().parents[1]
VAKKEN_DIR: Path = ROOT / "Vakken"
OUTPUT_FILE: Path = ROOT / "index.json"

def load_json(file: Path) -> dict:
    with file.open("r", encoding="utf-8") as f:
        return json.load(f)

def generate_index() -> dict:
    index: dict = {}
    for year_dir in VAKKEN_DIR.iterdir():
        if not year_dir.is_dir():
            continue
        year_key: str = year_dir.name
        index[year_key] = {}

        for program_dir in year_dir.iterdir():
            if not program_dir.is_dir():
                continue
            program_key: str = program_dir.name
            index[year_key][program_key] = {}

            for json_file in program_dir.glob("*.json"):
                subject_key: str = json_file.stem
                index[year_key][program_key][subject_key] = load_json(json_file)

    return index

def main() -> None:
    data: dict = generate_index()
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()