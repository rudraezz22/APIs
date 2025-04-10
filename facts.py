import requests


url1 = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_fact():
    response = requests.get(url1)
    if response.status_code == 200:
        p = response.json()
        print(f"Here is a fact : {p['text']}")
    else:
        print("error occured")

def main():

    while True:
     user_input1 = input("Press enter to continue and press q to exit").strip().lower()
     if user_input1 == "q":
       exit()
     else:
        get_fact()

main()
        
     

