from shapely.geometry import Point
import FavsUtil as util

jb = Point(-90.7049735, 35.8742851)
tysons = Point(-77.2185246, 38.9148015)
dallas = Point(-96.7431046,32.8527207)
la = Point(-119.7505133, 34.4249152)
ny = Point(-74.1907914, 41.560708)

points = [jb, ny]

for location in points:
    favorites = util.getFavs(location)

    print favorites

    print len(favorites.keys())

