import re

from enums.rarity import Rarity


def generate_rarity(text: str) -> Rarity:
    for x in Rarity:
        if re.search(rf"Rarity: {x.value}", text):
            return x
    raise NotImplementedError("Unable to discover item Rarity")