
from flask import Flask, request, make_response
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# TODO - Move to config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data.sqlite'

db = SQLAlchemy(app)


'''
create table starship (
	starshipid numeric not null primary key,
	name varchar(50),
	crewsize numeric,
	shipclass varchar(50),
	launchstardate numeric );
'''
class Starship(db.Model):
    __tablename__ = 'starship'
    starshipid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    crewsize = db.Column(db.Integer)
    shipclass = db.Column(db.String(64))
    launchstardate = db.Column(db.Integer)

    def __repr__(self):
        return '<Starship %r>' % self.name


class StarshipModel(Resource):
    def get(self, starship_id):
        starship = Starship.query.filter_by(starshipid = starship_id).first()
        if starship is None:
            return make_response("no starship matching that id", 404)

        return {'starship_id': starship.starshipid, 'name':starship.name, 'crewsize':starship.crewsize, 'shipclass':starship.shipclass, 'launchstardate':starship.launchstardate}

    def post(self, starship_id):
        name_param = request.form['name']
        crewsize_param = request.form['crewsize']
        shipclass_param = request.form['shipclass']
        launchstardate_param = request.form['launchstardate']
        new_starship = Starship(starshipid=starship_id, name=name_param, crewsize=crewsize_param, shipclass=shipclass_param, launchstardate=launchstardate_param)
        db.session.add(new_starship)
        db.session.commit()
        return make_response({'starship_id': starship_id, 'name':name_param, 'crewsize':crewsize_param, 'shipclass':shipclass_param, 'launchstardate':launchstardate_param}, 201)

    def put(self, starship_id):
        starship = Starship.query.filter_by(starshipid=starship_id).first()
        if starship is not None:
            starship.name = request.form['name']
            starship.crewsize = request.form['crewsize']
            starship.shipclass = request.form['shipclass']
            starship.launchstardate = request.form['launchstardate']

            db.session.add(starship)
            db.session.commit()
            return make_response({'starship_id': starship.starshipid, 'name':starship.name, 'crewsize':starship.crewsize, 'shipclass':starship.shipclass, 'launchstardate':starship.launchstardate}, 201)
        else:
            return make_response("no starship matching that id", 404)

    def delete(self, starship_id):
        starship = Starship.query.filter_by(starshipid=starship_id).first()

        if starship is not None:
            db.session.delete(starship)
            db.session.commit()
            # return make_response({'starship_id': starship.starshipid, 'name':starship.name, 'crewsize':starship.crewsize, 'shipclass':starship.shipclass, 'launchstardate':starship.launchstardate}, 202)
            return make_response("deleted", 202)
        else:
            return make_response("no starship matching that id", 404)


api.add_resource(StarshipModel, '/<string:starship_id>')


# Create the database tables.
# db.create_all()

if __name__ == '__main__':
    app.run()




