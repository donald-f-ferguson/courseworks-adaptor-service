from __future__ import annotations

from typing import Any, List, Optional
from pydantic import BaseModel, HttpUrl
from models.links import Link


class Participant(BaseModel):
    id: str = None
    user_id: str = None
    course_id: str = None
    role: str = None
    uni: str = None
    sortable_name: str = None
    course_section_id: str = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1234,
                    "user_id": 5678,
                    "course_id": 9101112,
                    "role": "student",
                    "uni": "xyz",
                    "sortable_name": "Baggins, Bilbo",
                    "course_section_id": 195731
                }
            ]
        }
    }


class ParticipantRSP(BaseModel):
    id: str = None
    user_id: str = None
    course_id: str = None
    role: str = None
    uni: str = None
    sortable_name: str = None
    course_section_id: str = None
    links: List[Link] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1234,
                    "user_id": 5678,
                    "course_id": 9101112,
                    "role": "student",
                    "uni": "xyz",
                    "sortable_name": "Baggins, Bilbo",
                    "course_section_id": 195731,
                    "links": [
                        {
                            "rel": "section",
                            "href": "/courses/course_section_id"
                        }
                    ]
                }
            ]
        }
    }
