def validate_list(values: list, allowlist: set) -> list:
    return [v for v in values if v in allowlist]
