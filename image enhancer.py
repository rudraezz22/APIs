import requests
from PIL import Image , ImageEnhance , ImageFilter
from io import BytesIO

api_key = "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" 

api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers" # used for image genration

def img_gen(prompt:str) -> Image.Image:
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs":prompt}
    try:
        response = requests.post(api_url , headers = headers , json = payload, timeout = 30)
        response.raise_for_status()
        if "image" in response.headers.get("Content-Type" , ''):
            img = Image.open(BytesIO(response.content))
            return img
        else :
            raise Exception("the output is not an image, it might be an error")
    except requests.exception.RequestException as E:
          raise Exception(f"the exceptionn is {E}")
    
def post_process(img:Image.Image)-> Image.Image :
    enhancer = ImageEnhance.Brightness(img)
    bright = enhancer.enhance(1.2)
    enhancer = ImageEnhance.Contrast(bright)
    contrast = enhancer.enhance(1.1)

    soft_focus_img = contrast.filter(ImageFilter.GaussianBlur(radius = 5))
    return soft_focus_img

def main():
    print("Welcomme!")
    print("type exit to quit")
    while True:
        user_input = input("enter the prompt of the image u want to genrate").strip()
        if user_input.lower() == "exit":
            print("BYe!")
            break
        else:
            try:
                img1 = img_gen(user_input)
                img_enhance = post_process(img1)

                img_enhance.show()
                save_option = input("do you want to save the image? (yes/no)").strip()
                if save_option == "yes":
                    file_name = input("enter the file name without extension ").strip() or "generated_image"
                    file_name = ''.join(c for c in file_name if c.isalnum() or c in  ("-","_")).rstrip()
                    img_enhance.save(f"{file_name}.png")
                    print("image saved success")
            except Exception as e:
                print(f"an error occurred {e}")

main()

               


