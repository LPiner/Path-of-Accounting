from typing import Optional

from models.currency import Currency


def generate_currency(text: str) -> Optional[Currency]:
    text = text.strip()
    type = text.splitlines()[1]
    return Currency(
        type=type,
    )



