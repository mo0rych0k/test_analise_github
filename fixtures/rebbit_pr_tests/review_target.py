"""Small target for the dense-review PR scenario."""


def normalize_name(value: str) -> str:
    return " ".join(value.strip().split()).title()
