#!/usr/bin/env python3

# processes data from the model and hands it to the router.
# Heavy logic/lifting should be done here or by helpers of controllers (e.g. engines)

import json
from api import db
from api.models.owner import Owner
from api.schemas.owner import OwnerSchema
from marshmallow import ValidationError
from api.common.http import OkRequest, BadRequest

import hashlib


class OwnerController():
    def getList():
        return OkRequest(OwnerSchema(many=True).dump(Owner.query.all()))

    def getOwner(id):
        return OkRequest(OwnerSchema().dump(Owner.query.get(id)))

    def create(respJson):
        try:
            valid = OwnerSchema().load(respJson)
        except ValidationError as e:
            return BadRequest(e.messages)
        else:
            h = str(hashlib.md5(valid['password'].encode()))
            o = Owner(firstname=valid['firstname'],
                      lastname=valid['lastname'],
                      username=valid['username'],
                      email=valid['email'],
                      password_hash=h,
                      city=valid['city'],
                      state=valid['state'],
                      zip_code=valid['zip_code'],
                      )
            db.session.add(o)
            db.session.commit()
            return OkRequest(OwnerSchema().dump(o))

    def delete(id):
        o = Owner.query.get(id)
        db.session.delete(o)
        db.session.commit()
        return OkRequest("Deleted")
