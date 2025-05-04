import requests
api_key = "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"
MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

headers = {"Authorization":f"Bearer {api_key}"}

def caption_img():
    image = "test.png"
    try:
        with open(image, "rb" ) as var:
           abcd = var.read()
    except Exception as e:
        print(f"the image could not be loaded{image} with exception {e}")
        return 
    response = requests.post(API_URL , headers = headers , data = abcd)
    result = response.json()

    if isinstance(result , dict) and "error" in result:
        print(result["error"])
        return
    caption = result[0].get("generated_text" , "no text generated")
    print("image:",image)
    print(caption)

caption_img()