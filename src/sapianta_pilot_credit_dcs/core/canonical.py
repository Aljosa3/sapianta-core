import json
from decimal import Decimal, ROUND_HALF_UP

def canonical_dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def quantize_decimal(value: Decimal, places: int = 6) -> Decimal:
    q = Decimal("1").scaleb(-places)
    return value.quantize(q, rounding=ROUND_HALF_UP)

def decimal_to_float_fixed(value: Decimal, places: int = 6) -> float:
    return float(quantize_decimal(value, places))
