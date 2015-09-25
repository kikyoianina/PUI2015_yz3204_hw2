import json
import sys
import urllib2

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.load(request)
    
    vehicleActivity = data['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']
    number_bus = len(vehicleActivity)
    print 'Bus Line : %s' % sys.argv[2]
    print 'Number of Active Buses : %s' % number_bus
    for i in range(number_bus):
        Latitude = vehicleActivity[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Latitude']
        Longitude = vehicleActivity[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Longitude']    
        print 'Bus %s is at latitude %s and longitude %s' % (i, Latitude, Longitude)