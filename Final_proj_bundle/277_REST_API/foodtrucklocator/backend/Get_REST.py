from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import sqlite3
import json
'''
{"username":"truckOwner1", "password":"xxxxxxx"}
'''
@api_view(['PUT'])
def truckLogin (request):
	if request.method == 'PUT':
		j = json.loads(request.body)
		connection = sqlite3.connect('FoodTruckLocator.db')
		cursor=connection.cursor()
		username=str(j['username'])
		password=str(j['password'])

		cursor.execute('SELECT trucktId from truckLogin where userName = '+'"'+username+'"'+' and password= '+'"'+password+'"')
		try:
			class_tuple=cursor.fetchall()[0][0]
		except:
			raise Http404

		connection.commit()
		connection.close()
		response = []
		try:
			response.append(class_tuple)
		except:
			raise Http404

		return Response(response)
		raise Http404



@api_view(['GET'])
def activeTrucks(request):
	if request.method == 'GET':
		connection = sqlite3.connect('FoodTruckLocator.db')
		cursor=connection.cursor()
		cursor.execute('SELECT * from truckStatus where activeFlag = ?',"Y")
		class_tuple=cursor.fetchall()
		connection.commit()
		connection.close()
		response = []
		try:
			response.append(class_tuple)
		except:
			raise Http404

		return Response(response)
		print "truck ID is"
		print truck_id
		raise Http404



'''
SAMPLE JSON for postGeoLoc API
{"TID":11111, "Mark":"N", "GeoLat":-3622.2, "GeoLong":-22.444}
'''


@api_view([ 'POST'])
def postGeoLoc(request):
	if request.method == 'POST':
		print request.body
		j = json.loads(request.body)
		print str(j['TID'])
		print str(j['Mark'])
		print str(j['GeoLat'])
		print str(j['GeoLong'])
		connection = sqlite3.connect('FoodTruckLocator.db')
		cursor=connection.cursor()
		cursor.execute('UPDATE truckStatus set activeFlag='+'"'+str(j['Mark'])+'"'+', geoLat=?, geoLong=? where trucktId=? ',(str(j['GeoLat']),str(j['GeoLong']),str(j['TID'])))
		print "cursor rowcount is "
		print cursor.rowcount
		connection.commit()
		connection.close()
		if cursor.rowcount ==1:
			return Response({'Detail': 'Data of Truck Owner Updated'})
		else:
			return Response({'Detail': 'Data of Truck Owner was not Updated'})
		
		


		raise Http404



