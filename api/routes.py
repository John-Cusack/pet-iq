#!/usr/bin/env python3

from flask import Flask, request
from api import app
from api.controllers.owner import OwnerController as Owner
from api.controllers.dog import DogController as Dog

v1Root = "/api/v1/"

# the heart of the api, handles routing and calls controllers

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def hello():
	return "Hi"


# Owner routes
@app.route(v1Root + "owner", methods=['GET', 'POST'])
def owner():
	if request.method == 'GET':
		return Owner.getList()
	else:
		return Owner.create(request.get_json())


@app.route(v1Root + "owner/<id>", methods=['GET','DELETE'])
def ownerId(id):
	if request.method == 'GET':
		return Owner.getOwner(id)
	else:
		return Owner.delete(id)


# Dog routes		
@app.route(v1Root + "dogs/<ownerId>", methods=['GET'])
def ownerDogs():
	if request.method == 'GET':
		return Dog.getDogs()


@app.route(v1Root + "dog", methods=['GET', 'POST'])
def dog():
	if request.method == 'GET':
		return Dog.getList()
	else:
		return Dog.create(request.get_json())


@app.route(v1Root + "dog/<id>", methods=['GET','DELETE'])
def dogId(id):
	if request.method == 'GET':
		return Dog.getOwner(id)
	else:
		return Dog.delete(id)
