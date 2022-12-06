import json
import requests

gpt3_url = \
    "https://api.openai.com/v1/completions"

gpt3_headers = \
    {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }

def get_paraphrase(sentence):

    gpt3_payload = \
        {
            "model": "text-davinci-003",
            "prompt": "The following is an original sentence followed by a paraphrased version of it" +
                      "with a diverse choice of words:" +
                      "\n\noriginal: We should all strive to be better stewards of the planet." +
                      "\nparaphrase: We should all endeavor to look after the Earth more responsibly." +
                      "\n###" +
                      "\noriginal: " + sentence +
                      "\nparaphrase:",
            "temperature": 0.5,
            "max_tokens": 100,
            "top_p": 1,
            "frequency_penalty": 0.72,
            "presence_penalty": 0.72,
            "stop": ["###"]
        }

    response = requests.request("POST", gpt3_url, headers=gpt3_headers, json=gpt3_payload).json()
    paraphrased_sentence = response['choices'][0]['text'].strip()
    return paraphrased_sentence

def lambda_handler(event, context):

    raw_string = r'{}'.format(event['body'])
    body = json.loads(raw_string)
    originaltext = body['text']
    paraphrased_text = get_paraphrase(originaltext)

    print("original text: " + originaltext)
    print("paraphrased text: " + paraphrased_text)

    output = \
        {
            "paraphrased": paraphrased_text
        }

    return {
        "statusCode": 200,
        "body": json.dumps(output),
    }
