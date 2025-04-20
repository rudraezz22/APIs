import requests

api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
h1_read_apikey= "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"
sample_text = "i am not feeling good"
header1 = {
    "Authorization":  f"Bearer {h1_read_apikey}"

}

   
payload = {"inputs":sample_text}
response = requests.post(api_url , headers= header1, json= payload)
   

   
if response.status_code == 200:     
  result = response.json()
  print(result)
else:
  print("error")
   





    
