from flask import Flask, make_response, json, request
from order_data_type import OrderDataType



app = Flask(__name__)

@app.route('/')
def index():
    return "hi test"

@app.route('/webhook', methods=['POST'])
def webhook():
    return make_response(json.dumps(result()))


def result():
    req = request.get_json(force=True)
    print("req : ", req)

    queryText = req.get("queryResult").get("queryText")
    print("queryText : ", queryText)

    test_response = OrderDataType.response_type[queryText]
    displayType_response = req.get("queryResult").get("intent").get("displayName")
    print(test_response)

    respText = {
        "fulfillmentMessages": [
            {
                "text":{
                    "text":[
                        "자료구조 : {} \n displayName : {}".format(test_response, displayType_response)
                    ]
                }
            }
        ]
    }

    return respText

if __name__ == "__main__":
    app.run(port=8070)