import requests
import time

def synchronous_get(urls):
    results = []
    start_time = time.time()
    
    for url in urls:
        response = requests.get(url)
        results.append(response.text[:100])  # Taking the first 100 characters as an example
    
    end_time = time.time()
    print(f"Synchronous total elapsed time: {end_time - start_time:.2f}s")
    return results

# Example usage
urls = [
    "https://e6156-402914.ue.r.appspot.com/static/index.html",
    "http://ec2-18-234-220-207.compute-1.amazonaws.com:8011/",
    "http://34.30.27.130:8011/",
]
results = synchronous_get(urls)
for result in results:
    print(result)
