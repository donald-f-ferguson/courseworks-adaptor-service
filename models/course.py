from __future__ import annotations

from typing import Any, List, Optional
from pydantic import BaseModel, HttpUrl
from models.links import Link


class Course(BaseModel):
    name: str = None
    course_no: str = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "TOPICS IN SOFTWARE ENGINEERING: Cloud and Microservice Applications",
                    "course_no": "COMSE6156"
                }
            ]
        }
    }


class CourseRSP(BaseModel):
    name: str = None
    course_no: str = None
    links: List[Link]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "TOPICS IN SOFTWARE ENGINEERING: Cloud and Microservice Applications",
                    "course_no": "/COMSE6156",
                    "links": [
                        {
                            "rel": "sections",
                            "href": "/sections/COMSE6156"
                        }
                    ]
                }
            ]
        }
    }



