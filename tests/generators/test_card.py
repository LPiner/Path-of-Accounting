from unittest.mock import MagicMock
from pytest import mark
from pytest import fixture

from enums.rarity import Rarity
from generators.card import generate_card
from models.card import Card

from models.map import Map


class TestCardGenerator:


    @mark.parametrize("data, expected", [
        ["""
        Rarity: Divination Card
The Cartographer
--------
10x Cartographer's Chisel
--------
It's always easier to find your way if you draw a map of the progress you've made.

""",
         Card(type='The Cartographer')
         ],
    ])
    def test_generate_card(self, data: str, expected: Map):
        assert generate_card(data) == expected
