from flask import Flask, request
from summarize import summarizationService

app = Flask(__name__)


@app.route("/summarize", methods=['POST'])
def summarize():
    return summarizeArticles(request.get_json()['links'])


if __name__ == "__main__":
    app.run(host="127.0.0.1")
