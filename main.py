from kivy.uix.boxlayout import BoxLayout
from kivymd.toast import toast
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import Screen
from random import randint, choice, shuffle
import webbrowser

Sledge = {'name': 'Sledge', 'loadout_main': ['L85A2', 'M590A1'], 'loadout_secondary': ['P226 Mk 25', 'SMG-11'], 'secondary_gadget': ['Grenade', 'Flashbang'], 'pic': 'images_operators_att/Sledge.png'}
Thatcher = {'name': 'Thatcher', 'loadout_main': ['AR33','L85A2', 'M590A1'], 'loadout_secondary': ['P226 Mk 25'], 'secondary_gadget': ['Claymore', 'Breach Charges'], 'pic': 'images_operators_att/Thatcher.png'}
Ash = {'name': 'Ash', 'loadout_main': ['R4-C', 'G36-C'], 'loadout_secondary': ['5.7 USG', 'M45 MEUSOC'], 'secondary_gadget': ['Breach Charges', 'Claymore'], 'pic': 'images_operators_att/Ash.png'}
Thermite = {'name': 'Thermite', 'loadout_main': ['556XI', 'M1014'], 'loadout_secondary': ['5.7 USG', 'M45 MEUSOC'], 'secondary_gadget': ['Claymore', 'Flashbang'], 'pic': 'images_operators_att/Thermite.png'}
Twitch = {'name': 'Twitch', 'loadout_main': ['F2', '417', 'SG-CQB'], 'loadout_secondary': ['P9', 'LFP586'], 'secondary_gadget': ['Claymore', 'Smoke Grenade'], 'pic': 'images_operators_att/Twitch.png'}
Montagne = {'name': 'Montagne', 'loadout_main': ['Shield'], 'loadout_secondary': ['P9', 'LFP586'], 'secondary_gadget': ['Hard-Breach Charge', 'Smoke Grenade'], 'pic': 'images_operators_att/Montagne.png'}
Glaz = {'name': 'Glaz', 'loadout_main': ['OTs-03'], 'loadout_secondary': ['PMM', 'GONNE-6'], 'secondary_gadget': ['Grenade', 'Smoke Grenade'], 'pic': 'images_operators_att/Glaz.png'}
Fuze = {'name': 'Fuze', 'loadout_main': ['Ballistic shield', '6P41', 'AK-12'], 'loadout_secondary': ['PMM', 'GSH-18'], 'secondary_gadget': ['Breach Charges', 'Hard-Breach Charge'], 'pic': 'images_operators_att/Fuze.png'}
Blitz = {'name': 'Blitz', 'loadout_main': ['Ballistic Shield B52'], 'loadout_secondary': ['P12'], 'secondary_gadget': ['Breach Charges', 'Smoke Grenade'], 'pic': 'images_operators_att/Blitz.png'}
IQ = {'name': 'IQ', 'loadout_main': ['G8A1', 'COMMANDO-552', 'AUG A2'], 'loadout_secondary': ['P12'], 'secondary_gadget': ['Breach Charges', 'Claymore'], 'pic': 'images_operators_att/IQ.png'}
Buck = {'name': 'Buck', 'loadout_main': ['C8-SFW', 'CAMRS'], 'loadout_secondary': ['Mk1 9mm'], 'secondary_gadget': ['Hard-Breach Charge', 'Flashbang'], 'pic': 'images_operators_att/Buck.png'}
BlackBeard = {'name': 'BlackBeard', 'loadout_main': ['Mk17 CQB', 'SR-25'], 'loadout_secondary': ['D-50'], 'secondary_gadget': ['Breach Charges', 'Flashbang'], 'pic': 'images_operators_att/Blackbeard.png'}
Capitao = {'name': 'Capitao', 'loadout_main': ['PARA-308', 'M249'], 'loadout_secondary': ['PRB92'], 'secondary_gadget': ['Hard-Breach Charge', 'Claymore'], 'pic': 'images_operators_att/Capitao.png'}
Hibana = {'name': 'Hibana', 'loadout_main': ['TYPE-89', 'SUPERNOVA'], 'loadout_secondary': ['P229 RC', 'BEARING 9'], 'secondary_gadget': ['Breach Charges', 'Flashbang'], 'pic': 'images_operators_att/Hibana.png'}
Jackal = {'name': 'Jackal', 'loadout_main': ['C7E', 'PDW9', 'ITA12L'], 'loadout_secondary': ['USP40', 'ITA12S'], 'secondary_gadget': ['Smoke Grenade', 'Claymore'], 'pic': 'images_operators_att/Jackal.png'}
Zofia = {'name': 'Zofia', 'loadout_main': ['LMG-E', 'M762'], 'loadout_secondary': ['RG15'], 'secondary_gadget': ['Breach Charges', 'Claymore'], 'pic': 'images_operators_att/Zofia.png'}
Ying = {'name': 'Ying', 'loadout_main': ['T-95 LSW', 'SIX12'], 'loadout_secondary': ['Q-929'], 'secondary_gadget': ['Hard-Breach Charge', 'Smoke Grenade'], 'pic': 'images_operators_att/Ying.png'}
Dokkaebi = {'name': 'Dokkaebi', 'loadout_main': ['MK 14 EBR', 'BOSG.12.2'], 'loadout_secondary': ['GONNE-6', 'SMG-12'], 'secondary_gadget': ['Smoke Grenade', 'Flashbang'], 'pic': 'images_operators_att/Dokkaebi.png'}
Lion = {'name': 'Lion', 'loadout_main': ['V308', '417', 'SG-CQB'], 'loadout_secondary': ['GONNE-6', 'LFP586'], 'secondary_gadget': ['Hard-Breach Charge', 'Flashbang'], 'pic': 'images_operators_att/Lion.png'}
Finka = {'name': 'Finka', 'loadout_main': ['SPEAR .308', '6P41', 'SASG-12'], 'loadout_secondary': ['PMM', 'GONNE-6'], 'secondary_gadget': ['Flashbang', 'Hard-Breach Charges'], 'pic': 'images_operators_att/Finka.png'}
Maverick = {'name': 'Maverick', 'loadout_main': ['AR-15.50', 'M4 GS'], 'loadout_secondary': ['1911 TACOPS'], 'secondary_gadget': ['Grenade', 'Claymore'], 'pic': 'images_operators_att/Maverick.png'}
Nomad = {'name': 'Nomad', 'loadout_main': ['AK-74M', 'ARX200'], 'loadout_secondary': ['PRB92', '.44 MAG SEMI-AUTO'], 'secondary_gadget': ['Breach Charges', 'Flashbang'], 'pic': 'images_operators_att/Nomad.png'}
Gridlock = {'name': 'Gridlock', 'loadout_main': ['F90', 'M249 SAW'], 'loadout_secondary': ['SUPER SHORTY', 'GONNE-6'], 'secondary_gadget': ['Smoke Grenade', 'Breach Charges'], 'pic': 'images_operators_att/Gridlock.png'}
Nokk = {'name': 'Nokk', 'loadout_main': ['FMG-9', 'SIX12 SD'], 'loadout_secondary': ['5.7 USG', 'D-50'], 'secondary_gadget': ['Grenade', 'Hard-Breach Charge'], 'pic': 'images_operators_att/Nokk.png'}
Amaru = {'name': 'Amaru', 'loadout_main': ['G8A1', 'SUPERNOVA'], 'loadout_secondary': ['GONNE-6', 'SMG-11'], 'secondary_gadget': ['Hard-Breach Charge', 'Flashbang'], 'pic': 'images_operators_att/Amaru.png'}
Kali = {'name': 'Kali', 'loadout_main': ['CSRX 300'], 'loadout_secondary': ['SPSMG9', 'C75 AUTO'], 'secondary_gadget': ['Breach Charges', 'Claymore'], 'pic': 'images_operators_att/Kali.png'}
Iana = {'name': 'Iana', 'loadout_main': ['ARX200', 'G36C'], 'loadout_secondary': ['MK1 9MM', 'GONNE-6'], 'secondary_gadget': ['Grenade', 'Smoke Grenade'], 'pic': 'images_operators_att/Iana.png'}
Ace = {'name': 'Ace', 'loadout_main': ['AK-12', 'M1014'], 'loadout_secondary': ['P9'], 'secondary_gadget': ['Smoke Grenade', 'Breach Charges'], 'pic': 'images_operators_att/Ace.png'}
Zero = {'name': 'Zero', 'loadout_main': ['SC3000K', 'MP7'], 'loadout_secondary': ['5.7 USG', 'GONNE-6'], 'secondary_gadget': ['Hard-Breach Charge', 'Claymore'], 'pic': 'images_operators_att/Zero.png'}
Flores = {'name': 'Flores', 'loadout_main': ['AR33', 'SR-25'], 'loadout_secondary': ['GSH-18'], 'secondary_gadget': ['Flashbang', 'Claymore'], 'pic': 'images_operators_att/Flores.png'}

