import pymongo
import urllib
client = pymongo.MongoClient()

#Create a Database called mydatabase
mydb = client["demo_database"]

print(client.list_database_names())


mycol = mydb["first_coll"]

#Insert a document into the collection
mydict = { "id": "105", "name": "Cass" }
x = mycol.insert_one(mydict)
result=mycol.find({},{'id'})
print(result[2])
query={"name":"Dean"}
result=mycol.find({},query)
for r in result:
    print(r)
