
import requests
he_api_key= "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"
def abcd(text):
    api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    header = {"Authorization":  f"Bearer {he_api_key}"}
    payload = {"inputs":text}
    response = requests.post(api_url , headers= header, json= payload)
    return response.json()

def main():
    sample_text = "HI I AM NOT GOOD!"
    result = abcd(sample_text)
    print(result)

main()
    