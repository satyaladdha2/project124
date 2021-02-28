from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': u'Buy groceries',
        'contact': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Learn Python',
        'contact': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Aaj mere paas gaadi hai,bungla hai,bank balance hai! Tumhare paas kya hai? Mere paas maa hai! "

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Request is unsuccessful!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True) 