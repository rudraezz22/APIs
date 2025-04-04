import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code ==200:
        joke_data = response.json()
        print(f"full json response {joke_data}")
        return f"{joke_data['setup']} , {joke_data['punchline']}" 
    else:
        return "an error ocurred"

def main():
    print("welcome to random joke genrator!")
    
    while True:
        user_input = input("enter your choice enter to continue or q to quit").strip().lower()
        if user_input == "q":
            exit()

        else:
           joke = get_joke()
           print(joke)

main()
