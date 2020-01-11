from unittest.mock import MagicMock
from pytest import mark
from pytest import fixture

from enums.rarity import Rarity
from generators.map import generate_map

from models.map import Map


class TestMapGenerator:


    @mark.parametrize("data, expected", [
        ["""Rarity: Normal
Beach Map
--------
Map Tier: 1
--------
Item Level: 62
--------
Travel to this Map by using it in a personal Map Device. Maps can only be used once.""",
         Map(type="Beach Map", identified=True, rarity=Rarity.NORMAL, tier=1, ilvl=62, blighted=False, shaper=False, elder=False, enslaver=False, eradicator=False, constrictor=False, purifier=False)
         ],
        [
            """
            Rarity: Unique
Necropolis Map
--------
Map Tier: 15
--------
Item Level: 68
--------
Unidentified
--------
Travel to this Map by using it in a personal Map Device. Maps can only be used once.

            """,
            Map(type="Necropolis Map", identified=False, rarity=Rarity.UNIQUE, tier=15, ilvl=68, blighted=False, shaper=False,
                elder=False, enslaver=False, eradicator=False, constrictor=False, purifier=False)

        ],
        [
            """
Rarity: Rare
Destiny Haven
Maze Map
--------
Map Tier: 9
Item Quantity: +59% (augmented)
Item Rarity: +35% (augmented)
Monster Pack Size: +23% (augmented)
--------
Item Level: 81
--------
Area has patches of burning ground
23% more Rare Monsters
Rare Monsters each have a Nemesis Mod
Monsters take 35% reduced Extra Damage from Critical Strikes
Monsters have a 45% chance to avoid Poison, Blind, and Bleeding
Area is inhabited by Abominations
--------
Travel to this Map by using it in a personal Map Device. Maps can only be used once.

            """,
            Map(type="Maze Map", name="Destiny Haven", identified=True, rarity=Rarity.RARE, tier=9, ilvl=81, blighted=False,
                iir=35,
                iiq=59,
                pack_size=23,
                shaper=False,
                elder=False, enslaver=False, eradicator=False, constrictor=False, purifier=False)

        ],
        [
            """
Rarity: Unique
Superior Bone Crypt Map
--------
Map Tier: 4
Item Quantity: +5% (augmented)
Quality: +5% (augmented)
--------
Item Level: 68
--------
Unidentified
--------
Travel to this Map by using it in a personal Map Device. Maps can only be used once.
            """,
            Map(type="Bone Crypt Map", identified=False, rarity=Rarity.UNIQUE, tier=4, ilvl=68,
                blighted=False,
                iiq=5,
                quality=5,
                shaper=False,
                elder=False, enslaver=False, eradicator=False, constrictor=False, purifier=False)

        ]
    ])
    def test_unique_maps(self, data: str, expected: Map):
        assert generate_map(data) == expected
