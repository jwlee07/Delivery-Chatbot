from flask import Flask, render_template, request

import os
from google.cloud import dialogflow_v2 as dfw
from google.api_core.exceptions import InvalidArgument

from collections import OrderedDict

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index_page_landing():
    if request.method == "POST":
        pass
    else:
        dialog = conversation_chatbot()
        return render_template('renewal_index.html', context=dialog)

#terminal에서 대화형 챗봇 흉내내기
def conversation_chatbot():
    keys = []
    values = []

    requestText = input("request text : ")
    respText = ""

    while(requestText != 'quit'):
        respText = chatbot_request(requestText)
        keys.append(requestText) #request text
        values.append(respText) #response text
        requestText = input("request text : ")

    dialog = OrderedDict({key:val for key, val in zip(keys, values)})
    return dialog

def chatbot_request(txtInput):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'deliverychatbot-uflj-318c727647a6.json'

    DIALOGFLOW_PROJECT_ID = 'deliverychatbot-uflj'
    DIALOGFLOW_LANGUAGE_CODE = 'ko'
    SESSION_ID = 'mine'


    text_to_be_analyzed = txtInput

    session_client = dfw.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dfw.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dfw.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print("Query Text : ", response.query_result.query_text)
    print("Detected intent : ", response.query_result.intent.display_name)
    print("Detected intent confidence : ", response.query_result.intent_detection_confidence)
    print("Fulfillment text : ", response.query_result.fulfillment_text)

    return response.query_result.fulfillment_text


if __name__ == "__main__":
    #실행 시
    #PermissionError: [Errno 13] Permission denied: '/var/folders/4w/7mc0wn_x6hg10_bw1777w_qc0000gn/T/ngrok/ngrok'
    #해당 폴더로 가서 chmod -R 775 ngrok
    '''
    이것도 안될 시,
    run_with_ngrok(app) 주석처리
    '''
    app.run()
