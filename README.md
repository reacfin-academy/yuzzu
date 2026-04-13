# Yuzzu Case Study

Small bond-pricing package built as `src/yuzzu`.

## Run

```bash
uv run python scripts/example.py
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

```bash
uv run pytest
```
