from django.core.management.base import BaseCommand, CommandError
from weatherdata.models import Post, Weather
import httplib

class Command(BaseCommand):

        def handle(self, *args, **options):
                parameters = {"Tmax","Tmin","Tmean","Sunshine","Rainfall"}
                locations = {"UK","England","Wales","Scotland"}
                count = 0;
                for l in locations:
                    print l
                    #for p in parameters:
                    connection = httplib.HTTPConnection("www.metoffice.gov.uk")
		    url = "/pub/data/weather/uk/climate/datasets/"+"Tmax"+"/date/"+l+".txt"
	            #print url
		    connection.request("GET", url)
		    r1 = connection.getresponse()
	            #print r1.status, r1.reason
         	    max_temp = r1.read()
		    url = "/pub/data/weather/uk/climate/datasets/"+"Tmin"+"/date/"+l+".txt"
	            #print url
		    connection.request("GET", url)
		    r1 = connection.getresponse()
	            #print r1.status, r1.reason
         	    min_temp = r1.read()
         	    url = "/pub/data/weather/uk/climate/datasets/"+"Tmean"+"/date/"+l+".txt"
	            #print url
		    connection.request("GET", url)
		    r1 = connection.getresponse()
	            #print r1.status, r1.reason
         	    mean_temp = r1.read()
         	    url = "/pub/data/weather/uk/climate/datasets/"+"Sunshine"+"/date/"+l+".txt"
	            #print url
		    connection.request("GET", url)
		    r1 = connection.getresponse()
	            #print r1.status, r1.reason
         	    sunshine = r1.read()
         	    url = "/pub/data/weather/uk/climate/datasets/"+"Rainfall"+"/date/"+l+".txt"
	            #print url
		    connection.request("GET", url)
		    r1 = connection.getresponse()
	            #print r1.status, r1.reason
         	    rainfall = r1.read()
         	    connection.close()
		    max_temperature=max_temp
                    min_temperature=min_temp
                    mean_temperature=mean_temp
                    rainfall=rain_fall
                    sunshine=sunshine_hrs
