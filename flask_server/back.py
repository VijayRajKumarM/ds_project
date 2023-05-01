
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from joblib import load 
import pandas as pd 
import numpy as np
from datetime import datetime 
app = Flask(__name__)
model = load(r'C:\Users\vijay\deva\ui_page\flask_server\random_forest.joblib') #Loading the joblib file
hotel_model = load(r'C:\Users\vijay\deva\ui_page\flask_server\Hotel_Cost_prediction.joblib')
#food_model = load(r'')
#have to change the airfare - stops, return journey
@app.route('/convert', methods=['POST','GET']) #creating end point 
def convert():
        global target , source ,week_end_days,dto , airlines, cla  
        source = request.form['setChoice'] #fetching source city
        print(source)
        target = request.form['setChoice1'] #fetching target city
        print(target)
        airlines= request.form['setChoice2'] #fetching airlines city
        print(airlines)
        cla = request.form['setChoice3'] #fetching class 
        print(cla)
        time = request.form['setChoice4'] #fetching departure time
        print(time)
        stops = request.form['setChoice5'] #fetching no of stops
        print(stops)
        try:
            date=request.form['setChoice6']
            print(date)
        except Exception as e:
             print("THE ERROR IS ",e)
        date2 = request.form['setChoice'] #fetching return date 
        dto=datetime.strptime(date,"%Y-%m-%d") 
        dto1 = datetime.strptime(date2,"%Y-%m-%d")
        end_days = dto1 - dto 
        week_end_days = end_days.days 
        cdt=datetime.today().strftime('%Y-%m-%d') #computing current date
        cdo=datetime.strptime(cdt,"%Y-%m-%d")
        tdelta=dto-cdo #finding difference to compute no of days
        no_of_days=tdelta.days
        print(no_of_days)
        stops1=int(stops)
        print(stops1)
        dic={'days_left':[no_of_days], 'airline_AirAsia':[0], 'airline_Air_India':[0],
       'airline_GO_FIRST':[0], 'airline_Indigo':[0], 'airline_SpiceJet':[0],
       'airline_Vistara':[0], 'source_city_Bangalore':[0], 'source_city_Chennai':[0],
       'source_city_Delhi':[0], 'source_city_Hyderabad':[0], 'source_city_Kolkata':[0],
       'source_city_Mumbai':[0], 'class_Business':[0], 'class_Economy':[1],
       'departure_time_Afternoon':[0], 'departure_time_Early_Morning':[0],
       'departure_time_Evening':[0], 'departure_time_Late_Night':[0],
       'departure_time_Morning':[0], 'departure_time_Night':[0],
       'destination_city_Bangalore':[0], 'destination_city_Chennai':[0],
       'destination_city_Delhi':[0], 'destination_city_Hyderabad':[0],
       'destination_city_Kolkata':[0], 'destination_city_Mumbai':[0]} #initialising integer attributes as it is and for string attributes with 0
        dic["airline_"+airlines]=[1] #changing corresponding airline to 1
        dic["source_city_"+source]=[1] #changing corresponding source city to 1
        dic["destination_city_"+target]=[1] #changing corresponding destination city to 1
        dic["departure_time_"+time]=[1] #changing corresponding departure_time to 1
        df = pd.DataFrame(dic) #converting to a dataframe
        prediction = model.predict(df) #passing data to joblib file
        return {'prediction': str(prediction)} #returning predicted value as string
