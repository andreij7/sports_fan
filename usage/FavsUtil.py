from shapely.geometry import Point
import json
from shapely.geometry import Polygon as SPolygon
from shapely.geometry import MultiPolygon as MPolygon
from shapely.geometry import shape
from matplotlib import pyplot
from descartes import PolygonPatch

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def loadBaseMap(fileName):
    with open('../basemaps/%s.json'%fileName, 'r') as f:
        return json.load(f, object_hook=_byteify)

def loadFansZip(fileName):
    with open('../sports/%s_fans_zip.json' % fileName, 'r') as f:
        return json.load(f, object_hook=_byteify)

def loadFansMetro(fileName):
    with open('../sports/%s_fan_metro.json' % fileName, 'r') as f:
        return json.load(f, object_hook=_byteify)

def zipFans(location):
    retVal = {}

    zipCodes = loadBaseMap('zipcodes')

    for feature in zipCodes['features']:
        s = shape(feature['geometry'])

        try:
            polygon = SPolygon(s)
        except:
            polygon = MPolygon(s)

        zip = feature['properties']['zip']

        if (location.within(polygon)):
            location = polygon.centroid
            ncaaf_favs = loadFansZip('ncaaf')
            mlb_favs = loadFansZip('mlb')

            try:
                retVal['ncaaf'] = ncaaf_favs[zip]
            except:
                pass

            try:
                retVal['mlb'] = mlb_favs[zip]
            except:
                pass

    return (retVal, location)

def metroFans(location, returnDict):
    metros = loadBaseMap('metros')

    for feature in metros['features']:
        s = shape(feature['geometry'])

        try:
            polygon = SPolygon(s)
        except:
            polygon = MPolygon(s)

        area_name = feature['geometry']['properties']['name']

        if(area_name == 'New York NY'):
            print polygon

        if (polygon.contains(location) or polygon.touches(location)):
            nba_favs = loadFansMetro('nba')
            nfl_favs = loadFansMetro('nfl')
            nhl_favs = loadFansMetro('nhl')

            try:
                returnDict['nba'] = nba_favs[area_name]
            except:
                print 'error nba'

            try:
                returnDict['nfl'] = nfl_favs[area_name]
            except:
                print 'error nfl'

            try:
                returnDict['nhl'] = nhl_favs[area_name]
            except:
                print 'error nhl'

    return returnDict

def getFavs(location):

    retVal, location = zipFans(location)

    retVal = metroFans(location, retVal)

    return retVal


