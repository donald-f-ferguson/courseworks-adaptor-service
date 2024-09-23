from resources.section_resource import SectionResource
import json


"""
def t1():
    cr = CourseEnrollmentResource(None)
    cs = cr.get_courses()
    print("t1: courses = \n", json.dumps(cs, indent=4, default=str))


def t2():
    cr = CourseEnrollmentResource(None)
    cs = cr.get_course(203180)
    print("t2: course = \n", json.dumps(cs, indent=4, default=str))
    

def t4():
    cr = CourseEnrollmentResource(None)
    cs = cr.get_course(203180)
    print("t2: course = \n", json.dumps(cs, indent=4, default=str))
"""


def t5():
    sr = SectionResource(None)
    ss = sr.get_section_by_id("COMSW4153_001_2024_3")
    print("t5: section = \n", json.dumps(ss, indent=4, default=str))


if __name__ == "__main__":
    # t1()
    t5()
