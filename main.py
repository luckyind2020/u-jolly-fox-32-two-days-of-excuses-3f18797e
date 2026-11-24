"""Two Days of Excuses — entry runner.

Reads the one-line excuse from entry.txt beside this file and writes it
to /output/entry.txt, the path the sealed scorer reads.
"""

from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    line = (here / "entry.txt").read_text(encoding="utf-8").strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(line)}")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
