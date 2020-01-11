from unittest.mock import MagicMock
from pytest import mark
from pytest import fixture

from enums.rarity import Rarity
from generators.card import generate_card
from generators.currency import generate_currency
from models.card import Card
from models.currency import Currency

from models.map import Map


class TestCurrencyGenerator:


    @mark.parametrize("data, expected", [
        ["""
Rarity: Currency
Orb of Transmutation
--------
Stack Size: 16/40
--------
Upgrades a normal item to a magic item
--------
Right click this item then left click a normal item to apply it.
Shift click to unstack.
""",
         Currency(type='Orb of Transmutation')
         ],
    ])
    def test_generate_currency(self, data: str, expected: Map):
        assert generate_currency(data) == expected
