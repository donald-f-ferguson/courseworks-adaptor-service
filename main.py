# Simple starter project for FastAPI REST Microservice.
#
# Based on https://fastapi.tiangolo.com/tutorial/first-steps/
#

# Explicitly included uvicorn to enable starting within main program.
# Starting within main program is a simple way to enable running
# the code within the PyCharm debugger
#
import uvicorn

# Import JSON for mapping between Python dict classes and various uses of JSON.
# JSON is a lightweight approach to defining and exchanging data.
# https://www.json.org/json-en.html
import json


# The FastAPI server class.
#
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

# See https://fastapi.tiangolo.com/tutorial/middleware/ for an explanation of middleware.
#
# See https://en.wikipedia.org/wiki/Cross-origin_resource_sharing for an explanation of CORS
#
from fastapi.middleware.cors import CORSMiddleware

# Added support for "static" web pages and other content.
# Static pages, e.g. HTML are in the path /static. For example,
# http://localhost:8001/static/index.html
#
from fastapi.staticfiles import StaticFiles

# FastAPI understands pydantic for defining "models" for REST API
# bodies. https://swagger.io/specification/
#
# An overview: https://medium.com/@nicola88/your-first-openapi-document-part-ii-data-model-52ee1d6503e0
#
# This is a form of the data transfer object pattern.
#
from typing import List, Union
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from models.course import Course, CourseRSP
from models.section import SectionsRSP, Section
from models.participant import Participant, ParticipantRSP

from resources.section_resource import SectionResource

# Create the application/api server class.
#
app = FastAPI()

# This is sloppy. The CORS configuration should come from the environment.
# 12 - Factor Application design pattern suggest configuration should come from environment,
# not be hard coded.
#
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# See the explanation for static files and mount on the FastAPI documentation.
# https://fastapi.tiangolo.com/tutorial/static-files/
#
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=JSONResponse)
async def root():
    """
    Basic test for root path. I added the "hint" to the returned message to guide students to
    find the OpenAPI document pages.

    :return: Simple JSON message.
    """
    return {
        "message": "Hello World",
        "hint": "Go to /docs to see the OpenAPI documentation."
    }


@app.get("/hello")
async def say_hello(name: str) -> str:
    """
    Implements the pass /hello
    :param name: A string as a query parameter. That is, /hello?name=some name
    :return: A JSON object in text format with the message saying hello.
    """
    return json.dumps({"message": f"Hello {name}"}, indent=2)


@app.get("/api/courses", response_model=List[CourseRSP])
async def get_courses() -> List[CourseRSP]:
    """
    """
    raise NotImplemented()


@app.post("/api/courses", )
async def create_course(course: Course) -> None:
    """
    """
    raise NotImplemented()


@app.get("/api/sections", response_model=List[SectionsRSP])
async def get_sections(
        course_id: str = None,
        semester: str = None,
        year: str = None
) -> List[SectionsRSP]:
    """
    """
    raise NotImplemented()


@app.get("/api/sections/{section_id}", response_model=SectionsRSP)
async def get_section_by_id(
    section_id
) -> SectionsRSP:
    """
    """
    try:
        sec = SectionResource(None)
        result = sec.get_section_by_id(section_id=section_id)
    except Exception as ex:
        print("Exception = ", ex)
        result = None

    return result



@app.get("/api/sections/{section_id}/participants", response_model=List[SectionsRSP])
async def get_section_participants(
        section_id: str = None,
        role: str = None
) -> SectionsRSP:

    raise NotImplementedError




# Added the code below to enable running in PyCharm debugger.
# Modified the port from 8000 to 8001 because I often have multiple
# microservices running and need to spread over ports.
#
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)