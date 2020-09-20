from flask import Flask
from flask_restplus import Api, fields

app = Flask(__name__)
api = Api(app, version="0.1", title="AppAddress API",
          description="kubernetes service ip를 애조로 도메인으로 할당해줍니다.")
ns = api.namespace('api', 'restful api')

model = api.model('DNS', {
    'id': fields.Integer(readonly=True, description='Azr Domain ID'),
    'name': fields.String(required=True, description='Azr Domain name recorded'),
    'ip': fields.String(required=True, description='Azr Domain member IP')
})
