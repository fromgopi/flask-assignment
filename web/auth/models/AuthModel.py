from web import db
from web.commons.helper.AuthHelper import generate_hash_for_password


class AuthModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    isAdmin = db.Column(db.SmallInteger, nullable=True)

    def create_user(self, payload):
        self._create_authmodel_object(payload)
        user_data = {}
        try:
            self.password = generate_hash_for_password(self.password)
            db.session.add(self)
            db.session.commit()
            user_data = {"id": self.id, "email": payload['email'], 'code': 200}
            return user_data
        except Exception as e:
            print(e)
            user_data['code'] = 422
            return user_data

    def check_for_user(self, email):
        return AuthModel.query.filter_by(email=email).first()

    def check_user_by_id(self, id):
        return AuthModel.query.filter_by(id=id).first()

    def _create_authmodel_object(self, payload):
        self.email = payload['email']
        self.name = payload['name']
        self.password = payload['password']
        self.isAdmin = payload['isAdmin']

