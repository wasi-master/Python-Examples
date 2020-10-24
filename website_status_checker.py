import requests # We use the requests module to make a web request
# pythom -m pip install requests

url = input("Enter a website address: ") # We get the url


try: # We try in case there is a error while getting that url
    r = requests.get(url) # We get the website
except Exception as e: # We catch the error
    print(str(e)) # We print the string representation of the error
    exit() # We exit out of the code


if r.status_code == 200: # If all went right
    print("Website all ok") # We say website is okay
else: # If something went wrong
    print("Website not ok, response code: " + r.status_code) # We say website errored