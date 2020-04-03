from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource , reqparse
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:pass@localhost/pure_sql'+ os.path.join(basedir,'postgres.postgresql')
api = Api(app)


Computers = [
    {
        "id" : 1,
        "hard_drive_type" : "ssd",
        "processor" : "intel dual core",
        "amount_ram" : "5GB",
        "max_ram" : "64B",
        "hard_drive_size" :"1TB",
        "form_factor" : "mini"
    },
     {
         "id" :2,
        "hard_drive_type" : "hdd",
        "processor" : "amd",
        "amount_ram" : "8GB",
        "max_ram" : "16",
        "hard_drive_size" : "500GB",
        "form_factor" : "medium"
    },
     {
         "id" :3,
        "hard_drive_type" : "ssd",
        "processor" : "intel atom",
        "amount_ram" : "2GB",
        "max_ram" : "16GB",
        "hard_drive_size" : "256GB",
        "form_factor" : "medium"
    }
]
 
class Computer_api(Resource):
    def get(self, name): # READ
        for Computer in Computers:
            if(name == Computer["computer_name"]):
                return Computer,200
        return "Computer not found" ,404


    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Computers</h1>
        <p>A prototype API for Umuzi Computers.</p>'''

    @app.route('/api/v1/resources/Computers/all', methods=['GET'])
    def api_all(): 
        conn = postgres.connect('Computers.pure_sql')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_Computers = cur.execute('SELECT * FROM Computers;').fetchall()

        return jsonify(all_Computers)

    def read():
        return [Computers[key] for key in sorted(Computers.keys())]

    def post(self, name): 
        parser  = reqparse.RequestParser()
        parser.add_argument("hard_drive_type")
        parser.add_argument("processor")
        parser.add_argument("amount_ram")
        parser.add_argument("max_ram")
        parser.add_argument("hard_drive_size")
        parser.add_argument("form_factor")
        args = parser.parse_args()


        for Computer in Computers:
                Computer["hard_drive_type"] = args["hard_drive_type"]
                Computer["processor"] = args["processor"]
                Computer["amount_ram"] = args["amount_ram"]
                Computer["max_ram"] = args["max_ram"]
                Computer["hard_drive_size"] = args["hard_drive_size"]
                Computer["form_factor"] = args["form_factor"]
                return Computer, 200

        Computer = {
            "hard_drive_type" : args["hard_drive_type"],
            "processor" : args["processor"],
            "amount_ram" : args["amount_ram"],
            "max_ram" : args["max_ram"],
            "hard_drive_size" : args["hard_drive_size"],
            "form_factor" : args["form_factor"]
        }
        Computers.append(Computer)
        return Computer, 201

    def put(self, name): 
        parser  = reqparse.RequestParser()
        parser.add_argument("hard_drive_type")
        parser.add_argument("processor")
        parser.add_argument("amount_ram")
        parser.add_argument("max_ram")
        parser.add_argument("hard_drive_size")
        parser.add_argument("form_factor")
        args = parser.parse_args()


        for Computer in Computers:
            if(name == Computer["computer_name"]):
                Computer["hard_drive_type"] = args["hard_drive_type"]
                Computer["processor"] = args["processor"]
                Computer["amount_ram"] = args["amount_ram"]
                Computer["max_ram"] = args["max_ram"]
                Computer["hard_drive_size"] = args["hard_drive_size"]
                Computer["form_factor"] = args["form_factor"]
                return Computer, 200

        Computer = {
            "computer_name" : name,
             "hard_drive_type" : args["hard_drive_type"],
             "processor" : args["processor"],
             "amount_ram" : args["amount_ram"],
             "max_ram" : args["max_ram"],
             "hard_drive_size" : args["hard_drive_size"],
             "form_factor" : args["form_factor"]
        }
        Computers.append(Computer)
        return Computer, 201

    def delete(self, name): # Delete
        global Computers
        Computers = [Computer for Computer in Computers if Computer["computer_name"] != name]
        return "<h1>404</h1><p>The resource could not be found.</p>", 404

    @app.route('/api/v1/resources/computer', methods=['GET'])
    def api_id():
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."

        results = []

        for Computer in Computers:
            if Computer['id'] == id:
                results.append(Computer)
        return jsonify(results)

app.run()
api.add_resource(Computer_api, "/computer/<string:name>")
app.run(debug=True)