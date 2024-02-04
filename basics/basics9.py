## works with lists and dictionaries
import json

obj={
    "k":"v"
}

dumps_obj=json.dumps(obj)
print(dumps_obj, type(dumps_obj))

json_obj=json.loads(dumps_obj)
print(json_obj, type(json_obj))