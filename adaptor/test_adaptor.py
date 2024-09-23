#
# TODO -- This is a bad location in the project for tests.
#

from adaptor.courseworks_adaptor import Adapter
import json
# from models.course import Enrollment, CourseEnrollment


def t1():
    results = Adapter.get_courses()
    print("t1 result for get courses = \n", json.dumps(results, indent=2, default=str))


def t2():
    results = Adapter.get_courses()
    json.dump(results,
              open('t2.json', 'w'),
              indent=2,
              default=str)


def t3():

    with open("t2.json", "r") as f:
        j = json.load(f)
        c = j[1][0]
        print("t3 result for get courses = \n", json.dumps(c, indent=2, default=str))
        # m = CourseEnrollment(**c)
        # print("t3, m = ", m)


def t4():
    results = Adapter.get_students(class_id=204283)
    print("t4 results for get_students = \n", json.dumps(results, indent=2, default=str))
    with open("t4.json", "w") as o_file:
        json.dump(results, o_file, indent=2, default=str)


def t5():
    results = Adapter.get_sections(section_id="COMSW4153_001_2024_3")
    print("t5 results for get_sections = \n", json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    # t1()
    # t2()
    # t3()
    # t4()
    t5()

