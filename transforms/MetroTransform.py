import json

def addMetroNames(team):
    for area in team['default']['geoMapData']:
        for feature in metro_json['features']:
            properties = feature['geometry']['properties']

            if (properties['id'] == 'US-' + area['geoCode']):
                if ('name' in properties.keys()): continue
                properties['name'] = area['geoName']


with open('../basemaps/metro.json', 'r') as f:
    metro_json = json.load(f)


with open('../misc/pittsburgh_steelers.json', 'r') as f:
    steelers = json.load(f)

with open('../misc/san_francisco_49ers.json', 'r') as f:
    niners = json.load(f)

with open('../misc/dallas_cowboys.json', 'r') as f:
    boys = json.load(f)

with open('../misc/miami_dolphins.json', 'r') as f:
    fins = json.load(f)



addMetroNames(boys)
addMetroNames(steelers)
addMetroNames(niners)
addMetroNames(boys)


for feature in metro_json['features']:
    coords = feature['geometry']['coordinates']

    for first in coords:
        for second in first:
            second.reverse()

    feature['geometry']['coordinates'] = coords

with open('metros.json', 'w') as outfile:
    json.dump(metro_json, outfile)
