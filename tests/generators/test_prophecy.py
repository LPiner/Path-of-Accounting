from unittest.mock import MagicMock
from pytest import mark
from pytest import fixture

from enums.rarity import Rarity
from generators.map import generate_map
from generators.prophecy import generate_prophecy

from models.map import Map
from models.prophecy import Prophecy


class TestProphecyGenerator:


    @mark.parametrize("data, expected", [
        ["""
        Rarity: Normal
Fire from the Sky
--------
Fire rains down across the land. Beware the path you take.
--------
You will discover an area with an Infernal Tempest
--------
Right-click to add this prophecy to your character.
""",
         Prophecy(name='Fire from the Sky', rarity=Rarity.NORMAL)
         ],
    ])
    def test_generate_prophecy(self, data: str, expected: Map):
        assert generate_prophecy(data) == expected
