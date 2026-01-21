import sys
import pandas as pd


if len(sys.argv) < 2:
    print("Vui lòng nhập month khi chạy script!")
    sys.exit(1)
print("arguments", sys.argv)

month = int(sys.argv[1])


df = pd.DataFrame({"day": [1, 2], "num_passenger":[3, 4]})
df["month"] = month
print(df.head())

df.to_parquet(f"output_month={month}.parquet")
print(f"Hello pipeline month={month}")