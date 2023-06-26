from common import common_db
from pymongo.operations import DeleteMany, InsertOne
import json
import os

def restore() -> bool:


    filenames = []

    files = os.listdir("./backup/")
    for filename in files:
        if not filename.endswith(".json"):
            continue
        col_name = filename[0:-5]
        filenames.append(col_name)
        requests = []
        requests.append(DeleteMany({}))
        with open("/backup/" + filename, "r", encoding="utf-8") as file:
            items = json.load(file)
            for item in items:
                requests.append(InsertOne(item))
        result = common_db[col_name].bulk_write(requests)

    return {"restored" : filenames}