'''
@app.route('/convert1',methods = ['POST','GET'])
def convert1():
     source = request.form['setChoice'] #fetching source city
        print(source)
        target = request.form['setChoice1'] #fetching target city
        print(target)
        airlines= request.form['setChoice2'] #fetching airlines city
        print(airlines)
        cla = request.form['setChoice3'] #fetching class 
        print(cla)
        time = request.form['setChoice4'] #fetching departure time
        print(time)
        #stops = request.form['setChoice5'] #fetching no of stops
        #print(stops)
        try:
            date=request.form['setChoice6']
            print(date)
        except Exception as e:
             print("THE ERROR IS ",e)
        date2 = request.form['setChoice'] #fetching return date 
        dto=datetime.strptime(date,"%Y-%m-%d") 
        dto1 = datetime.strptime(date2,"%Y-%m-%d")
        end_days = dto1 - dto 
        week_end_days = end_days.days 
        cdt=datetime.today().strftime('%Y-%m-%d') #computing current date
        cdo=datetime.strptime(cdt,"%Y-%m-%d")
        tdelta=dto-cdo #finding difference to compute no of days
        no_of_days=tdelta.days
        print(no_of_days)
        stops1=int(stops)
        print(stops1)
        dic={'days_left':[no_of_days], 'airline_AirAsia':[0], 'airline_Air_India':[0],
       'airline_GO_FIRST':[0], 'airline_Indigo':[0], 'airline_SpiceJet':[0],
       'airline_Vistara':[0], 'source_city_Bangalore':[0], 'source_city_Chennai':[0],
       'source_city_Delhi':[0], 'source_city_Hyderabad':[0], 'source_city_Kolkata':[0],
       'source_city_Mumbai':[0], 'class_Business':[0], 'class_Economy':[1],
       'departure_time_Afternoon':[0], 'departure_time_Early_Morning':[0],
       'departure_time_Evening':[0], 'departure_time_Late_Night':[0],
       'departure_time_Morning':[0], 'departure_time_Night':[0],
       'destination_city_Bangalore':[0], 'destination_city_Chennai':[0],
       'destination_city_Delhi':[0], 'destination_city_Hyderabad':[0],
       'destination_city_Kolkata':[0], 'destination_city_Mumbai':[0]} #initialising integer attributes as it is and for string attributes with 0
        dic["airline_"+airlines]=[1] #changing corresponding airline to 1
        dic["source_city_"+source]=[1] #changing corresponding source city to 1
        dic["destination_city_"+target]=[1] #changing corresponding destination city to 1
        dic["departure_time_"+time]=[1] #changing corresponding departure_time to 1
        df = pd.DataFrame(dic) #converting to a dataframe
        prediction = model.predict(df) #passing data to joblib file
        return {'prediction': str(prediction)} #returning predicted value as string
              
@app.route('/hotel', methods=['POST','GET']) #creating end point 
def hotel():
     wifi = request.form['setChoice'] 
     print(wifi)
     if(wifi == "yes"):
        wifi=1
     else:
        wifi = 0
     breakfast = request.form['setChoice1'] 
     print(breakfast)
     if(breakfast == "yes"):
         breakfast = 1
     else:
         breakfast = 0
     star = request.form['setChoice2']
     print(star)
     isweekend = 0
     enddays = ["Sunday","Saturday"]
     week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
     ind = week.index(dto.striftime("%A"))
     for i in range(0,week_end_days):
        if(week[(ind+i)%7] in enddays):
            isweekend = 1
            break 
     print(isweekend)
     dic = {'IsWeekend':[isweekend],'StarRating':[star],'FreeWifi':[wifi],'FreeBreakFast':[breakfast],
            'HotelCapacity' :[86.3942],'CityName_Bangalore' :[0],'CityName_Chennai':[0],'CityName_Kolkata':[0],
            'CityName_Delhi':[0],'CityName_Hyderabad':[0],'CityName_Mumbai':[0]}
     dic['CityName_'+target] = [1] 
     df = pd.DataFrame(dic)
     hotel_prediction = hotel_model.predict(df)
     return {'hotel_prediction' : str(hotel_prediction)}

app.route('/food', methods=['POST','GET']) #creating end point 
def food():
        cuisines = request.form['setChoice']
        print(cuisines)
        rating = request.form['setchoice1']
        print(rating)
        dic = {'City_Bangalore':[0],'City_Chennai':[0],'City_Hyderabad':[0],'City_Kolkata':[0],'City_Mumbai':[0],
               'City_New Delhi':[0],'Cuisines_North Indian':[0],'Cuisines_Others'=[0],'Cuisines_South Indian'=[0],
               'Rating text_Average':[0],'Rating text_Excellent':[0],'Rating text_Good':[0],'Rating text_Very Good':[0],
               'Rating text_Poor':[0],'Price range':[price]}
        dic['City_'+target]=[1]
        dic['Cuisines_'+cuisines] = [1]
        dic['Rating text_'+rating] = [1]
        df = pd.DataFrame(dic)
        food_prediction = food_model.predict(df)
        return {'food':str(food_prediction)}'''    
     
if __name__ == '__main__':
    app.run(debug='True',port=5000) #running the flask server on port 5000
