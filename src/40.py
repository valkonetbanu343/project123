import requests
import os
import time

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {save_path}")
    else:
        print(f"Failed to download {url}")

def main():
    # Replace this with the actual URL of the file you want to save
    url = "https://example.com/file.txt"
    
    # Replace this with the path where you want to save the file
    save_path = "/path/to/save/file.txt"

    print(f"Downloading file from {url}...")
    download_file(url, save_path)
    time.sleep(2)  # Give the browser some time to open the page

if __name__ == "__main__":
    main()