r6_ops_attack = [Sledge, Thatcher, Ash, Thermite, Twitch, Montagne, Glaz, Fuze, Blitz, IQ, Buck,BlackBeard, Capitao, Hibana, Jackal, Zofia, Ying, Dokkaebi, Lion,
Finka, Maverick, Nomad, Gridlock, Nokk, Amaru, Kali, Iana, Ace, Zero, Flores]

Smoke = {'name': 'Smoke', 'loadout_main': ['FMG-9', 'M590A1'], 'loadout_secondary': ['P226 Mk 25', 'SMG-11'], 'secondary_gadget': ['Shield', 'Barbed wire'], 'pic': 'images_operators_def/Smoke.png'}
Mute = {'name': 'Mute', 'loadout_main': ['MP5-K', 'M590A1'], 'loadout_secondary': ['P226 Mk 25', 'SMG-11'], 'secondary_gadget': ['C4', 'Bulletproof camera'], 'pic': 'images_operators_def/Mute.png'}
Castle = {'name': 'Castle', 'loadout_main': ['UMP-45', 'M1014'], 'loadout_secondary': ['5.7 USG', 'SUPER SHORTY'], 'secondary_gadget': ['Bulletproof camera', 'Proximity alarm'], 'pic': 'images_operators_def/Castle.png'}
Pulse = {'name': 'Pulse', 'loadout_main': ['UMP-45', 'M1014'], 'loadout_secondary': ['5.7 USG', 'M45 MEUSOC'], 'secondary_gadget': ['C4', 'Barbed wire'], 'pic': 'images_operators_def/Pulse.png'}
Doc = {'name': 'Doc', 'loadout_main': ['MP5', 'P90', 'SG-CQB'], 'loadout_secondary': ['P9', 'LFP586'], 'secondary_gadget': ['Bulletproof camera', 'Barbed wire'], 'pic': 'images_operators_def/Doc.png'}
Rook = {'name': 'Rook', 'loadout_main': ['MP5', 'P90', 'SG-CQB'], 'loadout_secondary': ['P9', 'LFP586'], 'secondary_gadget': ['Proximity alarm', 'Impacts'], 'pic': 'images_operators_def/Rook.png'}
Tachanka = {'name': 'Tachanka', 'loadout_main': ['DP27', '9x19vsn'], 'loadout_secondary': ['PMM', 'GSH-18'], 'secondary_gadget': ['Barbed wire', 'Proximity alarm'], 'pic': 'images_operators_def/Tachankin.png'}
Kapkan = {'name': 'Kapkan', 'loadout_main': ['SASG-12', '9x19vsn'], 'loadout_secondary': ['PMM', 'GSH-18'], 'secondary_gadget': ['Impacts', 'C4'], 'pic': 'images_operators_def/Kapkan.png'}
Jager = {'name': 'Jager', 'loadout_main': ['416-Carabine', 'M780'], 'loadout_secondary': ['P12'], 'secondary_gadget': ['Barbed wire', 'Bulletproof camera'], 'pic': 'images_operators_def/Jager.png'}
Bandit = {'name': 'Bandit', 'loadout_main': ['MP7', 'M780'], 'loadout_secondary': ['P12'], 'secondary_gadget': ['C4', 'Barbed wire'], 'pic': 'images_operators_def/Bandit.png'}
Frost = {'name': 'Frost', 'loadout_main': ['9mm C1', 'Super 90'], 'loadout_secondary': ['Mk1 9mm', 'ITA12S'], 'secondary_gadget': ['Shield', 'Bulletproof camera'], 'pic': 'images_operators_def/Frost.png'}
Valkyrie = {'name': 'Valkyrie', 'loadout_main': ['MPX', 'SPAS-12'], 'loadout_secondary': ['D-50'], 'secondary_gadget': ['C4', 'Impacts'], 'pic': 'images_operators_def/Valkyrie.png'}
Caveira = {'name': 'Caveira', 'loadout_main': ['M12', 'SPAS-15'], 'loadout_secondary': ['LUISON'], 'secondary_gadget': ['Impacts', 'Proximity alarm'], 'pic': 'images_operators_def/Caveira.png'}
Echo = {'name': 'Echo', 'loadout_main': ['MP5-SD', 'SUPERNOVA'], 'loadout_secondary': ['P229 RC', 'BEARING 9'], 'secondary_gadget': ['Impacts', 'Shield'], 'pic': 'images_operators_def/Echo.png'}
Mira = {'name': 'Mira', 'loadout_main': ['Vector .45 ACP', 'ITA12L'], 'loadout_secondary': ['USP40', 'ITA12S'], 'secondary_gadget': ['C4', 'Proximity alarm'], 'pic': 'images_operators_def/Mira.png'}
Ela = {'name': 'Ela', 'loadout_main': ['Scorpion Evo 3 A1', 'FO-12'], 'loadout_secondary': ['RG15'], 'secondary_gadget': ['Barbed wire', 'Shield'], 'pic': 'images_operators_def/Ela.png'}
Lesion = {'name': 'Lesion', 'loadout_main': ['T-5 SMG', 'SIX12 SD'], 'loadout_secondary': ['Q-929'], 'secondary_gadget': ['Impacts', 'Bulletproof camera'], 'pic': 'images_operators_def/Lesion.png'}
Vigil = {'name': 'Vigil', 'loadout_main': ['K1A', 'BOSG.12.2'], 'loadout_secondary': ['C75 AUTO', 'SMG-12'], 'secondary_gadget': ['Impacts', 'Bulletproof camera'], 'pic': 'images_operators_def/Vigil.png'}
Maestro = {'name': 'Maestro', 'loadout_main': ['ALDA 5.56', 'ACS12'], 'loadout_secondary': ['KERATOS .357', 'BAILIFF410'], 'secondary_gadget': ['Impacts', 'Barbed wire'], 'pic': 'images_operators_def/Maestro.png'}
Alibi = {'name': 'Alibi', 'loadout_main': ['MX4 STORM', 'ACS12'], 'loadout_secondary': ['KERATOS .357', 'BAILIFF410'], 'secondary_gadget': ['Impacts', 'Shield'], 'pic': 'images_operators_def/Alibi.png'}
Clash = {'name': 'Clash', 'loadout_main': ['Shock Shield'], 'loadout_secondary': ['P-10C', 'SPSMG9'], 'secondary_gadget': ['Impacts', 'Barbed wire'], 'pic': 'images_operators_def/Clash.png'}
Kaid = {'name': 'Kaid', 'loadout_main': ['AUG A3', 'TCSG12'], 'loadout_secondary': ['LFP586', '.44 MAG SEMI-AUTO'], 'secondary_gadget': ['C4', 'Barbed wire'], 'pic': 'images_operators_def/Kaid.png'}
Mozzie = {'name': 'Mozzie', 'loadout_main': ['COMMANDO 9', 'P10 RONI'], 'loadout_secondary': ['SDP 9MM'], 'secondary_gadget': ['C4', 'Barbed wire'], 'pic': 'images_operators_def/Mozzie.png'}
Warden = {'name': 'Warden', 'loadout_main': ['MPX', 'M590A1'], 'loadout_secondary': ['SMG-12', 'P-10C'], 'secondary_gadget': ['Shield', 'C4'], 'pic': 'images_operators_def/Warden.png'}
Goyo = {'name': 'Goyo', 'loadout_main': ['Vector .45 ACP', 'TCSG12'], 'loadout_secondary': ['P229 RC'], 'secondary_gadget': ['C4', 'Proximity alarm'], 'pic': 'images_operators_def/Goyo.png'}
Wamai = {'name': 'Wamai', 'loadout_main': ['AUG 2', 'MP5-K'], 'loadout_secondary': ['P12', 'KERATOS .357'], 'secondary_gadget': ['Impacts', 'Proximity alarm'], 'pic': 'images_operators_def/Wamai.png'}
Oryx = {'name': 'Oryx', 'loadout_main': ['SPAS-12', 'T-5 SMG'], 'loadout_secondary': ['BAILIFF 410', 'USP40'], 'secondary_gadget': ['Barbed wire', 'Proximity alarm'], 'pic': 'images_operators_def/Oryx.png'}
Melusi = {'name': 'Melusi', 'loadout_main': ['MP5', 'Super 90'], 'loadout_secondary': ['RG15'], 'secondary_gadget': ['C4', 'Impacts'], 'pic': 'images_operators_def/Melusi.png'}
Aruni = {'name': 'Aruni', 'loadout_main': ['P10 RONI', 'MK 14 EBR'], 'loadout_secondary': ['PRB92'], 'secondary_gadget': ['Barbed Wire', 'Bulletproof camera'], 'pic': 'images_operators_def/Aruni.png'}

