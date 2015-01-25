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

def privateZombieShelterFilter(poi):
    if poi["id"] == "Private Zombie Shelter":
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
        poiName = poi["name"]
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
    {"id":"Town","x":-937,"y":72,"z":-1898,"name":"Bowlshaft"},
    {"id":"Town","x":-14,"y":72,"z":-2,"name":"Upper Unicorn"},
    {"id":"Town","x":-664,"y":65,"z":660},
    #Public Zombie shelters
    {"id":"Zombie Shelter","x":-92,"y":77,"z":-433,"name":"Northern Unicorn Zombie Shelter"},
    #Public farms
    {"id":"Public Farm","x":-28,"y":79,"z":-44,"owner":"Town of Upper Unicorn"},
    #Public chests
    {"id":"Public Chest","x":-4,"y":77,"z":-43,"name":"Upper Unicorn Public Chests","owner":"Town of Upper Unicorn"},
    #Cobblestone Generators
    {"id":"Cobblestone Generator","x":-12,"y":77,"z":31,"owner":"Compy_McKitties","description":freeforall},
    #Miscellaneous points of interest
    {"id":"Misc","x":-6,"y":76,"z":-22,"name":"Zachary DuBois Department of Transportation - world headquarters","owner":"ZDBDOT"}
]

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
renders["worlddaysouth"] = {
    "world": "world",
    "title": "World Daytime South",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    "northdirection" : "lower-right",
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
renders["worldnightsouth"] = {
    "world": "world",
    "title": "World Nighttime South",
    "rendermode": smooth_night,
    "dimension": "overworld",
    "northdirection" : "lower-right",
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
renders["nethersouth"] = {
    "world": "nether",
    "title": "Nether South",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
    "northdirection" : "lower-right",
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
renders["endsouth"] = {
    "world": "end",
    "title": "End South",
    "rendermode": smooth_lighting,
    "dimension": "end",
    "northdirection" : "lower-right",
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
renders["hothdaysouth"] = {
    "world": "hoth",
    "title": "Hoth Daytime South",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    "northdirection" : "lower-right",
}
renders["hothnight"] = {
    "world": "hoth",
    "title": "Hoth Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}
renders["hothnightsouth"] = {
    "world": "hoth",
    "title": "hoth Nighttime South",
    "rendermode": smooth_night,
    "dimension": "overworld",
    "northdirection" : "lower-right",
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
renders["ampdaysouth"] = {
    "world": "amp",
    "title": "Amplified Daytime South",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    "northdirection" : "lower-right",
}
renders["ampnight"] = {
    "world": "amp",
    "title": "Amplified Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}
renders["ampnightsouth"] = {
    "world": "amp",
    "title": "Amplified Nighttime South",
    "rendermode": smooth_night,
    "dimension": "overworld",
    "northdirection" : "lower-right",
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
renders["oldworlddaysouth"] = {
    "world": "oldworld",
    "title": "Old World Daytime South",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    "northdirection" : "lower-right",
}
renders["oldworldnight"] = {
    "world": "oldworld",
    "title": "Old World Nighttime",
    "rendermode": smooth_night,
    "dimension": "overworld",
}
renders["oldworldnightsouth"] = {
    "world": "oldworld",
    "title": "Old World Nighttime South",
    "rendermode": smooth_night,
    "dimension": "overworld",
    "northdirection" : "lower-right",
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
renders["oldnethersouth"] = {
    "world": "oldnether",
    "title": "Old Nether South",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
    "northdirection" : "lower-right",
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
renders["oldendsouth"] = {
    "world": "oldend",
    "title": "End South",
    "rendermode": smooth_lighting,
    "dimension": "end",
    "northdirection" : "lower-right",
}
renders["oldendcave"] = {
    "world": "oldend",
    "title": "End Caves",
    "rendermode": cave,
    "dimension": "end",
}


outputdir = "/home/zacharydubois/render/done"
texturepath = "/home/zacharydubois/render/texturepack.zip"
