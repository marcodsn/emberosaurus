# Example client for the server.py script
import requests

# make a get request to the server
sentence = "The quick brown fox jumps over the lazy dog"
word = "quick"
response = requests.post(
    "http://localhost:5000/synonyms", json={"sentence": sentence, "word": word}
)

# print the response
print(response.json())
