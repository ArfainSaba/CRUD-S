from typing import Union

from fastapi import FastAPI, Request

# import index
from index import results

app = FastAPI()

# results = index.results
for row in results:
    print(row)

@app.get("/v1/dataset")
# async def read_root(request: Request):
async def get_json():
    # payload = await results.json()
    # result = results() 
    # response= results.json()
    # return {"result":result}
    return results


@app.get("/v1/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}