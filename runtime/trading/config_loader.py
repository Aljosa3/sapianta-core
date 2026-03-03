"""
Configuration loader and validator for trading engine.
Ensures config is valid and deterministically hashed.
"""

from deterministic_utils import stable_hash


def load_and_validate_config(config: dict, assets: list) -> dict:
    """
    Load and validate trading engine configuration.

    Args:
        config: Configuration dictionary
        assets: List of asset names that will be traded

    Returns:
        Dictionary with 'config' (immutable snapshot) and 'config_hash'

    Raises:
        Exception: If configuration is invalid
    """
    required_keys = [
        'stop_multiplier',
        'min_sample',
        'min_edge_threshold',
        'max_position_cap'
    ]

    # Validate required keys
    for key in required_keys:
        if key not in config:
            raise Exception(f"Missing required config key: {key}")

    # Validate stop_multiplier is a dict
    if not isinstance(config['stop_multiplier'], dict):
        raise Exception("stop_multiplier must be a dictionary")

    # Validate stop_multiplier contains entries for all assets
    for asset in assets:
        if asset not in config['stop_multiplier']:
            raise Exception(f"stop_multiplier missing entry for asset: {asset}")

    # Validate each stop_multiplier value is numeric and > 0
    for asset, value in config['stop_multiplier'].items():
        if not isinstance(value, (int, float)):
            raise Exception(f"stop_multiplier[{asset}] must be numeric, got {type(value)}")
        if value <= 0:
            raise Exception(f"stop_multiplier[{asset}] must be > 0, got {value}")

    # Create immutable snapshot (deep copy via dict constructor)
    immutable_snapshot = {
        'stop_multiplier': dict(config['stop_multiplier']),
        'min_sample': config['min_sample'],
        'min_edge_threshold': config['min_edge_threshold'],
        'max_position_cap': config['max_position_cap']
    }

    # Compute deterministic hash
    config_hash = stable_hash(immutable_snapshot)

    return {
        "config": immutable_snapshot,
        "config_hash": config_hash
    }
