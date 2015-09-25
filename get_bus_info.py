import json
import sys
import urllib2
import csv

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    data = json.load(request)
    
    vehicleActivity = data['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']
    number_bus = len(vehicleActivity)

with open(sys.argv[3], 'wb') as csvFile:
    writer = csv.writer(csvFile)
    headers = ['Latitude', 'Longitude','Stop Name', 'Stop Status']
    writer.writerow(headers)    
    
    for i in range(number_bus):
        Latitude = vehicleActivity[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Latitude']
        Longitude = vehicleActivity[i]['MonitoredVehicleJourney'][
            'VehicleLocation']['Longitude']    
        if vehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
            stopName = 'N/A'
            stopStatus = 'N/A'
        else:
            stopName = vehicleActivity[i]['MonitoredVehicleJourney'][
                'OnwardCalls']['OnwardCall'][0]['StopPointName']
            stopStatus = vehicleActivity[i]['MonitoredVehicleJourney'][
                'OnwardCalls']['OnwardCall'][0]['Extensions'] ['Distances']['PresentableDistance']
        writer.writerow([Latitude, Longitude, stopName, stopStatus])

