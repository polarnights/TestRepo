from flask import Flask, request, jsonify, make_response, abort
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'HIDDEN'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'HIDDEN'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'admin':
        return '1234'
    elif username == 'nickoliger':
        return 'mypwd2022'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'Error': 'Unauthorized access'}), 401)


users = [
    {
        'first_name': "Vasily",
        'last_name': "Petrov",
        'middle_name': "Sergeevich",
        'phone_number': "79091234567",
        'track': 1,
        'age': 'UNKNOWN',
        'citizenship': 'UNKNOWN'
    },
    {
        'first_name': "Anton",
        'last_name': "Romanov",
        'middle_name': "Alexandrovich",
        'phone_number': "79993827117",
        'track': 2,
        'age': 'UNKNOWN',
        'citizenship': 'UNKNOWN'
    },
    {
        'first_name': "Semyon",
        'last_name': "Skvortsov",
        'middle_name': "Nikolayevich",
        'phone_number': "79631228923",
        'track': 3,
        'age': 'UNKNOWN',
        'citizenship': 'UNKNOWN'
    },
    {
        'first_name': "Nick",
        'last_name': "Oliger",
        'middle_name': "Alexandrovich",
        'phone_number': "79631227145",
        'track': 4,
        'age': 'UNKNOWN',
        'citizenship': 'UNKNOWN'
    },
    {
        'first_name': "Tester",
        'last_name': "Tested",
        'middle_name': "Test",
        'phone_number': "42",
        'track': 5,
        'age': 'UNKNOWN',
        'citizenship': 'UNKNOWN'
    },
]


@app.route('/teremok/get_users', methods=['GET'])
@auth.login_required
def get_users():
    return jsonify({'users': users})


@app.route('/teremok/users/<string:phone_number>', methods=['GET'])
@auth.login_required
def get_user(phone_number):
    user = list(filter(lambda t: t['phone_number'] == phone_number, users))
    if not user:
        abort(404)
    return jsonify({'user': user[0]})


@app.route('/teremok/create_user', methods=['POST'])
@auth.login_required
def create_user():
    if not request.json or not 'first_name' in request.json or not 'last_name' in request.json or not 'phone_number' in request.json:
        abort(400)
    user = {
        'phone_number': request.json['phone_number'],
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'middle_name': request.json.get('middle_name', ""),
        'track': request.json.get('track', 1),
        'age': request.json.get('age', "UNKNOWN"),
        'citizenship': request.json.get('citizenship', "UNKNOWN")
    }
    users.append(user)
    return jsonify({'user': user}), 201


@app.route('/teremok/update_info', methods=['PUT'])
@auth.login_required
def update_user():
    if not request.json or not 'phone_number' in request.json or not 'age' in request.json or not 'citizenship' in request.json:
        abort(400)
    user = list(filter(lambda t: t['phone_number'] == request.json['phone_number'], users))
    if not user:
        abort(404)
    user[0]['age'] = request.json['age']
    user[0]['citizenship'] = request.json['citizenship']
    return jsonify({'user': user[0]})


@app.route('/teremok/delete_user/<string:phone_number>', methods=['DELETE'])
@auth.login_required
def delete_task(phone_number):
    user = list(filter(lambda t: t['phone_number'] == phone_number, users))
    if not user:
        abort(404)
    users.remove(user[0])
    return jsonify({'DELETE': "Successfully deleted user!"})


if __name__ == "__main__":
    app.run(debug=True)
