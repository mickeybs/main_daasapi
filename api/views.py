from django.shortcuts import render
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RainPrediction(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']        
        model = ApiConfig.model  

        rain_predicted = model.predict([[year, month, day, tmax]])  
        
        return Response(rain_predicted, status=200)

class RainPrediction_DE(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']  
        model2 = ApiConfig.model2
               
        rain_predicted2 = model2.predict([[year, month, day, tmax]]) 
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(rain_predicted2, status=200)

class RainPrediction_YJ(APIView):
    def post(self, request):
        data = request.data
        year = data['year']
        month = data['month']
        day = data['day']
        tmax = data['tmax']
        model3 = ApiConfig.model3           
        rain_predicted3 = model3.predict([[year, month, day, tmax]])          
        # response_dict = {"Predicted if there is rain for 3 month": rain_predicted}
        return Response(rain_predicted3, status=200)





