import json

from newspaper import Article


def summarize_articles(to_summarize):
    result = []

    for source in to_summarize:
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
