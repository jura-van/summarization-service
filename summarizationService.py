import json

from newspaper import Article
from newspaper.configuration import Configuration


def summarizeArticles(toSummarize):
    result = []

    for source in toSummarize:
        article = Article(source)

        article.download()
        article.parse()
        article.nlp()

        sum_to_return = {'title': article.title,
                         'summary': article.summary,
                         'authors': article.authors,
                         'keywords': article.keywords,
                         'source': source}

        result.append(sum_to_return)

    return json.dumps(result)
