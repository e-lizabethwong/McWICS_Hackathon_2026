import requests
username = input("Enter Instagram username: ")
print(requests.get(f"http://10.69.34.59:5000/scrape_instagram?username={username}").json())
