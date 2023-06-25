import requests
from bs4 import BeautifulSoup

# Define a dictionary of characters and their respective Wikipedia page URLs
characters = {
    'Naruto Uzumaki': 'https://naruto.fandom.com/wiki/Naruto_Uzumaki?file=Naruto_Part_II.png',
    'Sakura Haruno': 'https://naruto.fandom.com/wiki/Sakura_Haruno?file=Sakura_Part_II.png',
    'Kiba Inuzuka': 'https://naruto.fandom.com/wiki/Kiba_Inuzuka?file=Kiba_Part_II.png',
    'Kakashi Hatake': 'https://naruto.fandom.com/wiki/Kakashi_Hatake?file=Kakashi_Part_II.png',
    'Kurenai Yuhi': 'https://naruto.fandom.com/wiki/Kurenai_Y%C5%ABhi?file=Kurenai_Part_II.png',
    'Asuma Sarutobi': 'https://naruto.fandom.com/wiki/Asuma_Sarutobi?file=Asuma_Part_II.png'
}

# Iterate over the characters and fetch their profile picture URLs
for character, url in characters.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the HTML element that contains the profile picture image
    image_element = soup.find('img', {'class': 'pi-image-thumbnail'})

    if image_element:
        profile_picture_url = image_element['src']
        print(f"Character: {character}")
        print(f"Profile Picture URL: {profile_picture_url}")
        print("-----------------------------")
    else:
        print(f"Profile picture not found for {character}")
