from flask            import Flask, g, render_template
from flask_restful    import Api, Resource, reqparse, abort
from BarTender        import BarTender
from Drink            import Drink, storeDrinks
from Dispenser        import Dispenser, storeDispensers

import constants
import os


app  = Flask(__name__)
api  = Api(app)


b = BarTender()


class DrinkListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, location='json')
        self.reqparse.add_argument('ingredients',  action='append', required=True, location='json')

        super(self.__class__, self).__init__()

    def get(self):
        global b
        menu = []
        for drink in b.drinks:
            if b.canMake(drink):
                menu.append(drink.name)
        return {'menu': menu}, 200

    # TODO The ingredients list doesnt work
    def post(self):
        jsonDrink = self.reqparse.parse_args()
        b.drinks.append(Drink(jsonDrink['name'], list(jsonDrink['ingredients'])))
        storeDrinks(b.drinks)
        return {'success': 'Drink added.' }, 200

class DrinkAPI(Resource):
    # def __init__(self):
    #     # self.reqparse = reqparse.RequestParser()
    #     # self.reqparse.add_argument('name', type=str, required=True, location='json')
    #
    #     super(self.__class__, self).__init__()

    def get(self, drink_name: str):
        global b

        # drink_name = self.reqparse.parse_args()['name']
        for drink in b.drinks:
            if drink.name==drink_name:
                return {'ingredients': list(drink.ingredients)}
        return {'error': 'Drink not found'}, 404


class AddQueueAPI(Resource):
    def post(self, drink_name: str):
        global b

        if not b.has_glass:
            return {'error': 'No Glass. PUT to /glass'}, 403
        if drink_name not in [drink.name for drink in b.drinks]:
            return {'error': drink_name + ' is not a valid drink. GET from /menu to see drinks'}, 404

        for drink in b.drinks:
            if drink.name == drink_name:
                b.make(drink)
                break
        b.has_glass = False
        return {'sucess': 'Made drink'},200

class GlassAPI(Resource):
    def post(self):
        global b

        b.has_glass = True
        return {'sucess': 'Placed glass'}

class DispenserListAPI(Resource):
    def __init__(self):

        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument('name',      type=str, required=True, location='json')
        self.reqparse.add_argument('type',      type=str, required=True, location='json')
        self.reqparse.add_argument('index',     type=int, required=True, location='json')
        self.reqparse.add_argument('remaining', type=int, required=True, location='json')

        super(self.__class__, self).__init__()

    def get(self):
        global b
        ret = {}
        for i, d in enumerate(b.dispensers):
            ret['d'+str(i)] =  {'name': d.name, 'remaining': d.amount}
        return {'dispensers': ret}, 200

    def post(self):
        global b
        jsonDispenser = self.reqparse.parse_args()

        name           = jsonDispenser['name']
        dispenser_type = jsonsDispenser['type']
        index          = int(jsonDispenser['index'])
        remaining      = int(jsonDispenser['remaining'])

        if (not (0 <= index < len(constants.DISPENSER_LOCATIONS))):
            return {'error': 'Invalid index. Enter 0-' + str(len(constants.DISPENSER_LOCATIONS)) }, 403

        if (dispenser_type not in ['pump', 'optic']):
            return {'error': 'Invalid dispenser type'}, 403

        b.addDispenser(name, dispenser_type, index, remaining)

        return {'sucess': 'Added the new dispenser'}, 200

class ShutdownAPI(Resource):
    def post(self):
        global b
        b.shutDown()
        return {'sucess': 'Garrison Shutdown'},200


api.add_resource(DrinkListAPI,     '/drinks',     endpoint='drinks')
api.add_resource(DrinkAPI,         '/drinks/<string:drink_name>',     endpoint='drink')
api.add_resource(AddQueueAPI,      '/queue/<string:drink_name>', endpoint='add_queue')
api.add_resource(GlassAPI,         '/glass',      endpoint='glass')
api.add_resource(ShutdownAPI,      '/shutdown',   endpoint='shutdown')
api.add_resource(DispenserListAPI, '/dispensers', endpoint='dispensers')


@app.route('/', methods=['GET'])
def homepage():
    # return render_template('index.html')
    return 'This will be the home page'

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
