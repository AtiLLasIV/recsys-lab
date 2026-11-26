from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "ml-1m"


def load_ratings(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    df = pd.read_csv(
        data_dir / "ratings.dat",
        sep="::",
        engine="python",
        names=["user_id", "item_id", "rating", "timestamp"],
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    return df


def load_movies(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    return pd.read_csv(
        data_dir / "movies.dat",
        sep="::",
        engine="python",
        names=["item_id", "title", "genres"],
        encoding="latin-1",
    )

