
@app.route('/login', methods=['POST'])
def login():
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )

    user = UserInfo.query \
        .filter_by(email=auth.get('email')) \
        .first()

    if not user:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        # JWT Token
        token = jwt.encode({
            'userId': user.userId,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password !"'}
    )


# signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.form

    firstName, lastName, email, password, phoneNumber = data.get('firstName'), data.get('lastName'), data.get(
        'email'), data.get('password'), data.get('phoneNumber')

    user = UserInfo.query \
        .filter_by(email=email) \
        .first()
    if not user:
        # database ORM object
        user = UserInfo(
            userId=uuid.uuid4(),
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        return make_response('Successfully registered.', 201)
    else:
        return make_response('User already exists. Please Log in.', 202)