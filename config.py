worlds["world"] = "/home/zacharydubois/render/worlds/world"
worlds["nether"] = "/home/zacharydubois/render/worlds/world_nether"
worlds["end"] = "/home/zacharydubois/render/worlds/world_the_end"
worlds["hoth"] = "/home/zacharydubois/render/worlds/hoth"
worlds["amp"] = "/home/zacharydubois/render/worlds/amp"
worlds["oldworld"] = "/home/zacharydubois/render/worlds/old_world"
worlds["oldnether"] = "/home/zacharydubois/render/worlds/old_world_nether"
worlds["oldend"] = "/home/zacharydubois/render/worlds/old_world_the_end"


def townFilter(poi):
    if poi["id"] == "Town":
        if not "name" in poi:
            poiName = "&lt;unnamed town&gt;"
        else:
            poiName = poi["name"]
        poiDescription=poiName
        if "region" in poi:
            poiName+=", "+poi["region"]
            poiDescription+=",\n"+poi["region"]+"\n"
        if "mayor" in poi:
            poiDescription+="Mayor: "+poi["mayor"]+"\n"
        elif "owner" in poi:
            poiDescription+="Owner: "+poi["owner"]+"\n"
        if "description" in poi:
            poiDescription+="\n"+poi["description"]
        return (poiName,poiDescription)

def publicZombieShelterFilter(poi):
    if poi["id"] == "Zombie Shelter":
        poiName = poi["name"]
        poiDescription="<b>"+poiName+"</b>\n"
        if "owner" in poi:
            poiDescription+="Owner: "+poi["owner"]+"\n"
        if "description" in poi:
            poiDescription+=poi["description"]
        return (poiName,poiDescription)

def publicChestFilter(poi):
    if poi["id"] == "Public Chest":
        poiName = poi["name"]
        poiDescription="<b>"+poiName+"</b>\n"
        if "owner" in poi:
            poiDescription+="Owner: "+poi["owner"]+"\n"
        if "description" in poi:
            poiDescription+=poi["description"]
        return (poiName,poiDescription)

def publicCobblestoneGeneratorFilter(poi):
    if poi["id"] == "Cobblestone Generator":
        if "name" in poi:
            poiName = poi["name"]
        else:
            poiName = "Cobblestone Generator"
        poiDescription="<b>"+poiName+"</b>\n"
        if "owner" in poi:
            poiDescription+="Owner: "+poi["owner"]+"\n"
        if "description" in poi:
            poiDescription+=poi["description"]
        return (poiName,poiDescription)

def publicFarmFilter(poi):
    if poi["id"] == "Public Farm":
        if "name" in poi:
            poiName = poi["name"]
        else:
            poiName = "Public Farm"
        poiDescription="<b>"+poiName+"</b>\n"
        if "owner" in poi:
            poiDescription+="Owner: "+poi["owner"]+"\n"
        if "description" in poi:
            poiDescription+=poi["description"]
        return (poiName,poiDescription)

def userHouseFilter(poi):
    if poi["id"] == "User House":
        if "name" in poi:
            poiName = poi["name"]
        else:
            poiName = "User House"
        poiDescription="<b>"+poiName+"</b>\n"
        if "owner" in poi:
            poiDescription+="Owner: "+poi["owner"]+"\n"
        if "description" in poi:
            poiDescription+=poi["description"]
        return (poiName,poiDescription)

def miscFilter(poi):
    if poi["id"] == "Misc":
        poiName = poi["name"]
        poiDescription="<b>"+poiName+"</b>\n"
        if "owner" in poi:
            poiDescription+="Owner: "+poi["owner"]+"\n"
        if "description" in poi:
            poiDescription+=poi["description"]
        return (poiName,poiDescription)

freeforall="Free for all to use"

