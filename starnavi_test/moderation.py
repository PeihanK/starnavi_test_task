from transformers import pipeline

toxicity_model = pipeline('text-classification', model='unitary/toxic-bert')


def toxic_content(content):
    result = toxicity_model(content)
    print(f"Model result: {result}")
    return result[0]['score'] > 0.6