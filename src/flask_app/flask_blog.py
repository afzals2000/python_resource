import os
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)
posts = [
            {
                "author":"peter pane",
                "title" : "Blog Post 1",
                "content" : "First post content",
                "date_posted" : "April 1, 2019"
            },
            {
                "author":"jamie",
                "title" : "Blog Post 2",
                "content" : "second post content",
                "date_posted" : "April 2, 2019"
            }
]

##########################################################################
#flask
##########################################################################
@app.route("/")
@app.route("/home")
def home():                                 # =>http://0.0.0.0:5000/home
    return render_template("home.html", posts=posts)

@app.route("/about")                        # => http://0.0.0.0:5000/about
def about():
    str = jsonify({"about": "Page"})
    print(type(str))
    print(str)
    return str


##########################################################################
#flask_restful
##########################################################################

class HelloWorld(Resource):
    def get(self):                          # => http://0.0.0.0:5000/HelloWorld
        return {"about": "Hello World"}

    def post(self):  # => curl -H "Content-Type: application/json" -X POST -d '{"name":"xyz","address":"Address xyz"}' http://0.0.0.0:5000/HelloWorld
        some_json = request.get_json()
        return {"you sent": some_json}, 201 # default return code is 200, it can be overridden

class Multi(Resource):
    def get(self, num):                     # => http://0.0.0.0:5000/multi/10
        return {"result": num*10}

api.add_resource(HelloWorld, "/HelloWorld")
api.add_resource(Multi, "/multi/<int:num>")


##########################################################################
#main
##########################################################################
if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT",5000)) #Get port from env var or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
