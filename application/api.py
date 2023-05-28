from flask import  request,jsonify
from flask_restful import  Resource
from application.models import Marker
from main import api

class MarkerResource(Resource):
    def get(self):
        markers = Marker.objects.all()
        return markers.to_json(), 200

    def post(self):
        
        
        address = request.form.get('address')
        longitude = request.form.get('longitude')
        latitude = request.form.get('latitude')
        

        marker = Marker(address=address, longitude=longitude, latitude=latitude)
        marker.save()
        
        return marker.to_json(), 201

api.add_resource(MarkerResource, '/markers')