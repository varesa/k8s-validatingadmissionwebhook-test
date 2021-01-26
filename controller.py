import datetime
import json

from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods=['POST'])
def view_activity():
    data = request.json
    print(json.dumps(data, indent=4))

    uid = data['request']['uid']
    image = data['request']['object']['spec']['containers'][0]['image']

    return json.dumps({
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
          "uid": uid,
          "allowed": False,
          "status": {
            "code": 403,
            "message": f"Image {image} forbidden"
          }
        }
    })
