from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, HttpUrl

class Link(BaseModel):
    rel: str = None
    href: str = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "rel": "sections",
                    "href": "/sections/COMSE6156"
                }
            ]
        }
    }