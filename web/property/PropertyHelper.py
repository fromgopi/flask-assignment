import json

from web import response
from web.property.models.PropertyModel import PropertyModel


class PropertyHelper:
    def post(self, payload):
        prop_model = PropertyModel()
        property_details = prop_model.add_property(payload)
        print(property_details)
        name = property_details['name']
        if property_details['code'] != 200:
            return response(property_details['msg'], property_details['code'], '')
        return response(property_details['msg'], property_details['code'], data=name)

    def search(self, payload):
        property_model = PropertyModel()
        data = {}
        if 'dimB' in payload:
            recos = property_model.search_for_property_by_dim_range(payload['type'], payload['dimA'], payload['dimB'])
            if not recos:
                return response('No result found', 200, '')
        else:
            print("Called other ")
            recos = property_model.search_for_property(payload['type'], payload['dimA'])
            if not recos:
                return response('No result found', 200, '')
        for row1, row2 in recos:
            data.setdefault(row1, []).append(row2)
        return json.dumps(data)