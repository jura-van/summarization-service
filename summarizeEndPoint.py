from flask import Flask, request

from summarizationService import summarize_articles

app = Flask(__name__)


@app.route("/summarize", methods=['POST'])
def summarize():
    return summarize_articles(request.get_json()['links'])


if __name__ == "__main__":
    app.run(host="127.0.0.1")
