import requests 

def get_items():
    resp = requests.get("http://0.0.0.0:8000/items/")
    print(resp.json())

def post_items(body):
    response = requests.post("http://0.0.0.0:8000/items/", data=body)
    print(response.json())

def retrieve_item(id):
    res = requests.get(f"http://0.0.0.0:8000/item/{id}")
    print(res.json())

retrieve_item(4)

# post_items({
#     "title": "coffee",
#     "stock_quantiy": 200,
#     "rating": "5 Stars",
#     "price": 3.99,
#     "in_stock": True
# })
