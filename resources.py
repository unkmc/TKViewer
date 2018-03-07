#!/usr/bin/env python

"""Resources for NexusTK."""

__author__ = 'DizzyThermal'
__email__ = 'DizzyThermal@gmail.com'
__license__ = 'GNU GPLv3'

import os
import pygame

from file_reader import DATHandler

"""Config Values :: Edit these values to match your system."""
config = dict()
config['nexus_data_dir'] = r'C:\Program Files (x86)\KRU\NexusTK\Data'
config['data_dir'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Data')
config['resources_dir'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Resources')
config['export_dir'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Exports')
config['tile_export_dir'] = os.path.join(config['export_dir'], 'Tiles')
config['sobj_export_dir'] = os.path.join(config['export_dir'], 'Static Objects')
config['maps_dir'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Maps')
config['client_icon'] = os.path.join(config['resources_dir'], 'client_icon.png')
config['client_width'] = 17
config['client_height'] = 15
config['viewer_icon'] = os.path.join(config['resources_dir'], 'viewer_icon.ico')

MAP_IDS = {
    "000000": {"map_name": "Kugnae"},
    "000002": {"map_name": "Walsuk Tavern"},
    "000008": {"map_name": "Dusk Shaman"},
    "000009": {"map_name": "Dawn Shaman"},
    "000011": {"map_name": "Warrior Tebaek"},
    "000012": {"map_name": "Tebaek Sanctum"},
    "000013": {"map_name": "Mage Haedu"},
    "000020": {"map_name": "Stoney Goh"},
    "000021": {"map_name": "Left Stone Board"},
    "000023": {"map_name": "Kugnae Salon"},
    "000028": {"map_name": "Baegil Shop"},
    "000029": {"map_name": "Baegi Shop"},
    "000030": {"map_name": "Baek Shop"},
    "000035": {"map_name": "Yusa Pit"},
    "000037": {"map_name": "Bamboo Tavern"},
    "000041": {"map_name": "Mythic Nexus"},
    "000099": {"map_name": "North Hamgyong Valley"},
    "000114": {"map_name": "Hamgyong nam-do"},
    "000306": {"map_name": "Haedu Sanctum"},
    "000309": {"map_name": "Eldritch"},
    "000325": {"map_name": "Ming-ken Shrine"},
    "000330": {"map_name": "Buya"},
    "000332": {"map_name": "Spring Tavern"},
    "000333": {"map_name": "Dok Smith"},
    "000334": {"map_name": "Ogi Butcher"},
    "000335": {"map_name": "Blossom Seams"},
    "000336": {"map_name": "Chi Seams"},
    "000337": {"map_name": "Paryu Message"},
    "000338": {"map_name": "Felis Shaman"},
    "000339": {"map_name": "Storm Shaman"},
    "000340": {"map_name": "Peach Chapel"},
    "000341": {"map_name": "Warrior Yebaek"},
    "000342": {"map_name": "Mage Eldritch"},
    "000343": {"map_name": "Rogue Maso"},
    "000344": {"map_name": "Poet Song"},
    "000345": {"map_name": "Shadow Dragon"},
    "000346": {"map_name": "Budol Goh"},
    "000347": {"map_name": "Beginner Budol Board"},
    "000351": {"map_name": "JadeSpear's Home"},
    "000356": {"map_name": "Mountain Arena"},
    "000359": {"map_name": "Pyung Shop"},
    "000360": {"map_name": "Sire Pit"},
    "000361": {"map_name": "Pepper Tavern"},
    "000362": {"map_name": "Yunsil Tavern"},
    "000363": {"map_name": "Bagai Shop"},
    "000364": {"map_name": "Pitch Shop"},
    "000365": {"map_name": "Buya Salon"},
    "000366": {"map_name": "Yebaek Sanctum"},
    "000368": {"map_name": "Maso Sanctum"},
    "000369": {"map_name": "Song Sanctum"},
    "000370": {"map_name": "Dirt Cave"},
    "000371": {"map_name": "Vermin Cavern"},
    "000372": {"map_name": "Rat Race"},
    "000373": {"map_name": "Sonar Central"},
    "000374": {"map_name": "Thousand Legs"},
    "000375": {"map_name": "Rat Burrough"},
    "000384": {"map_name": "Gangrel Cave"},
    "000385": {"map_name": "Bear Chamber"},
    "000386": {"map_name": "Curtain Den"},
    "000387": {"map_name": "Winding Cave"},
    "000388": {"map_name": "Cub Cavern"},
    "000389": {"map_name": "Paw Catacomb"},
    "000390": {"map_name": "Fox Landscape"},
    "000391": {"map_name": "Barren Cave"},
    "000392": {"map_name": "Lush Tunnels"},
    "000393": {"map_name": "Lava Cave"},
    "000394": {"map_name": "Wolf Cavern"},
    "000395": {"map_name": "Raven's Roost"},
    "000396": {"map_name": "Tall Tunnels"},
    "000397": {"map_name": "Winding Cavern"},
    "000398": {"map_name": "Water hole"},
    "000399": {"map_name": "Twenty-eight Tails"},
    "000400": {"map_name": "Radiant Valley"},
    "000401": {"map_name": "Deer Field"},
    "000402": {"map_name": "Barren Slopes"},
    "000403": {"map_name": "Grazing Rows"},
    "000404": {"map_name": "Warm Sands"},
    "000405": {"map_name": "Deer Edge"},
    "000406": {"map_name": "Disturbed Nests"},
    "000407": {"map_name": "Narrow Pass"},
    "000408": {"map_name": "Albino Way"},
    "000409": {"map_name": "Prey"},
    "000441": {"map_name": "Barren Graves"},
    "000442": {"map_name": "Sute's Nest"},
    "000443": {"map_name": "Forsaken Grotto"},
    "000444": {"map_name": "The Black Lake"},
    "000445": {"map_name": "Death's Isthmus"},
    "000446": {"map_name": "Sute's Welcome"},
    "000447": {"map_name": "Dark Pools"},
    "000450": {"map_name": "Old Shanty"},
    "000451": {"map_name": "Dagger House"},
    "000452": {"map_name": "Wicked Yard"},
    "000453": {"map_name": "Condemned"},
    "000454": {"map_name": "Broken Floor"},
    "000455": {"map_name": "Ruined House"},
    "000456": {"map_name": "Sorrow Yard"},
    "000457": {"map_name": "Sorrow Well"},
    "000458": {"map_name": "Dagger Yard"},
    "000459": {"map_name": "Wicked House"},
    "000486": {"map_name": "Buya Library"},
    "000487": {"map_name": "Buya Theater"},
    "000488": {"map_name": "Models Runway"},
    "000489": {"map_name": "Imperial Runway Foyer"},
    "000490": {"map_name": "Imperial Runway Show"},
    "000501": {"map_name": "Dirge"},
    "000502": {"map_name": "Bone Feet"},
    "000503": {"map_name": "Lost Pen"},
    "000504": {"map_name": "Bone Finger"},
    "000505": {"map_name": "Muffled Drum"},
    "000506": {"map_name": "Torn Shroud"},
    "000507": {"map_name": "Vile Pit"},
    "000508": {"map_name": "Death March"},
    "000521": {"map_name": "Forest Crossroads"},
    "000522": {"map_name": "Cave"},
    "000532": {"map_name": "Spirit Grove"},
    "000533": {"map_name": "Lilac Walk"},
    "000534": {"map_name": "Crumbling Steps"},
    "000535": {"map_name": "Infested Granary"},
    "000536": {"map_name": "Oak Pathway"},
    "000537": {"map_name": "Meeting Field"},
    "000538": {"map_name": "Pine Grove"},
    "000539": {"map_name": "Open Pasture"},
    "000540": {"map_name": "Tangled Thicket"},
    "000541": {"map_name": "Stone Bridge"},
    "000615": {"map_name": "The Ultimate Gauntlet"},
    "000720": {"map_name": "Kinung"},
    "001000": {"map_name": "Koguryo Valley"},
    "001001": {"map_name": "Buya Valley"},
    "001002": {"map_name": "Wilderness"},
    "001004": {"map_name": "Dae Shore"},
    "001005": {"map_name": "Vale"},
    "001008": {"map_name": "Islets"},
    "001011": {"map_name": "Kugnae Gathering"},
    "001012": {"map_name": "Buya Gathering"},
    "001014": {"map_name": "Sonhi Valley"},
    "001015": {"map_name": "Wilderness Valley"},
    "001016": {"map_name": "Vale Valley"},
    "001031": {"map_name": "Noxhil Home"},
    "001032": {"map_name": "Buya Houses"},
    "001059": {"map_name": "Graveyard"},
    "001408": {"map_name": "Baekho Altar"},
    "001413": {"map_name": "Ju Jak Altar"},
    "001418": {"map_name": "Hyun Moo Altar"},
    "001451": {"map_name": "Mountain Ascent"},
    "001452": {"map_name": "Small Valley"},
    "001453": {"map_name": "Forgotten Falls"},
    "001454": {"map_name": "Mountain Pass"},
    "001455": {"map_name": "Mountain Top"},
    "002205": {"map_name": "Oh-mudum crypt"},
    "002206": {"map_name": "Uk-mudum crypt"},
    "002207": {"map_name": "Chil-mudum crypt"},
    "002208": {"map_name": "Pal-mudum crypt"},
    "002209": {"map_name": "Gu-mudum crypt"},
    "002210": {"map_name": "Hallowed Pass"},
    "002220": {"map_name": "Cemetery"},
    "002221": {"map_name": "Il-mudum crypt"},
    "002222": {"map_name": "Ee-mudum crypt"},
    "002223": {"map_name": "Sam-mudum crypt"},
    "002224": {"map_name": "Sa-mudum crypt"},
    "002500": {"map_name": "Nagnang"},
    "002517": {"map_name": "Nagnang Valley"},
    "002520": {"map_name": "Nagnang Gathering"},
    "002590": {"map_name": "Nagnang Arena"},
    "002593": {"map_name": "Stone pit"},
    "002964": {"map_name": "Vortex"},
    "003010": {"map_name": "Carnage Hall"},
    "003016": {"map_name": "Haunted Arena"},
    "003041": {"map_name": "Chonsa Den"},
    "003300": {"map_name": "Tutorial Hall"},
    "003301": {"map_name": "Tutor's Domain"},
    "003400": {"map_name": "Pond's Library"},
    "003502": {"map_name": "Kugnae Palace's Prison"},
    "003517": {"map_name": "Interrogation chambers"},
    "003518": {"map_name": "Meeting hall"},
    "003519": {"map_name": "Stealth Grotto"},
    "003537": {"map_name": "Tai Chi"},
    "003538": {"map_name": "Yin & Yang"},
    "003540": {"map_name": "Tao Te Ching"},
    "003575": {"map_name": "Palace Monster Keep"},
    "003627": {"map_name": "Poetic Justice"},
    "003628": {"map_name": "Sanctum of Song"},
    "003629": {"map_name": "Garden of the Muses"},
    "003636": {"map_name": "Echo's Refuge"},
    "003637": {"map_name": "Asa's Inn"},
    "003639": {"map_name": "Flight of Fancy"},
    "003640": {"map_name": "The Road Not Taken"},
    "003658": {"map_name": "Hsien Courtyard"},
    "003703": {"map_name": "Kugnae Mage's Hall"},
    "003705": {"map_name": "Buya Warrior's Hall"},
    "003706": {"map_name": "Buya Rogue's Hall"},
    "003707": {"map_name": "Buya Mage's Hall"},
    "003708": {"map_name": "Buya Poet's Hall"},
    "003910": {"map_name": "Heavens Clan"},
    "003930": {"map_name": "Bear Clan"},
    "003938": {"map_name": "Bear Falls"},
    "003940": {"map_name": "Phoenix Clan Garden"},
    "003941": {"map_name": "Phoenix Hall"},
    "003942": {"map_name": "Phoenix Arena"},
    "003944": {"map_name": "Phoenix Council Room"},
    "003945": {"map_name": "The Nest"},
    "003946": {"map_name": "Crafting Claws"},
    "003947": {"map_name": "Everlasting Fire"},
    "003948": {"map_name": "Feng-Huang"},
    "003949": {"map_name": "Phoenix Warp Room"},
    "003950": {"map_name": "Enigma Clan"},
    "003951": {"map_name": "Enigma Hall"},
    "003952": {"map_name": "Strength in Unity"},
    "003953": {"map_name": "Enigma Primogen"},
    "003954": {"map_name": "Enigma Treasury"},
    "003955": {"map_name": "Hamal Pagoda"},
    "003956": {"map_name": "Tol'Chuk's Lair"},
    "003957": {"map_name": "Gauntlet of Honor"},
    "003959": {"map_name": "Gordian's Knot"},
    "003960": {"map_name": "Lost Kingdom Clan"},
    "003970": {"map_name": "Dharma Clan"},
    "003990": {"map_name": "Elendhirin Clan"},
    "004504": {"map_name": "Koguryo Palace Courtyard"},
    "004505": {"map_name": "Royal Palace Mezzanine"},
    "004506": {"map_name": "Koguryo Throne Room"},
    "004507": {"map_name": "Kugnae Theater"},
    "004508": {"map_name": "Koguryo Royal Court"},
    "004513": {"map_name": "Kugnae Palace Baths"},
    "004514": {"map_name": "Royal Palace Stairway"},
    "004516": {"map_name": "Coliseum Atrium"},
    "004518": {"map_name": "Victory Square"},
    "004519": {"map_name": "King MuHyul's Jeongwon"},
    "004520": {"map_name": "Koguryo Treasury"},
    "004529": {"map_name": "Royal Palace Kitchen"},
    "004530": {"map_name": "Royal Dining Room"},
    "004539": {"map_name": "Yuri's Seamstress"},
    "004542": {"map_name": "Koguryo Palace Hall"},
    "004543": {"map_name": "Koguryo Royal Room"},
    "004544": {"map_name": "Koguryo Guest Room"},
    "004545": {"map_name": "King's Bedroom"},
    "004546": {"map_name": "Koguryo Army Quarters"},
    "004606": {"map_name": "Buya Courtyard"},
    "004613": {"map_name": "Secret Garden"},
    "004623": {"map_name": "Shining Jewel Foundation"},
    "004980": {"map_name": "Destiny Garden"},
    "005010": {"map_name": "Tiger Clan Garden"},
    "005040": {"map_name": "SanSin Garden"},
    "006582": {"map_name": "Buya Library Caverns"},
    "006583": {"map_name": "Buya Library Caverns"},
    "006584": {"map_name": "Buya Library Caverns"},
    "006585": {"map_name": "Buya Library Caverns"},
    "006586": {"map_name": "Buya Library Caverns"},
    "006587": {"map_name": "Buya Library Caverns"},
    "006588": {"map_name": "Buya Library Caverns"},
    "006589": {"map_name": "Buya Library Caverns"},
    "006590": {"map_name": "Buya Library Caverns"},
    "006591": {"map_name": "Buya Library Caverns"},
    "006592": {"map_name": "Buya Library Caverns"},
    "006593": {"map_name": "Buya Library Caverns"},
    "006594": {"map_name": "Buya Library Caverns"},
    "006595": {"map_name": "Buya Library Caverns"},
    "006596": {"map_name": "Buya Library Caverns"},
    "006597": {"map_name": "Buya Library Caverns"},
    "006598": {"map_name": "Buya Library Caverns"},
    "006599": {"map_name": "Buya Library Caverns"},
    "008200": {"map_name": "Incubator"},
    "009000": {"map_name": "Woodlands Entrance"},
    "013000": {"map_name": "Prince Study"},
    "013001": {"map_name": "Prince Mobon"},
    "013002": {"map_name": "Prince MingJung"},
    "018400": {"map_name": "Sonjok'ada"},
    "018402": {"map_name": "Ocean bound Hanseong"},
    "029200": {"map_name": "Duel"},
    "027800": {"map_name": "Malgalod"},
    "030580": {"map_name": "Hidden Pond"},
    "030591": {"map_name": "Supply Tunnel"},
    "030636": {"map_name": "Supply Cache"},
    "030686": {"map_name": "Eastern Collapse"},
    "030800": {"map_name": "Mine Entrance"},
    "030802": {"map_name": "Inner Mines"},
    "030803": {"map_name": "Deep Mines"},
    "030811": {"map_name": "Desolate Mines"},
    "030812": {"map_name": "Darkened Tunnels"},
    "030813": {"map_name": "Underground Cavern"},
    "030814": {"map_name": "Muddy Passage"},
    "030815": {"map_name": "Shadow Cave"},
    "030816": {"map_name": "Dirt Grotto"},
    "030817": {"map_name": "Leeches Lair"},
    "030818": {"map_name": "Echo Valley"},
    "030822": {"map_name": "South Tunnel"},
    "030823": {"map_name": "South Expansion"},
    "030824": {"map_name": "East Tunnel"},
    "030825": {"map_name": "East Expansion"},
    "032095": {"map_name": "Entrance to Omphalos"}
}

"""Extracts dats to the Data Directory"""
def extract_dats(dats, extract_directory=config['data_dir']):
    if os.path.exists(extract_directory):
        for i in range(len(dats)):
            dat = DATHandler(dats[i])
            dat.export_files(extract_dir=extract_directory)

"""Returns the TK ID of the Map Name passed in, defined above in MAP_IDS."""
def get_id_from_map_name(map_name):
    for map_id, map_info in MAP_IDS.items():
        if map_info['map_name'] == map_name:
            return map_id

    return None

"""Creates a Sprite to represent a part"""
class Part(pygame.sprite.Sprite):
    def __init__(self, part):
        super().__init__()

        self.image = pygame.image.fromstring(part.tobytes(), part.size, part.mode)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)