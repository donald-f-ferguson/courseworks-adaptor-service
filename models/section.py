from __future__ import annotations

from typing import Any, List, Optional
from pydantic import BaseModel, HttpUrl
from models.links import Link


class Section(BaseModel):
    course_id: Optional[str] = None
    section_id: Optional[str] = None
    section_no: Optional[str] = None
    semester: Optional[str] = None
    year: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "course_id": "COMSE6156",
                    "section_id": "COMSE6156_001_2018_3",
                    "section_no": "001",
                    "semester": "3",
                    "year": "2018"
                }
            ]
        }
    }


class SectionsRSP(BaseModel):
    course_id: Optional[str] = None
    section_id: Optional[str] = None
    section_no: Optional[str] = None
    semester: Optional[str] = None
    year: Optional[str] = None

    links: Optional[List[Link]]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "section_id": "COMSE6156_001_2018_3",
                    "course_id": "COMSE6156",
                    "section_no": "001",
                    "semester": "3",
                    "year": "2018",
                    "links": [
                        {
                            "rel": "course",
                            "href": "/courses/COMSE6156"
                        },
                        {
                            "rel": "participants",
                            "href": "/sections/COMSE6156_001_2018_3/participants"
                        }
                    ]
                }
            ]
        }
    }



