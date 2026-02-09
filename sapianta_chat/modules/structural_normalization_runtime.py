"""
Structural Normalization Module (SNM v0.1)
EXT-3 · Non-semantic · Deterministic · Read-only

Purpose:
- Return bitwise-identical input (echo)
- Produce a purely structural description of the input string
  based only on positions, delimiters, and character types.

Absolutely no semantic interpretation is performed.
"""

from typing import Dict, Any, List


def structural_normalization(raw_text: str) -> Dict[str, Any]:
    """
    Returns:
      {
        "echo": <input string>,
        "structure": {
            "segments": [...],
            "char_types": [...],
            "metrics": {...}
        }
      }
    """

    # Fail-safe: None treated as empty string (deterministic)
    if raw_text is None:
        raw_text = ""

    echo = raw_text
    length = len(raw_text)

    # -------------------------
    # Character type map
    # -------------------------
    char_types: List[str] = []
    for ch in raw_text:
        if ch.isalpha():
            char_types.append("letter")
        elif ch.isdigit():
            char_types.append("digit")
        elif ch.isspace():
            char_types.append("whitespace")
        else:
            char_types.append("symbol")

    # -------------------------
    # Line segmentation
    # -------------------------
    segments: List[Dict[str, int]] = []
    start = 0

    for idx, ch in enumerate(raw_text):
        if ch == "\n":
            segments.append({
                "type": "line",
                "start_index": start,
                "end_index": idx,
                "length": idx - start,
            })
            start = idx + 1

    # Final segment
    segments.append({
        "type": "line",
        "start_index": start,
        "end_index": length,
        "length": length - start,
    })

    # -------------------------
    # Structural metrics
    # -------------------------
    segment_lengths = [seg["length"] for seg in segments]

    metrics = {
        "char_count": length,
        "segment_count": len(segments),
        "min_segment_length": min(segment_lengths) if segment_lengths else 0,
        "max_segment_length": max(segment_lengths) if segment_lengths else 0,
    }

    return {
        "echo": echo,
        "structure": {
            "segments": segments,
            "char_types": char_types,
            "metrics": metrics,
        }
    }
