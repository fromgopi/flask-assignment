from web import db
from web.auth.models.AuthModel import AuthModel


class PropertyModel(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50), nullable=False)
    dimension = db.Column(db.String(50), nullable=False)
    createdBy = db.Column(db.INTEGER, nullable=False)

    # This method is to add Property.
    def add_property(self, payload):
        self._populate_property_model_object(payload)
        try:
            db.session.add(self)
            db.session.commit()
            return {'name': self.type, 'code': 200, 'msg': 'Property Added'}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {'code': 422, 'msg': 'Unable to add at this point of time'}

    def search_for_property(self, type, dimension):
        return db.session \
            .query(PropertyModel.type.label('property_type'), PropertyModel.dimension.label('property_dimension')) \
            .join(AuthModel, AuthModel.id == PropertyModel.createdBy) \
            .filter(PropertyModel.type == type, PropertyModel.dimension == dimension).all()

    def search_for_property_by_dim_range(self, type, dimA, dimB):
        return db.session \
            .query(PropertyModel.type.label('property_type'), PropertyModel.dimension.label('property_dimension')) \
            .join(AuthModel, AuthModel.id == PropertyModel.createdBy) \
            .filter(PropertyModel.type == type, PropertyModel.dimension.between(dimA, dimB)).all()

    def _populate_property_model_object(self, payload):
        self.type = payload['type']
        self.dimension = payload['dimension']
        if 'createdBy' in payload:
            self.createdBy = payload['createdBy']
