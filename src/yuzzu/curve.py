from pathlib import Path

import numpy as np
import pandas as pd


class YieldCurve:
    """Load yields from a CSV file and interpolate rates by maturity."""

    def __init__(self, csv_path):
        """Read yield curve data from a CSV file.

        Args:
            csv_path (str | Path): Path to a CSV file with `maturity` and
                `yield` columns.
        """
        path = Path(csv_path)
        if not path.exists():
            raise FileNotFoundError(f"Curve file not found: {path}")

        self.path = path
        frame = pd.read_csv(path).sort_values("maturity").reset_index(drop=True)
        self.maturities = frame["maturity"].to_numpy(dtype=float)
        self.yields = frame["yield"].to_numpy(dtype=float)

    def rate(self, maturity):
        """Return the interpolated yield for a maturity.

        Args:
            maturity (int | float): Bond maturity in years.

        Returns:
            float: Interpolated yield as a decimal.
        """
        if maturity <= 0:
            raise ValueError("maturity must be greater than 0")

        return float(np.interp(maturity, self.maturities, self.yields))
