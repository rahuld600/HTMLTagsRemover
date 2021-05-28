


from flask import Flask, jsonify, request
app = Flask(__name__)
import requests
import traceback
from bs4 import BeautifulSoup

@app.route('/')
def helloWorld():
    return "Hello World"
    
@app.route('/htmlremover', methods=["GET"])
def removeTAGS():
    try:
        website = request.args.get('site')
        page = requests.get(website)
        soup = BeautifulSoup( page.content,'html.parser')
        for data in soup(['style','script']):
            data.decompose()
        texts = ' '.join(soup.stripped_strings)
        result = {
            "PageUrl":website,
            "RawData":texts
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error" : traceback.format_exc()})


    

if __name__ == "__main__":
    app.run(debug=True)