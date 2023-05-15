import wikipedia
import threading
import time
import sys

def animate():
    print()
    while not done:
        for c in ['|', '/', '-', '\\']:
            print('\r' + 'Searching for article ' + c + " ", end="", flush=True)
            time.sleep(0.05)
    print("\r", end="", flush=True)

print("\033[2J\033[H", end="")
topic = input("Enter a topic : ")

done = False
t = threading.Thread(target=animate)
t.start()

search_results = wikipedia.search(topic, results=5)
if not search_results:
    print(f"\nNo article found for '{topic}'")
    done = True
    t.join()
    exit()
article_title = search_results[0]
article = wikipedia.page(article_title)

with open('wiki-search-result.txt', 'w', encoding='utf-8') as f:
    f.write(f"Title: {article.title}\n\n")
    f.write(article.content)

done = True
t.join()

print('\nDone.')