#Points of Intrest for "world"
places_world=[
    #Towns
    {"id":"Town","x":-218,"y":70,"z":-1320,"name":"Caberpan"},
    {"id":"Town","x":-413,"y":63,"z":-1675,"name":"Overlake"},
    {"id":"Town","x":-937,"y":72,"z":-1898,"name":"unnamed, formerly Bowlshaft"},
    {"id":"Town","x":-14,"y":72,"z":-2,"name":"Upper Unicorn","mayor":"Zachary_DuBois"},
    {"id":"Town","x":-664,"y":65,"z":660,"name":"Lower Unicorn"},
    {"id":"Town","x":-347,"y":64,"z":-2344,"name":"Halfway Point"},
    {"id":"Town","x":545,"y":79,"z":511,"name":"Petra"},
    {"id":"Town","x":-690,"y":64,"z":-1211}
    {"id":"Town","x":349,"y":66,"z":3076}
    {"id":"Town","x":1483,"y":65,"z":3266}
    {"id":"Town","x":-699,"y":71,"z":1351}
    {"id":"Town","x":-1179,"y":71,"z":1127}
    {"id":"Town","x":-1880,"y":73,"z":1172}
    {"id":"Town","x":-2440,"y":66,"z":1060}
    {"id":"Town","x":-2715,"y":65,"z":578}
    {"id":"Town","x":-1706,"y":72,"z":-1197}
    {"id":"Town","x":-808,"y":65,"z":-683}
    {"id":"Town","x":-491,"y":72,"z":-3944}
    {"id":"Town","x":1373,"y":67,"z":-3883}
    {"id":"Town","x":1810,"y":67,"z":-939}
    #Public Zombie shelters
    {"id":"Zombie Shelter","x":-92,"y":77,"z":-433,"name":"Northern Unicorn Zombie Shelter"},
    #Public farms
    {"id":"Public Farm","x":-28,"y":79,"z":-44,"owner":"Town of Upper Unicorn"},
    #Public chests
    {"id":"Public Chest","x":-4,"y":77,"z":-43,"name":"Upper Unicorn Public Chests","owner":"Town of Upper Unicorn"},
    #Cobblestone Generators
    {"id":"Cobblestone Generator","x":-12,"y":77,"z":31,"owner":"Compy_McKitties","description":freeforall},
    # Houses
    {"id":"User House","x":20,"y":79,"z":-62,"name":"The home of Zachary_DuBois","owner":"Zachary_DuBois"},
    {"
    #Miscellaneous points of interest
    {"id":"Misc","x":-6,"y":76,"z":-22,"name":"Zachary DuBois Department of Transportation - world headquarters","owner":"ZDBDOT"}
]

#List of destination types
townsDict=dict(name="User house", icon="icons/marker_user_house.png", filterFunction=townFilter,checked=True)
townsDict=dict(name="Towns", icon="icons/marker_town.png", filterFunction=townFilter,checked=True)
sheltersDict=dict(name="Public zombie shelters", icon="icons/marker_tower.png",filterFunction=publicZombieShelterFilter)
farmsDict=dict(name="Public farms", icon="icons/marker_hoe.png", filterFunction=publicFarmFilter)
chestsDict=dict(name="Public chests", icon="icons/marker_chest.png",filterFunction=publicChestFilter)
cobbleDict=dict(name="Cobblestone generators", icon="icons/marker_cobblestone_generator.png", filterFunction=publicCobblestoneGeneratorFilter)
miscDict=dict(name="Miscellaneous",icon="icons/marker_misc.png", filterFunction=miscFilter)

defaultDestinationList=[townsDict,sheltersDict,farmsDict,chestsDict,cobbleDict,miscDict]


renders["worldday"] = {
    "world": "world",
    "title": "World Daytime",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    "manualpois":places_world,
    "markers": defaultDestinationList,
}
renders["worldnight"] = {
    "world": "world",
    "title": "World Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
    "manualpois":places_world,
    "markers": defaultDestinationList,
}
renders["worldcave"] = {
    "world": "world",
    "title": "World Caves",
    "rendermode": cave,
    "dimension": "overworld",
    "manualpois":places_world,
    "markers": defaultDestinationList,
}


renders["nether"] = {
    "world": "nether",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
renders["nethercave"] = {
    "world": "nether",
    "title": "Nether Caves",
    "rendermode": cave,
    "dimension": "nether",
}


renders["end"] = {
    "world": "end",
    "title": "End",
    "rendermode": smooth_lighting,
    "dimension": "end",
}
renders["endcave"] = {
    "world": "end",
    "title": "End Caves",
    "rendermode": cave,
    "dimension": "end",
}


renders["hothday"] = {
    "world": "hoth",
    "title": "Hoth Daytime",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}
renders["hothnight"] = {
    "world": "hoth",
    "title": "Hoth Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}
renders["hothcave"] = {
    "world": "hoth",
    "title": "Hoth Caves",
    "rendermode": cave,
    "dimension": "overworld",
}


renders["ampday"] = {
    "world": "amp",
    "title": "Amplified Daytime",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}
renders["ampnight"] = {
    "world": "amp",
    "title": "Amplified Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}
renders["ampcave"] = {
    "world": "amp",
    "title": "Amplified Caves",
    "rendermode": cave,
    "dimension": "overworld",
}


renders["oldworldday"] = {
    "world": "oldworld",
    "title": "Old World Daytime",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}
renders["oldworldnight"] = {
    "world": "oldworld",
    "title": "Old World Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}
renders["oldworldcave"] = {
    "world": "oldworld",
    "title": "Old World Caves",
    "rendermode": cave,
    "dimension": "overworld",
}


renders["oldnether"] = {
    "world": "oldnether",
    "title": "Old Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
renders["oldnethercave"] = {
    "world": "oldnether",
    "title": "Old Nether Caves",
    "rendermode": cave,
    "dimension": "nether",
}


renders["oldend"] = {
    "world": "oldend",
    "title": "Old End",
    "rendermode": smooth_lighting,
    "dimension": "end",
}
renders["oldendcave"] = {
    "world": "oldend",
    "title": "End Caves",
    "rendermode": cave,
    "dimension": "end",
}


outputdir = "/home/zacharydubois/render/done"
texturepath = "/home/zacharydubois/render/texturepack.zip"
