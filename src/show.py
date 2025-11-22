import webbrowser
from src.search import search

query = input("Search for: ")

results = search(query, 5)

print("\nShowing top results:\n")
for path in results:
    print(path)
    webbrowser.open(path)
