
from pathlib import Path
import pandas as pd

base_folder = (
    Path(__file__).parent)
output_folder = base_folder.parent / "merged_csv"
output_folder.mkdir(parents=True, exist_ok=True)
all_cities = []
failed_files = []


    print(f"\nProcessing: {city_folder.name}")

    for file in files:
        try:
            df = pd.read_csv(
                file,
                encoding="latin1",
                low_memory=False
            )

            df["source_city"] = city_folder.name
            df["source_file"] = file.name

            city_data.append(df)
            print(f"  Read: {file.name} ({len(df)} rows)")

        except Exception as e:
            failed_files.append((file, str(e)))
            print(f"  FAILED: {file.name}: {e}")

    if city_data:
        merged = pd.concat(
            city_data,
            ignore_index=True,
            sort=False
        )

        output_file = (
            output_folder / f"{city_folder.name}_master.csv"
        )
        merged.to_csv(output_file, index=False, encoding="utf-8-sig")

        all_cities.append(merged)

        print(f"  Files read: {len(city_data)}/{len(files)}")
        print(f"  Total rows: {len(merged):,}")
        print(f"  Saved: {output_file.name}")

if all_cities:
    master = pd.concat(
        all_cities,
        ignore_index=True,
        sort=False
    )

    master_file = output_folder / "all_cities_master.csv"
    master.to_csv(master_file, index=False, encoding="utf-8-sig")

    print("\n========== MERGE SUMMARY ==========")
    print("Cities:", master["source_city"].nunique())
    print("Total rows:", f"{len(master):,}")
    print("Total columns:", len(master.columns))
    print("Master file:", master_file)

print("\nFailed files:", len(failed_files))

for file, error in failed_files:
    print(file, error)


