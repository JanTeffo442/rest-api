from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/umuzi_inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
ma = Marshmallow(app)


#create a database model
class Computers(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	hard_drive_type = db.Column(db.String(50))
	processor = db.Column(db.String(50))
	amount_of_ram = db.Column(db.String(30))
	maximum_ram = db.Column(db.String(50))
	hard_drive_space = db.Column(db.String(30))
	form_factor = db.Column(db.String(40))

	def __init__(self, hard_drive_type, processor, amount_of_ram, maximum_ram, hard_drive_space, form_factor):
		self.hard_drive_type = hard_drive_type
		self.processor = processor
		self.amount_of_ram = amount_of_ram
		self.maximum_ram = maximum_ram
		self.hard_drive_space = hard_drive_space
		self.form_factor = form_factor

#db.create_all()


class ComputerSchema(ma.Schema):
	class Meta:
		fields = ("hard_drive_type", "processor", "amount_of_ram", "maximum_ram", "hard_drive_space", "form_factor")

computer_schema = ComputerSchema()
computers_schema = ComputerSchema(many = True)



@app.route('/get', methods = ['GET'])
def get_post():
	return jsonify({'Hello':'World'})


@app.route('/add_computer', methods = ['POST'])
def add_computer():
	hard_drive_type = request.json['hard_drive_type']
	processor = request.json['processor']
	amount_of_ram = request.json['amount_of_ram']
	maximum_ram = request.json['maximum_ram']
	hard_drive_space = request.json['hard_drive_space']
	form_factor = request.json['form_factor']

	computer = Computers(hard_drive_type, processor, amount_of_ram, maximum_ram, hard_drive_space, form_factor)
	db.session.add(computer)
	db.session.commit()

	return computers_schema.jsonify(computer)


@app.route('/get_all', methods = ['GET'])
def all_computers():
	all_pcs = Computers.query.all()
	result = computers_schema.dump(all_pcs)

	return jsonify(result)


@app.route('/get_by_id/<id>/', methods = ['GET'])
def get_by_id(id):
	single_computer = Computers.query.get(id)

	return computers_schema.jsonify(single_computer)


if __name__ == "__main__":
	app.run(debug=True)