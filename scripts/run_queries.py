from pathlib import Path
import sqlite3
import pandas as pd


def main():
    project_root = Path(__file__).resolve().parent.parent

    db_file = project_root / "data" / "processed" / "analytics_fab.db"
    sql_dir = project_root / "sql"
    output_dir = project_root / "data" / "processed" / "query_results"

    output_dir.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_file)

    for sql_file in sorted(sql_dir.glob("*.sql")):
        query = sql_file.read_text(encoding="utf-8")

        df = pd.read_sql_query(query, conn)

        output_file = output_dir / f"{sql_file.stem}.csv"

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

    conn.close()


if __name__ == "__main__":
    main()