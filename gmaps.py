#!Python2.
'''
Program to calculate distance between to different geographic locations
the program takes in two command line arguments i.e point of origin and destination
it the returns the distance between the two points
The point of origin is optional(in a case where its not given, the program assumes thats your physical location 
    is your point of origin and uses your ip address to find the point of origin)
usage: gmaps.py -d [destination] -o [origin]
destination = end location
origin[optionl] = prefered starting point its optional and can be ommitted
'''
import sys
import urllib2
import getopt
import json
from geolocation.main import GoogleMaps as googlemaps
from geolocation.distance_matrix.client import DistanceMatrixApiClient

gmaps = googlemaps(api_key="AIzaSyB7janFYkqPTcNDYU7jy8kTVcjDdasuG8I")
# function to calculate distance from a place using your current location
# as origin


def calDistance(argv):
    origin = ''
    dest = ''
    try:
        opts, args = getopt.getopt(argv, "d:o:", ['destination=', 'Origin= '])
    except getopt.GetoptError:
        print 'gmaps.py -o <origin> -d <destination>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-d', '--destination'):
            dest = arg
        elif opt in ('-o', '--destination'):
            origin = arg

    try:
        assert origin  # check if a value for the point of origin was provided
        # search for the origin location if origin was provided
        origin = gmaps.search(location=origin)
        origin = origin.first()
    except AssertionError:  # if not get my current location
        # get my lovation details using my ip adress
        f = urllib2.urlopen('http://freegeoip.net/json/')
        j = f.read()
        location = json.loads(j)
        try:
            origin = location['city']
            assert origin != ''  # if origin is null, value for city is null
            origin = gmaps.search(location=origin).first()
        except AssertionError:
            # use my country as the origin instaed
            origin = location['country_name']

    # google search for an adress with my destination name
    My_dest = gmaps.search(location=dest)
    My_dest = My_dest.first()
    try:  # bug hunting manenos
        distances = gmaps.distance(origin, My_dest).all()
        for each in distances:
            print ('Origin: %s' % each.origin)
            try:
                print ('Origin route: %s' % origin.route)
            except:
                pass
            print ('Destination: %s' % each.destination)
            print ('Destination route: %s' % My_dest.route)
            print('Km: %.3f' % each.distance.kilometers)
            try:
                print('miles: %.3f' % each.distance.miles)
            except TypeError:
                pass
    except:
        print 'Operation to calculate distance between the two points unsuccesfull'

if __name__ == '__main__':
    calDistance(sys.argv[1:])
