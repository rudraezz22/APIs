import requests
from colorama import Fore , Style , init

init(autoreset = True)

api_key = "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"

default_model = "google/pegasus-xsum"

def build_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"

def query(payload, model_name = default_model):
    api_url = build_url(model_name)
    headers = {"Authorization" : f"Bearer {api_key}"}
    response = requests.post(api_url, headers=headers, json=payload)


    if response.status_code == 200:
        try:
           return response.json()
        except ValueError:
            print("failed to genrate response from api")
            print(f"{response.text}")
            return None
    else:
        print(f"API call failed with status {response.status_code}")
        print(f"Response content: {response.text}")
        return None
    
def summary_text(text , min_length , max_length , model = default_model ):
    payload = {
        "inputs":text,
        "parameters":{"min_length" : min_length , "max_length":max_length}

    }
    print(f"performin AI summarization with {model}")

    result = query(payload , model_name = model)
    if isinstance(result , list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print("error in summarization response")
        print(result)
        return None
    
if __name__ == "__main__":
    print("HELLO! WELCOME TO AI SUMMARY BOT")
    user_name = input("enter a username").strip()
    if not user_name:
        user_name = "user"
    print(f"Welcome! {user_name} give text and see the magic")
    user_text = input().strip()
    if not user_text:
        print("no text provided please provide a text")

    else:
        print("enter the model u want to choose")
        model_choice = input("enter your choice").strip()
        if not model_choice:
            model_choice = default_model
        print("choose a sumarization style for the input")
        print("1  for quick and consize , and 2 for more detailed and refined")
        style_choice = input("enter your style choice from 1 or 2").strip()
         
        if style_choice == "1":
            min_length = 80
            max_length = 240
            print("quick and consize explanantion")
        else:
            min_length = 250
            max_length = 500
            print("detailed and more refined explanantion")

        summary = summary_text(user_text , min_length , max_length , model = model_choice)
        if summary:
            print(f"your AI generated summary is{summary}")
        else:
            print("no summary was able to be genrated")


    
    


