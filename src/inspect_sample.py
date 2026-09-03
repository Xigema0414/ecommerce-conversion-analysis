"""读取少量原始数据，检查字段、类型和缺失情况。"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "2019-Oct.csv"
SAMPLE_ROWS = 100_000


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"找不到原始数据：{DATA_PATH}")

    data = pd.read_csv(DATA_PATH, nrows=SAMPLE_ROWS)

    print(f"数据文件：{DATA_PATH}")
    print(f"本次读取：{len(data):,} 行，{data.shape[1]} 列")
    print("\n字段名称：")
    print(data.columns.tolist())
    print("\n前 5 行：")
    print(data.head())
    print("\n字段类型：")
    print(data.dtypes)
    print("\n缺失值数量：")
    print(data.isna().sum().sort_values(ascending=False))
    print("\nevent_type 分布：")
    print(data["event_type"].value_counts(dropna=False))


if __name__ == "__main__":
    main()
