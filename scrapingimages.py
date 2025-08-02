import requests
import re
import os  # used for directory creation and path handling

user = input("Enter the number: ")
user_agent = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

# Google Image Search
url = f"https://www.google.com/search?q={user}+images&tbm=isch"
response = requests.get(url, headers=user_agent).text

# Extract image links using regex
pattern = r'(\["https://[^"]+\.jpg",\d+,\d+\])'     ##for matching the https we use this code
image_urls = re.findall(pattern, response)

print(f"Total images found: {len(image_urls)}")
number_images = int(input("Enter the number of images to download: "))

if image_urls:
    if not os.path.exists(user):  # check if folder exists
        os.mkdir(user)
    os.chdir(user)  # switch to the created/download folder

    for image in image_urls[:number_images]:
        try:
            images = eval(image)[0]  # extract the image URL from the list
            img_data = requests.get(url=images, headers=user_agent).content
            image_name = images.split('/')[-1]  # get last part of URL as filename

            with open(image_name, "wb") as file:
                file.write(img_data)
            print(f"Downloaded: {image_name}")
        except Exception as e:
            print(f"Failed to download image: {e}")