r6_ops_defence = [Smoke, Mute, Castle, Pulse, Doc, Rook, Tachanka, Kapkan, Bandit, Jager, Frost, Valkyrie, Caveira, Echo
                  , Mira, Ela, Lesion, Vigil, Maestro, Alibi, Clash, Kaid, Mozzie, Warden, Goyo, Wamai, Oryx, Melusi, Aruni]

kafe_dostoevskiy = {'name': 'kafe dostoevskiy','points': ['1f','2f', '3f'],'spawnpoints':['River Docks', 'Christmas Market', 'Park'], 'img': 'images/kafe_dostoevskiy.jpg'}
border = {'name': 'border','points': ['2f','1f'], 'spawnpoints':['East Vehicle Entrance', 'Valley', 'West Vehicle Exit'],'img': 'images/border.jpg'}
chalet = {'name': 'chalet','points': ['2F','1F', 'Basement'], 'spawnpoints':['Campfire', 'Cliffside', 'Lakeside'],'img': 'images/chalet.jpeg'}
clubhouse = {'name': 'clubhouse','points': ['2F','1F', 'Basement'], 'spawnpoints':['Main Gate', 'Warehouse', 'Shipping dock', 'Construction site'],'img': 'images/clubhouse.jpeg'}
coastline = {'name': 'coastline','points': ['2f','1f'], 'spawnpoints':['Main Entrance', 'Pool Side', 'Ruins'],'img': 'images/coastline.png'}
outback = {'name': 'outback','points': ['1f','2f'], 'spawnpoints':['Fuel Pumps', 'Storage yard', 'Camping'],'img': 'images/outback.jpg'}
kanal = {'name': 'kanal','points': ['2F','1F', 'Basement'], 'spawnpoints':['SailBoats', 'Floating Docks', 'Construction site'],'img': 'images/kanal.jpg'}
oregon = {'name': 'oregon','points': ['2F','1F', 'Basement'], 'spawnpoints':['Street', 'Junkyard', 'Construction site'],'img': 'images/oregon.jpg'}
theme_park = {'name': 'theme park','points': ['2f','1f'], 'spawnpoints':['Main Entrance', 'Bumper Cars', 'Teacups'],'img': 'images/theme_park.jpg'}
consulate = {'name': 'consulate','points': ['2F','1F', 'Basement'], 'spawnpoints':['Police Line', 'Side Entrance', 'Gas Station', 'Riot Barricade'],'img': 'images/consulate.png'}
villa = {'name': 'villa','points': ['2f','1f'], 'spawnpoints':['Main Road', 'Ruins', 'Fountain'],'img': 'images/villa.jpeg'}
house = {'name': 'house','points': ['2F','1F', 'Basement'], 'spawnpoints':['APC Area', 'Front Street', 'Side Street'],'img': 'images/house.png'}
bank = {'name': 'bank','points': ['2F','1F', 'Basement'], 'spawnpoints':['Parking Front', 'Jewelry Front', 'Alley Access'],'img': 'images/bank.png'}
hereford_base = {'name': 'hereford base','points': ['3F','2F','1F', 'Basement'], 'spawnpoints':['Control Tower', 'Spitfire Courtyard', 'Shooting Range'],'img': 'images/hereford_base.jpg'}
skyscraper = {'name': 'skyscraper','points': ['2F','1F'], 'spawnpoints':['Helipad', 'Tower', 'Ventilation Units'],'img': 'images/skyscraper.png'}
fortress = {'name': 'fortress','points': ['2F','1F'], 'spawnpoints':['Main Gate', 'Parking', 'Garden', 'Stable'],'img': 'images/fortress.jpg'}
presidential_plane = {'name': 'presidential plane','points': ['2F','1F'], 'spawnpoints':['Main Entrance', 'Reporter Entrance', 'Front Service Entrance'],'img': 'images/presidential_plane.jpg'}
yacht = {'name': 'yacht','points': ['4F','3F','2F','1F'], 'spawnpoints':['Submarine', 'Zodiac', 'Snowmobiles'],'img': 'images/yacht.jpg'}
tower = {'name': 'tower','points': ['2F','1F'], 'spawnpoints':['North Roof', 'South Roof'],'img': 'images/tower.jpg'}
favela = {'name': 'favela','points': ['3F','2F','1F'], 'spawnpoints':['Rooftops', 'Market', 'School Alley'],'img': 'images/favela.jpg'}
bartlett_university = {'name': 'bartlett university','points': ['2F','1F'], 'spawnpoints':['Main Gate', 'Festival', 'Courtyard'],'img': 'images/bartlett_university.jpg'}

