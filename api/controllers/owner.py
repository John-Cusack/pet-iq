#!/usr/bin/env python3

# processes data from the dto and hands it to the router.
# Heavy logic/lifting should be done here or by helpers of controllers (e.g. engines)

from api import db
from api.models.owner import Owner
from api.dto.owner import OwnerDTO
from api.requests.owner import OwnerRequests
import hashlib

class OwnerController():
	def getList():
		return [OwnerDTO(o) for o in Owner.query.all()]

	def getOwner(id):
		return OwnerDTO(Owner.query.get(id))

	def create(r: OwnerRequests):
		h = str(hashlib.md5(r.password.encode()))
		o = Owner(firstname="", lastname="", username=r.username, email=r.email, password_hash=h)
		db.session.add(o)
		db.session.commit()
		return OwnerDTO(o)

	def delete(id):
		o = Owner.query.get(id)
		db.session.delete(o)
		db.session.commit()
		return OwnerDTO(o)
