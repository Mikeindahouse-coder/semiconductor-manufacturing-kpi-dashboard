from pathlib import Path
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


# Reproducibility
np.random.seed(42)

# Configuration
NUM_LOTS = 3000

PRODUCTS = [
    "N3_CPU",
    "N3_GPU",
    "N3_MOBILE",
    "N3_AI"
]

PROCESS_STEPS = [
    "Lithography",
    "Etching",
    "Deposition",
    "CMP",
    "Metrology",
    "Inspection"
]

EQUIPMENTS = {
    "Lithography": ["LITHO_01", "LITHO_02", "LITHO_03"],
    "Etching": ["ETCH_01", "ETCH_02", "ETCH_03", "ETCH_04"],
    "Deposition": ["DEP_01", "DEP_02", "DEP_03"],
    "CMP": ["CMP_01", "CMP_02"],
    "Metrology": ["MET_01", "MET_02"],
    "Inspection": ["INSP_01", "INSP_02"]
}


def generate_fab_data(num_lots: int) -> pd.DataFrame:
    """
    Generate simulated semiconductor manufacturing data.
    """

    records = []

    start_date = datetime(2026, 1, 1)

    for lot_idx in range(1, num_lots + 1):

        lot_id = f"LOT_{lot_idx:05d}"

        product_id = np.random.choice(PRODUCTS)

        wafer_count = np.random.choice(
            [24, 25],
            p=[0.2, 0.8]
        )

        current_time = start_date + timedelta(
            days=np.random.randint(0, 90),
            hours=np.random.randint(0, 24)
        )

        for step in PROCESS_STEPS:

            equipment_id = np.random.choice(EQUIPMENTS[step])

            queue_time = max(
                0,
                np.random.normal(loc=6, scale=3)
            )

            process_time = max(
                0.5,
                np.random.normal(loc=3, scale=1)
            )

            # Create bottleneck behavior at Etching
            if step == "Etching":
                queue_time *= 1.8
                process_time *= 1.3

            start_time = current_time + timedelta(
                hours=queue_time
            )

            end_time = start_time + timedelta(
                hours=process_time
            )

            defect_count = np.random.poisson(lam=2)

            if step == "Inspection":

                base_yield = np.random.normal(
                    loc=0.94,
                    scale=0.03
                )

                if product_id == "N3_AI":
                    base_yield -= 0.02

                yield_rate = min(
                    max(base_yield, 0.75),
                    0.99
                )

            else:
                yield_rate = None

            status = np.random.choice(
                ["Completed", "Hold", "Rework"],
                p=[0.92, 0.05, 0.03]
            )

            records.append(
                {
                    "lot_id": lot_id,
                    "product_id": product_id,
                    "process_step": step,
                    "equipment_id": equipment_id,
                    "wafer_count": wafer_count,
                    "queue_time_hours": round(queue_time, 2),
                    "process_time_hours": round(process_time, 2),
                    "start_time": start_time,
                    "end_time": end_time,
                    "defect_count": defect_count,
                    "yield_rate": yield_rate,
                    "status": status
                }
            )

            current_time = end_time

    return pd.DataFrame(records)


def main():

    df = generate_fab_data(NUM_LOTS)

    # Project root
    project_root = Path(__file__).resolve().parent.parent

    # data/raw
    raw_dir = project_root / "data" / "raw"

    raw_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = raw_dir / "simulated_fab_data.csv"

    df.to_csv(
        output_file,
        index=False
    )

    print("=" * 60)
    print("Semiconductor Manufacturing Dataset Generated")
    print("=" * 60)
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Saved to: {output_file}")
    print("=" * 60)

    print("\nSample Data:")
    print(df.head())


if __name__ == "__main__":
    main()