from django.core.management.base import BaseCommand, CommandError
from weatherdata.models import Post, Weather 
import httplib

class Command(BaseCommand):

        def handle(self, *args, **options):
                parameters = {"Tmax","Tmin","Tmean","Sunshine","Rainfall"}
                locations = {"UK","England","Wales","Scotland"}
                count = 0;
                for l in locations:
                    for p in parameters:
                        connection = httplib.HTTPConnection("www.metoffice.gov.uk")
		        url = "/pub/data/weather/uk/climate/datasets/"+p+"/date/"+l+".txt"
		        #print url
		        connection.request("GET", url)
		        r1 = connection.getresponse()
		        #print r1.status, r1.reason
		        weather_data = r1.read()
		        #print weather_data
		        weather_filename = p+"_"+l+".txt"
		        weather_file = open(weather_filename, 'w')
		        weather_file.truncate()
		        weather_file.write(weather_data)
		        weather_file.close()
		        connection.close()


