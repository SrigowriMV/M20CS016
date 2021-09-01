from flask import Flask, render_template, request, redirect,url_for
from bson import ObjectId 
from pymongo import MongoClient 


app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

client = MongoClient("mongodb+srv://dbuser:12345@cluster0.rwb3t.mongodb.net/podcastDatabase?retryWrites=true&w=majority")
db = client.podcastDatabase
episodeCollection = db.episodeCollection


template = "index.html"
def redirect_url():    
    return request.args.get('next') or  request.referrer or  url_for('index')  


@app.route("/displayAll")
def listAllEpisodes():
    allEpisodes = episodeCollection.find()    
    return render_template(template,episodes=allEpisodes,a1="active") 

@app.route("/displayFinished")
def listFinishedEpisodes():
    finishedEpisodes = episodeCollection.find({"status":True})
    return render_template(template,episodes=finishedEpisodes,a3="active")

@app.route("/")
def listUnfinishedEpisodes():
    unfinishedEpisodes = episodeCollection.find({"status":False})
    return render_template(template,episodes=unfinishedEpisodes,a2="active")

@app.route("/update")
def update():
    id=request.values.get("_id")    
    episode=episodeCollection.find({"_id":ObjectId(id)})    
    episodeCollection.update({"_id":ObjectId(id)}, {"$set": {"status":not episode[0]["status"]}})    
    return redirect(redirect_url() )     

@app.route("/addEpisode",methods=['POST'])
def addEpisode():
    title = request.values.get("title")
    date = request.values.get("date")
    duration = request.values.get("duration")
    status = False 
    host = request.values.get("host")
    description=request.values.get("description")  

    episodeCollection.insert({"title":title,
                            "date":date,
                            "duration":duration,
                            "status":status,
                            "host":host,
                            "description":description})
    
    return redirect("/displayAll")

@app.route("/removeEpisode",methods=['GET'])
def removeEpisode():
    id = request.values.get("_id")
    print(id)
    episodeCollection.remove({"_id":ObjectId(id)})
    return redirect("/")

@app.route("/updateEpisode")
def updateEpisode():
    name=request.values.get("title")    
    description=request.values.get("description")    
    date=request.values.get("date")       
    id=request.values.get("_id")   
    host = request.values.get("host") 
    episodeCollection.update({"_id":ObjectId(id)}, {'$set':{ "name":name, "description":description, "date":date,"host":host }})    
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


