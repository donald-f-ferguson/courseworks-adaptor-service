#
# TODO -- This is a bad location in the project for tests.
#

from adaptor.courseworks_adaptor import Adapter
import json


def t1():
    results = Adapter.get_courses()
    print("t1 result for get courses = \n", json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    t1()

