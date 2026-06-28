import requests
import json
import os
import time
import random 


def fetch_comments(query, subreddit, size=200):
    try:
        response = requests.get(
            "https://api.pullpush.io/reddit/search/comment",
            params={
                "q": query,
                "subreddit": subreddit,
                "size": size,
                "sort": "score",
                "sort_type": "desc",
                "score": ">5"
            },
            timeout=20
        )
        return response.json().get("data", [])
    except Exception as e:
        print(f"Failed: {query} in {subreddit} — {e}")
        return []

def is_usable(comment):
    body = comment.get("body", "")
    if body in ["[removed]", "[deleted]", ""]:
        return False
    if len(body.split()) < 15:
        return False
    return True

def append_to_json(filepath, new_entries):
    data = []
    if os.path.exists(filepath):
        try:
            with open(filepath) as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: {filepath} was empty or corrupt, starting fresh")
            data = []
    
    existing_ids = {e["id"] for e in data}
    deduped = [e for e in new_entries if e["id"] not in existing_ids]
    data.extend(deduped)
    
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Added {len(deduped)} entries. Total: {len(data)}")



queries = [
    "Griselda",
    "Westside Gunn",
    "Benny the Butcher",
    "Conway the Machine",
    "Boldy James",
    "Rome Streetz",
    "Stove God Cooks",
]

subreddits = ["rap", "Griselda", "hiphopheads", "LetsTalkMusic"]

all_comments = []

for sub in subreddits:
    for query in queries:
        print(f"Fetching: '{query}' from r/{sub}")
        results = fetch_comments(query, sub, size=200)
        for c in results:
            if is_usable(c):
                all_comments.append({
                    "id": c.get("id"),
                    "text": c.get("body"),
                    "subreddit": c.get("subreddit"),
                    "score": c.get("score"),
                    "query_used": query,
                    "label": None,
                    "notes": None
                })
        time.sleep(1)



append_to_json("griselda.json", all_comments)
hot_takes = [d for d in all_comments if d['label']=='hot_take']
rest = [d for d in all_comments if d['label'] == 'hot_take']

random.seed(42)
balanced = rest + random.sample(hot_takes, 200)
random.shuffle(balanced)

print(f"Balanced dataset: {len(balanced)} entries")

print(f"Done. {len(all_comments)} usable comments collected.")