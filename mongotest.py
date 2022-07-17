import pymongo
client = pymongo.MongoClient("mongodb+srv://shuva41:2S0H0U3V1A9N9K1A@shuva41.irwdg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Shuvankar Ray",
    "email": "machineautoshuva41@gmail.com",
    "surname": "Ray"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
