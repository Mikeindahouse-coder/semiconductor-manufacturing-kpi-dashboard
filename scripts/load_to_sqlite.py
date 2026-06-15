from pathlib import Path
import sqlite3
import pandas as pd


def main():

    project_root = Path(__file__).resolve().parent.parent

    csv_file = (
        project_root
        / "data"
        / "raw"
        / "simulated_fab_data.csv"
    )

    db_dir = (
        project_root
        / "data"
        / "processed"
    )

    db_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    db_file = db_dir / "analytics_fab.db"

    df = pd.read_csv(csv_file)

    conn = sqlite3.connect(db_file)

    df.to_sql(
        "fab_data",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("=" * 60)
    print("SQLite Database Created")
    print("=" * 60)
    print(f"Rows Loaded: {len(df):,}")
    print(f"Database: {db_file}")
    print("Table: fab_data")
    print("=" * 60)


if __name__ == "__main__":
    main()