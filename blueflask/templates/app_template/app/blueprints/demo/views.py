from flask import jsonify, request
from flask.views import MethodView


# View function example
def demo():
    return '<h1>demo</h1>'


# Class based view example
class About(MethodView):
    def get(self):
        return jsonify({
            'title': 'About Blue Flask',
            'body': 'This is the GET response.',
            'args': request.args.copy(),
            'something_else': 42
        })
