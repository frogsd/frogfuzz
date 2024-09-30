#!/usr/bin/python

import requests
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)  

def fuzz_endpoint(url, wordlist_file):
    with open(wordlist_file, 'r') as file:
        fuzz_data = file.readlines()

    with open("ok.txt", 'a') as ok_file:
        for data in tqdm(fuzz_data, desc="Fuzzing", unit="request"):
            data = data.strip()
            if data:
                try:
                    response = requests.get(url + data)
                    print(f"Testing {url + data}: Status code: {response.status_code}")
                    if response.status_code == 200:
                        success_message = f"{Fore.GREEN}Success: {url + data}{Style.RESET_ALL}"
                        print(success_message)  
                        ok_file.write(url + data + '\n')
                except requests.exceptions.RequestException as e:
                    print(f"{Fore.RED}Error checking {url + data}: {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}FrogSec - Fuzzing Tool{Style.RESET_ALL}")
    url_to_check = input("Enter the URL to check (e.g., https://example.com): ")
    wordlist_file = "worldlist.txt"
    fuzz_endpoint(url_to_check, wordlist_file)

if __name__ == "__main__":
    main()
