from flask            import Flask, g
from flask_restful    import Api, Resource, reqparse, abort
from BarTender import BarTender
from Drink import drinks

import os


app  = Flask(__name__)
api  = Api(app)

glassInPlace = False

b = BarTender()


class MenuAPI(Resource):
    def get(self):
        global drinks
        global b
        menu = []
        for drink in drinks:
            if b.canMake(drink):
                menu.append(drink.name)
        return {'menu': menu}, 200

class AddQueueAPI(Resource):
    def put(self, drink_name: str):
        global glassInPlace
        global b
        global drinks

        if not glassInPlace:
            return {'error': 'No Glass. PUT to /glass'}, 403
        if drink_name not in [drink.name for drink in drinks]:
            return {'error': drink_name + ' is not a valid drink. GET from /menu to see drinks'}, 404

        for drink in drinks:
            if drink.name == drink_name:
                b.make(drink)
                break
        glassInPlace = False
        return {'sucess': 'Made drink'},200




class GlassAPI(Resource):

    def put(self):
        global glassInPlace

        glassInPlace = True
        return {'sucess': 'Placed glass'}

class DispenserListAPI(Resource):
    def get(self):
        global b
        return {'dispensers': [dispenser.name for dispenser in b.dispensers]}, 200


class ShutdownAPI(Resource):
    def put(self):
        global b
        b.shutDown()
        return {'sucess': 'Garrison Shutdown'},200


api.add_resource(MenuAPI,     '/menu', endpoint='menu')
api.add_resource(AddQueueAPI, '/queue/<string:drink_name>', endpoint='add_queue')
api.add_resource(GlassAPI,    '/glass', endpoint='glass')
api.add_resource(ShutdownAPI, '/shutdown', endpoint='shutdown')
api.add_resource(DispenserListAPI, '/dispensers', endpoint='dispensers')



if __name__ == '__main__':
    app.run(host= '0.0.0.0')
