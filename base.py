import pymongo
from bson import ObjectId


class BaseShop():
    def __init__(self,classterMongo):
        self.classterMongo = classterMongo
        self.classter = pymongo.MongoClient(self.classterMongo)

    def getAllUsr(self):
        db = self.classter["TronShop"]
        Offer = db["User"]
        of = []
        cursor = Offer.find({})
        for document in cursor:
            if document["app"] is False:
                of.append(document)
        return of

    def getUsr(self,usrId):
        db = self.classter["TronShop"]
        User = db["User"]

        return User.find_one({"usrId":usrId})

    def regUser(self,usrId,address,privatekey,type):
        db = self.classter["TronShop"]
        User = db["User"]
        post = {"usrId":usrId,
                "tronAddress":address,
                "privateKey":privatekey,
                "balance":0,
                "cart":[],
                "type":type,
                "create":{}}
        User.insert_one(post)


    def createProduct(self,name,discription,price,photo):
        db = self.classter["TronShop"]
        Product = db["Product"]
        post = {"name": name,
                "discription": discription,
                "price": price,
                "photo": photo
                }
        Product.insert_one(post)

    def forCreator(self,usrId,what,whay):
        db = self.classter["TronShop"]
        User = db["User"]

        User.update_one({"usrId":usrId},{"$set":{str(what):str(whay)}})


