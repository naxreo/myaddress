from mylib import app, ns, model
from flask_restplus import Resource


@ns.route('/v1/domain')
class GetDomain(Resource):
    '''Show a list of all domain'''
    @ns.doc('list_domain')
    # @ns.marshal_with(model)
    def get(self):
        '''List all domain'''
        return "show all domain"

    @ns.doc('create_domain')
    @ns.expect(model)
    def post(self):
        '''Create a new domain'''
        return "create a new domain"

    def put(self):
        '''Modify a domain record'''
        return "modify a domain record"

    def delete(self):
        '''delete a domain'''
        return "delete a domin"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
