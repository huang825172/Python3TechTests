from flask import Flask
import flask_restful as restful
from win10toast import ToastNotifier

app = Flask(__name__)
api = restful.Api(app)


class Helloworld(restful.Resource):
    def get(self):
        return {'hello': 'world'}


class ToSendMessage(restful.Resource):
    def get(self, todo_str):
        toaster = ToastNotifier()
        toaster.show_toast(todo_str, todo_str, 'favicon.ico')


api.add_resource(Helloworld, '/')
api.add_resource(ToSendMessage, '/<string:todo_str>')


def restfulTmain():
    # app.run(debug=True)
    app.run()