r6_maps = [kafe_dostoevskiy, border, chalet, clubhouse, coastline, consulate, outback, kanal, oregon, theme_park, villa,
           house, bank, hereford_base, skyscraper, fortress, bartlett_university, favela, tower, presidential_plane, yacht]

copper1 = {"name": "Copper 1", "img": "images_ranks/copper1.png", "start": 1500, "end": 1599}
copper2 = {"name": "Copper 2", "img": "images_ranks/copper2.png", "start": 1400, "end": 1499}
copper3 = {"name": "Copper 3", "img": "images_ranks/copper3.png", "start": 1300, "end": 1399}
copper4 = {"name": "Copper 4", "img": "images_ranks/copper4.png", "start": 1200, "end": 1299}
copper5 = {"name": "Copper 5", "img": "images_ranks/copper5.png", "start": 1100, "end": 1199}
bronze1 = {"name": "Bronze 1", "img": "images_ranks/bronze1.png", "start": 2000, "end": 2099}
bronze2 = {"name": "Bronze 2", "img": "images_ranks/bronze2.png", "start": 1900, "end": 1999}
bronze3 = {"name": "Bronze 3", "img": "images_ranks/bronze3.png", "start": 1800, "end": 1899}
bronze4 = {"name": "Bronze 4", "img": "images_ranks/bronze4.png", "start": 1700, "end": 1799}
bronze5 = {"name": "Bronze 5", "img": "images_ranks/bronze5.png", "start": 1600, "end": 1699}
silver1 = {"name": "Silver 1", "img": "images_ranks/silver1.png", "start": 2500, "end": 2599}
silver2 = {"name": "Silver 2", "img": "images_ranks/silver2.png", "start": 2400, "end": 2499}
silver3 = {"name": "Silver 3", "img": "images_ranks/silver3.png", "start": 2300, "end": 2399}
silver4 = {"name": "Silver 4", "img": "images_ranks/silver4.png", "start": 2200, "end": 2299}
silver5 = {"name": "Silver 5", "img": "images_ranks/silver5.png", "start": 2100, "end": 2199}
gold3 = {"name": "Gold 3", "img": "images_ranks/gold3.png", "start": 2600, "end": 2799}
gold2 = {"name": "Gold 2", "img": "images_ranks/gold2.png", "start": 2800, "end": 2999}
gold1 = {"name": "Gold 1", "img": "images_ranks/gold1.png", "start": 3000, "end": 3199}
plat3 = {"name": "Platinum 3", "img": "images_ranks/plat3.png", "start": 3200, "end": 3599}
plat2 = {"name": "Platinum 2", "img": "images_ranks/plat2.png", "start": 3600, "end": 3999}
plat1 = {"name": "Platinum 1", "img": "images_ranks/plat1.png", "start": 4000, "end": 4399}
diamond = {"name": "Diamond", "img": "images_ranks/diamond.png", "start": 4400, "end": 4999}
champion = {"name": "Champion", "img": "images_ranks/champion.png", "start": 5000, "end": 10000}

