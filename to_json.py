import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        res = func(*args, **kwargs)
        res = json.dumps(res)
        # print(res)
        return res
    return wrapped

# @to_json
# def get_data(num):
#     return {
#         'data': num
#     }
#
#
# get_data(42)  # вернёт '{"data": 42}'
