import threading
from concurrent.futures import ThreadPoolExecutor

def transformation(input):

    name = input['name']
    rows = input['rows']

    print(f"We have {name} table")
    print(f"It has {rows} rows")
    return f"I am Done loading {name}"


tables = [
    {"name": "customers", "rows": 1000},
    {"name": "orders", "rows": "5000"},
    {"name": "products", "rows": "200"},
]

with ThreadPoolExecutor(max_workers=3) as executor:

    my_future = executor.map(transformation,tables)

print(f"The returned values are {list(my_future)}")