ranks = [copper1, copper2, copper3, copper4, copper5, bronze1, bronze2, bronze3, bronze4, bronze5, silver1, silver2,
         silver3, silver4, silver5, gold3, gold2, gold1, plat3, plat2, plat1, diamond, champion]

mini_games = []
maps_deleted = []
widgets_maps_deleted = []
r6_players = []
team_1 = []
team_2 = []
added_minigames_widgets = []


class About_me(BoxLayout):
    def yt(self):
        webbrowser.open("https://www.youtube.com/channel/UCTm5Qb8ryDW-oLdNO8z3htQ/videos")

    def inst(self):
        webbrowser.open("https://www.instagram.com/ezzzz4/")

    def dnt(self):
        webbrowser.open("https://www.donationalerts.com/r/ezzzz4")


class BL_Rank(BoxLayout):
    img = ObjectProperty()
    ran = ObjectProperty()
    mmr = ObjectProperty()

    def rank(self):
        r = choice(ranks)
        self.ran.text = r["name"]
        self.img.source = r["img"]
        self.mmr.text = str(randint(r["start"], r["end"])) + " MMR"


class BL_Match(BoxLayout):
    beg = ObjectProperty()
    en = ObjectProperty()
    count = ObjectProperty()
    winr = ObjectProperty()

    def random_count(self):
        try:
            n1 = int(self.beg.text)
            n2 = int(self.en.text)
        except ValueError:
            toast("there should be a number, not something else")
        else:
            if n1 > n2:
                toast("start must be more than end")
            elif n2 > 10:
                toast("number of matches must be less than 10")
            else:
                i = randint(n1, n2)
                self.count.text = "Number of Matches: " + str(i) + " matches"
                self.winr.text = "Win will be with: " + str(i // 2 + 1) + " points"


class BL_mini_s(BoxLayout):
    tf = ObjectProperty()
    minigames = ObjectProperty()

    def clear_games(self):
        if len(mini_games) == 0:
            toast("There is nothing to clear")
        else:
            for j in added_minigames_widgets:
                self.minigames.remove_widget(j)
            added_minigames_widgets.clear()
            mini_games.clear()

    def add_mini_game(self):
        if self.tf.text == "":
            toast("You can't add empty minigame")
        elif len(self.tf.text) > 30:
            toast("Input must be less than 30 letters")
        elif len(mini_games) > 20:
            toast("You can only add 20 mini games")
            self.tf.text = ''
        else:
            mini_games.append(self.tf.text)
            k = MDFillRoundFlatButton(text=str(self.tf.text), size_hint=[1, 1])
            added_minigames_widgets.append(k)
            self.minigames.add_widget(k)
            self.tf.text = ''


class BL_mini(BoxLayout):
    minigame = ObjectProperty()

    def random_mini_game(self):
        if len(mini_games) == 0:
            toast("add minigames and when you do that, comeback here")
        else:
            i = choice(mini_games)
            self.minigame.font_style = "H5"
            self.minigame.text = str(i)


class BL_Map_s(BoxLayout):
    gl_maps = ObjectProperty()

    def delete_map(self, map_name):
        for i in r6_maps:
            if i["name"] == map_name.text:
                maps_deleted.append(i)
                r6_maps.remove(i)
                widgets_maps_deleted.append(map_name)
                self.gl_maps.remove_widget(map_name)

    def reset_maps(self):
        if len(r6_maps) == 21:
            toast("There is nothing to clear")
        else:
            for j in widgets_maps_deleted:
                self.gl_maps.add_widget(j)
            for k in maps_deleted:
                r6_maps.append(k)
            widgets_maps_deleted.clear()
            maps_deleted.clear()


class BL_Map(BoxLayout):
    mp = ObjectProperty()
    point = ObjectProperty()
    spawn = ObjectProperty()
    img = ObjectProperty()

    def random_map(self):
        if len(r6_maps) == 0:
            toast("There are no maps to return")
        else:
            i = randint(1, len(r6_maps))
            map = r6_maps[i - 1]
            self.mp.text = str(map['name'])
            p = map['points']
            k = randint(1, len(p))
            self.point.text = p[k - 1]
            s = map['spawnpoints']
            n = randint(1, len(s))
            self.spawn.text = s[n - 1]
            self.img.source = str(map['img'])


class BL_op_d(BoxLayout):
    img = ObjectProperty()
    lbl = ObjectProperty()
    lbl_lm = ObjectProperty()
    lbl_ls = ObjectProperty()
    lbl_sg = ObjectProperty()

    def operator_defence(self):
        i = randint(1, len(r6_ops_defence))
        defender = r6_ops_defence[i - 1]
        self.lbl.text = str(defender['name'])
        d = defender['loadout_main']
        k = randint(1, len(d))
        self.lbl_lm.text = d[k - 1]
        d_1 = defender['loadout_secondary']
        n = randint(1, len(d_1))
        self.lbl_ls.text = d_1[n - 1]
        d_2 = defender['secondary_gadget']
        h = randint(1, len(d_2))
        self.lbl_sg.text = d_2[h - 1]
        self.img.source = defender['pic']


class BL_op_a(BoxLayout):
    img = ObjectProperty()
    lbl = ObjectProperty()
    lbl_lm = ObjectProperty()
    lbl_ls = ObjectProperty()
    lbl_sg = ObjectProperty()

    def operator_attack(self):
        i = randint(1, len(r6_ops_attack))
        attacker = r6_ops_attack[i - 1]
        self.lbl.text = str(attacker['name'])
        att = attacker['loadout_main']
        k = randint(1, len(att))
        self.lbl_lm.text = att[k - 1]
        att_1 = attacker['loadout_secondary']
        n = randint(1, len(att_1))
        self.lbl_ls.text = att_1[n - 1]
        att_2 = attacker['secondary_gadget']
        h = randint(1, len(att_2))
        self.lbl_sg.text = att_2[h - 1]
        self.img.source = attacker['pic']

class BL_Team(BoxLayout):
    pl1 = ObjectProperty()
    pl2 = ObjectProperty()
    pl3 = ObjectProperty()
    pl4 = ObjectProperty()
    pl5 = ObjectProperty()
    pl6 = ObjectProperty()
    pl7 = ObjectProperty()
    pl8 = ObjectProperty()
    pl9 = ObjectProperty()
    pl10 = ObjectProperty()
    ti1 = ObjectProperty()
    ti2 = ObjectProperty()
    ti3 = ObjectProperty()
    ti4 = ObjectProperty()
    ti5 = ObjectProperty()
    ti6 = ObjectProperty()
    ti7 = ObjectProperty()
    ti8 = ObjectProperty()
    ti9 = ObjectProperty()
    ti10 = ObjectProperty()

    def team(self):
        if len(self.ti1.text) > 15 or len(self.ti2.text) > 15 or len(self.ti3.text) > 15 or len(self.ti4.text) > 15 or len(
                self.ti5.text) > 15 or len(self.ti6.text) > 15 or len(self.ti7.text) > 15 or len(self.ti8.text) > 15 or len(
                self.ti9.text) > 15 or len(self.ti10.text) > 15:
            toast("Input must be less than 15 letter")
        else:
            r6_players.append(self.ti1.text)
            r6_players.append(self.ti2.text)
            r6_players.append(self.ti3.text)
            r6_players.append(self.ti4.text)
            r6_players.append(self.ti5.text)
            r6_players.append(self.ti6.text)
            r6_players.append(self.ti7.text)
            r6_players.append(self.ti8.text)
            r6_players.append(self.ti9.text)
            r6_players.append(self.ti10.text)
            c = 9
            shuffle(r6_players)
            for _ in range(5):
                n = randint(0, c)
                team_1.append(r6_players[n])
                r6_players.remove(r6_players[n])
                c -= 1
            shuffle(r6_players)
            for _ in range(5):
                n = randint(0, c)
                team_2.append(r6_players[n])
                r6_players.remove(r6_players[n])
                c -= 1
            self.pl1.text = team_1[0]
            self.pl2.text = team_1[1]
            self.pl3.text = team_1[2]
            self.pl4.text = team_1[3]
            self.pl5.text = team_1[4]
            self.pl6.text = team_2[0]
            self.pl7.text = team_2[1]
            self.pl8.text = team_2[2]
            self.pl9.text = team_2[3]
            self.pl10.text = team_2[4]

            team_1.clear()
            team_2.clear()


class BL(BoxLayout):
    pass


class Main(Screen):
    pass


class MainApp(MDApp):

    def on_start(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = 'Green'
        self.theme_cls.theme_style = "Dark"

    def build(self):
        return Main()

if __name__ == "__main__":
    MainApp().run()
