from typing import List
import json

from adaptor.courseworks_adaptor import Adapter
from models.section import SectionsRSP
from adaptor.courseworks_adaptor import Adapter


# TODO Factor in the base framework.
class SectionResource:

    def __init__(self, context):
        self.context = context
        self.adaptor = Adapter

    def get_section_by_id(self, section_id: str) -> SectionsRSP:
        result = self.adaptor.get_sections(section_id=section_id)
        if result:
            final_result = {}
            split_id = result["sis_course_id"].split("_")

            final_result["course_id"] = split_id[0]
            final_result["section_id"] = result["sis_course_id"]
            final_result["section_no"] = split_id[1]
            final_result["semester"] = split_id[3]
            final_result["year"] = split_id[2]
            final_result["links"] = None

            final_result = SectionsRSP(**final_result)
        else:
            final_result = None

        return final_result
