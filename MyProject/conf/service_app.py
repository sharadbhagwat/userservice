import django


django.setup()
from flask import Flask, request
from flask_restful import Api, Resource

from MyProject.service_apis.userapi import UserApi
from MyProject.service_apis.loginapi import LoginApi

app = Flask(__name__)
api = Api(app, prefix='/userservice/')

api.add_resource(UserApi, 'user', 'user/<username>')
api.add_resource(LoginApi,'login','login/<token>')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
