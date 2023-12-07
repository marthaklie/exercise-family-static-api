"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import Family
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = Family("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }

    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_a_member():
    body=request.get_json()

    first_name=body["first_name"]
    age=body["age"]
    lucky_numbers= body["lucky_numbers"]
    
    member=FamilyStructure(
            first_name = first_name,
            age = age,
            lucky_numbers =  lucky_numbers
        )

    member=jackson_family.add_member(member)

    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    # this is how you can use the Family datastructure by calling its methods
    return jsonify(response_body),200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(member_id):

    member = jackson_family.get_member(member_id)
    response_body = {
        "hello": "world",
        "family": member
    }
    return jsonify(response_body),200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):

    member = jackson_family.delete_member(member_id)
    response_body = {
        "hello": "world",
        "family": member
    }
    return jsonify(response_body),200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)