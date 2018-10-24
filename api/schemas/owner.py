#!/usr/bin/env python3
from marshmallow import Schema, fields
from api.schemas.dog import DogSchema

class OwnerSchema(Schema):
	id = fields.Int(dump_only=True)
	username = fields.String(required=True)
	email = fields.Email(required=True)
	firstname = fields.String(required=True)
	lastname = fields.String(required=True)
	city = fields.String(required=True)
	state = fields.String(required=True)
	zip_code = fields.String(required=True)
	password = fields.String(required=True, load_only=True)
	dogs = fields.Nested(DogSchema, many=True)

