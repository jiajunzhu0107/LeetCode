from marshmallow import fields, Schema


class PortSchema(Schema):
    """Port schema"""

    portId = fields.Str(attribute="portId", dump_only=True)
    name = fields.Str(attribute="name", dump_only=True)
    country = fields.Str(attribute="country", dump_only=True)
    data = fields.Str(attribute="data", dump_only=True)
