# Yuzzu - Python training project

Small bond-pricing package with a simple example script and tests.

## Run

You can either make use of `uv`
```bash

uv run python scripts/example.py
```

or create a virtual environment and install the dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install .
python scripts/example.py
```

Edit the variables at the top of `scripts/example.py`:

- `CURVE_PATH`
- `MATURITY`
- `FACE_VALUE`
- `COUPON_RATE`

Then run the script. It prints:

- interpolated yield from the CSV file you provided
- bond price
- Macaulay duration
- yearly cash flows

It also writes a `cash_flows.png` chart in the project directory.

## Test

To run the tests, you can use `uv`

```bash
uv run pytest
```

or install the `dev` dependencies in a virtual environment and run `pytest`

```bash
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install . --group dev
pytest
```
