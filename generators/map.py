import re
from typing import Optional

from generators.rarity import generate_rarity
from models.map import Map


def generate_map(text: str) -> Optional[Map]:
    """
    Attempt to parse given map data.
    """
    """
    Mildy confusing
    All maps have a type but not all maps have a name
    Rarity: Rare
    name = Destiny Haven
    type = Maze Map
    """
    text = text.strip()

    # Second line should be the name
    if "Map" not in text.splitlines()[2]:
        # Map has no name
        name = None
        map_type = text.splitlines()[1]
    else:
        # Map has a name
        name = text.splitlines()[1]
        map_type = text.splitlines()[2]

    rarity = generate_rarity(text=text)
    tier = re.search("Map Tier: (\d+)", text)
    if tier:
        tier = int(tier.group(1))

    quality = re.search("Quality: (\d+)%", text)
    if quality:
        quality = int(tier.group(1))
    else:
        quality = None

    # May not work correctly
    identified = False if 'Unidentified' in text else True

    iiq = re.search("Item Quantity: \+(\d+)", text)
    if iiq:
        iiq = int(iiq.group(1))
    else:
        iiq = None

    iir = re.search("Item Rarity: \+(\d+)", text)
    if iir:
        iir = int(iir.group(1))
    else:
        iir = None

    pack_size = re.search("Monster Pack Size: \+(\d+)", text)
    if pack_size:
        pack_size = int(pack_size.group(1))
    else:
        pack_size = None

    ilvl = re.search("Item Level: (\d+)", text)
    if ilvl:
        ilvl = int(ilvl.group(1))

    return Map(
        name=name,
        type=map_type,
        identified=identified,
        quality=quality,
        rarity=rarity,
        tier=tier,
        ilvl=ilvl,
        iiq=iiq,
        iir=iir,
        pack_size=pack_size,
        blighted=bool(re.search("Blighted Map", text, re.M)),
        shaper=bool(re.search('Area is influenced by The Shaper', text, re.M)),
        elder=bool(re.search('Area is influenced by The Elder', text, re.M)),
        enslaver=bool(re.search('Map is occupied by The Enslaver', text, re.M)),
        eradicator=bool(re.search('Map is occupied by The Eradicator', text, re.M)),
        constrictor=bool(re.search('Map is occupied by The Constrictor', text, re.M)),
        purifier=bool(re.search('Map is occupied by The Purifier', text, re.M)),
    )




"""
		if info['quality'] != 0:
			info['itype'] = info['itype'].replace("Superior", "").strip()
		map_mods = {}
		map_mods['tier'] = re.findall(r"Map Tier: (\d+)", text)[0]
		map_mods['iiq'] = re.findall(r"Item Quantity: \+(\d+)%", text)[0]

		pack_re = re.findall(r"Pack Size: \+(\d+)%", text)
		if len(pack_re) > 0:
			map_mods['pack'] = pack_re[0]

		iir_re = re.findall(r"Item Rarity: \+(\d+)%", text)
		if len(iir_re) > 0:
			map_mods['iir'] = iir_re[0]

		map_mods['blight'] = bool(re.search("Blighted Map", text, re.M))
		map_mods['shaper'] = bool(re.search('Area is influenced by The Shaper', text, re.M))
		map_mods['elder'] = bool(re.search('Area is influenced by The Elder', text, re.M))
		map_mods['enslaver'] = bool(re.search('Map is occupied by The Enslaver', text, re.M))
		map_mods['eradicator'] = bool(re.search('Map is occupied by The Eradicator', text, re.M))
		map_mods['constrictor'] = bool(re.search('Map is occupied by The Constrictor', text, re.M))
		map_mods['purifier'] = bool(re.search('Map is occupied by The Purifier', text, re.M))

		info['maps'] = map_mods

"""