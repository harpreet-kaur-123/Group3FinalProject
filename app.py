
from flask import Flask, jsonify, request, render_template
import pymongo
from pymongo import mongo_client
import sys
print('Current python version: ', sys.version)
print('Download dependencies here: ', sys.executable)

    
app = Flask(__name__)

#client = pymongo.MongoClient("mongodb://Navjot200504868:Pass234@cluster0-shard-00-00.e0sgj.mongodb.net:27017,cluster0-shard-00-01.e0sgj.mongodb.net:27017,cluster0-shard-00-02.e0sgj.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-dmv2sm-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.weather_db
#client = pymongo.MongoClient("mongodb+srv://Navjot200504868:Pass234@cluster0.e0sgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

client = pymongo.MongoClient("mongodb+srv://HarpreetKaurPannu123:12345@cluster0.d9rhl.mongodb.net/test")
db = client.weather_db

#print(db)
table1 = db["weather_records"]
#todos=table1.find_one(sort=[( '_id', pymongo.DESCENDING )])

barchart_data =table1.find()
#print(barchart)
mystring = ""
barchart_arr=[]
linechart_arr=[]
combochart_arr=[]
scatterchart_arr=[]
barchart_arr.append(['Date','humidity'])
linechart_arr.append([0,0])
combochart_arr.append(['Date','Temp_c','Temp_f','feelslike_c'])
scatterchart_arr.append(['o3','co'])
i=0
for x in barchart_data:
	a = [x['location']['localtime'], x['current']['humidity']]
	barchart_arr.append(a)
	a2 = [i, x['current']['wind_kph']]
	linechart_arr.append(a2)
	a3 = [x['location']['localtime'], x['current']['temp_c'], x['current']['temp_f'], x['current']['feelslike_c']]
	combochart_arr.append(a3)
	a4 = [x['current']['air_quality']['o3'], x['current']['air_quality']['co']]
	scatterchart_arr.append(a4)
	i = i + 1
    #mystring+= str(x) #making string of records in the table
    
#print(barchart_arr)
@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/charts')
def charts():
    return render_template("pie-chart.html",chartdata=todos,temp_c=temp_c,temp_f=temp_f,wind_mph=wind_mph,wind_kph=wind_kph,wind_degree=wind_degree,pressure_mb=pressure_mb,pressure_in=pressure_in,precip_mm=precip_mm,precip_in=precip_in,humidity=humidity,cloud=cloud,feelslike_c=feelslike_c,feelslike_f=feelslike_f,vis_km=vis_km,vis_miles=vis_miles,gust_mph=gust_mph,gust_kph=gust_kph,name=name,region=region,country=country,localtime=localtime)

@app.route("/barchart")
def barchart():
	#return barchart_arr
    return render_template("bar-chart.html",barchart_arr=barchart_arr)

@app.route("/linechart")
def linechart():
	#return barchart_arr
    return render_template("line-chart.html",linechart_arr=linechart_arr)

@app.route("/scatterchart")
def scatterchart():
	#return barchart_arr
    return render_template("scatter-chart.html",scatterchart_arr=scatterchart_arr)

@app.route("/mapchart")
def mapchart():
	#return barchart_arr
    return render_template("map-chart.html",linechart_arr=linechart_arr)

@app.route("/combochart")
def combochart():
	#return barchart_arr
    return render_template("combo-chart.html",combochart_arr=combochart_arr)
	
if __name__ == "__main__":
    app.run()