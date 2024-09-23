from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, HttpUrl


class Calendar(BaseModel):
    ics: HttpUrl


class Enrollment(BaseModel):
    type: str = None
    role: str = None
    role_id: int = None
    user_id: int = None
    enrollment_state: str = None
    limit_privileges_to_course_section: bool = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "type": "student",
                    "role": "StudentEnrollment",
                    "role_id": 123,
                    "limit_privileges_to_course_section": 3456,
                }
            ]
        }
    }


class CourseEnrollment(BaseModel):
    id: int = None
    name: str = None
    account_id: int = None
    uuid: str = None
    start_at: Any = None
    grading_standard_id: Any = None
    is_public: bool = None
    created_at: str = None
    course_code: str = None
    default_view: str = None
    root_account_id: int = None
    enrollment_term_id: int = None
    license: str = None
    grade_passback_setting: Any = None
    end_at: Any = None
    public_syllabus: bool = None
    public_syllabus_to_auth: bool = None
    storage_quota_mb: int = None
    is_public_to_auth_users: bool = None
    homeroom_course: bool = None
    course_color: Any = None
    friendly_name: Any = None
    apply_assignment_group_weights: bool = None
    calendar: Calendar
    time_zone: str = None
    blueprint: bool = None
    template: bool = None
    sis_course_id: str = None
    integration_id: Any = None
    enrollments: List[Enrollment] = None
    hide_final_grades: bool = None
    workflow_state: str = None
    restrict_enrollments_to_course_dates: bool = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 5555555,
                    "name": "COMSE6156_001_2018_3 - TOPICS IN SOFTWARE ENGINEERING: Cloud and Microservice Applications",
                    "account_id": 333,
                    "uuid": "DO57H1uh7HiQ3fyx9F9Ag9Bxjnsxe42QWO2BmzFO",
                    "start_at": None,
                    "grading_standard_id": None,
                    "is_public": False,
                    "created_at": "2018-07-13T12:31:19Z",
                    "course_code": "COMSE6156_001_2018_3 - TOPICS IN SOFTWARE ENGINEERING",
                    "default_view": "wiki",
                    "root_account_id": 1,
                    "enrollment_term_id": 329,
                    "license": "private",
                    "grade_passback_setting": None,
                    "end_at": None,
                    "public_syllabus": False,
                    "public_syllabus_to_auth": False,
                    "storage_quota_mb": 1572,
                    "is_public_to_auth_users": False,
                    "homeroom_course": False,
                    "course_color": None,
                    "friendly_name": None,
                    "apply_assignment_group_weights": False,
                    "calendar": {
                        "ics": "https://courseworks2.columbia.edu/feeds/calendars/course_DO57H1uh7HiQ3fyx9F9Ag9Bxjnsxe42QWO2BmzFO.ics"
                    },
                    "time_zone": "America/New_York",
                    "blueprint": False,
                    "template": False,
                    "sis_course_id": "COMSE6156_001_2018_3",
                    "integration_id": None,
                    "enrollments": [
                        {
                            "type": "teacher",
                            "role": "TeacherEnrollment",
                            "role_id": 436,
                            "user_id": 44444,
                            "enrollment_state": "active",
                            "limit_privileges_to_course_section": False
                        }
                    ],
                    "hide_final_grades": False,
                    "workflow_state": "available",
                    "restrict_enrollments_to_course_dates": False
                },
                {
                    "id": 7777777,
                    "name": "COMSE6156_001_2019_3 - TOPICS IN SOFTWARE ENGINEERING",
                    "account_id": 333,
                    "uuid": "R1fTDNdQc7Koh3BDCiwX7raLt6gcujOSMr56pEET",
                    "start_at": "2019-04-25T03:30:00Z",
                    "grading_standard_id": None,
                    "is_public": False,
                    "created_at": "2019-04-25T00:57:03Z",
                    "course_code": "COMSE6156_001_2019_3 - TOPICS IN SOFTWARE ENGINEERING",
                    "default_view": "syllabus",
                    "root_account_id": 1,
                    "enrollment_term_id": 332,
                    "license": "private",
                    "grade_passback_setting": None,
                    "end_at": None,
                    "public_syllabus": False,
                    "public_syllabus_to_auth": False,
                    "storage_quota_mb": 1572,
                    "is_public_to_auth_users": False,
                    "homeroom_course": False,
                    "course_color": None,
                    "friendly_name": None,
                    "apply_assignment_group_weights": False,
                    "calendar": {
                        "ics": "https://courseworks2.columbia.edu/feeds/calendars/course_R1fTDNdQc7Koh3BDCiwX7raLt6gcujOSMr56pEET.ics"
                    },
                    "time_zone": "America/New_York",
                    "blueprint": False,
                    "template": False,
                    "sis_course_id": "COMSE6156_001_2019_3",
                    "integration_id": None,
                    "enrollments": [
                        {
                            "type": "teacher",
                            "role": "TeacherEnrollment",
                            "role_id": 6666,
                            "user_id": 33333333,
                            "enrollment_state": "active",
                            "limit_privileges_to_course_section": False
                        }
                    ],
                    "hide_final_grades": False,
                    "workflow_state": "available",
                    "restrict_enrollments_to_course_dates": False,
                    "overridden_course_visibility": ""
                }
            ]

        }
    }
