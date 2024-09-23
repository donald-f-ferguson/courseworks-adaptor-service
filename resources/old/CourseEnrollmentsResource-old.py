from typing import List
import json

from adaptor.courseworks_adaptor import Adapter
from models.course import Enrollment, CourseEnrollment


# TODO Factor in the base framework.
class CourseEnrollmentResource:

    def __init__(self, context):
        self.context = context
        self.adaptor_file = "/adaptor/t2.json"
        self.cached_courses = None
        self.load_courses()

    def load_courses(self):
        with open(self.adaptor_file, "r") as f:
            self.cached_courses = json.load(f)
            if self.cached_courses:
                self.cached_courses = self.cached_courses[1]

    def get_courses(self) -> List[CourseEnrollment]:
        return self.cached_courses

    def get_course(self, course_id: int) ->List[CourseEnrollment]:
        result = None

        cs = self.get_courses()
        for c in cs:
            if c["id"] == course_id:
                result = c
                break

        return result

    def get_course_enrollments(self, course_id: int) -> List[Enrollment]:
        result = None

        cs = self.get_courses()
        for c in cs:
            if c["id"] == course_id:
                result = c
                break

        return result.get("enrollments", [])







