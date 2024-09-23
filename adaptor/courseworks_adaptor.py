import requests
from context import Context


class Adapter:
    #
    # TODO -- Add support for logging/trace/observability.
    # TODO -- Add support for automatically generating API documentation.
    # TODO -- This should be dependency injection
    #
    # TODO -- Remove all of the lazy implementation stuff.
    #
    context = Context

    @classmethod
    def get_access_token(cls):
        result = Adapter.context.get_courseworks_token()
        return result

    @classmethod
    def get_next_url(cls, links=None):
        """
        Passed a list of links of the form '{"rel": "Some relationship", "href": "Some link."}'
        Iterates through the array until it find the rel = next to find the link to the next page.

        :param links: List of dictionaries of rel/href.
        :return: The next page URL.
        """

        next_url = None

        if links is not None:
            all_links = links.split(',')
            for l in all_links:
                this_l = l.split(';')
                if this_l[1].find("next") != -1:
                    next_url = this_l[0]
                    next_url = next_url[1:-1]
                    break
        return next_url

    @classmethod
    def get_with_pagination(cls, url):

        tk = Adapter.get_access_token()

        headers = {"Authorization": tk}
        all_data = []

        # print("Headers = ", headers)

        status_code = None

        next_url = url
        while next_url is not None:
            result = requests.get(url=next_url, headers=headers)
            if result.status_code == 200:
                dd = result.json()
                status_code = result.status_code
                if type(dd) == list:
                    all_data.extend(dd)
                else:
                    all_data.append(dd)
                links = result.headers.get("Link")
                next_url = cls.get_next_url(links)
            else:
                status_code = result.status_code
                dd = None
                done = True
                next_url = None

        return status_code, all_data

    @classmethod
    def get_sections(cls, course_id=None, role=None, section_id=None):
        url = Adapter.context.courseworks_section_url

        if course_id is not None:
            url += "/" + str(course_id)

        if role is not None:
            url += "?enrollment_type=" + role

        result = cls.get_with_pagination(url)

        final_result = None

        if section_id is not None:
            for s in result[1]:
                if s.get("sis_course_id", None) == section_id:
                    final_result = s
                    break
        else:
            final_result = result

        ret = final_result
        return ret


    @classmethod
    def get_students(cls, class_id, student_id=None):
        url = Adapter.context.courseworks_base_url + "/courses/" + str(class_id) + "/users?include[]=enrollments"
        if student_id is not None:
            url += "/" + str(student_id)

        tk = Adapter.get_access_token()

        headers = {"Authorization": tk}
        # result = requests.get(url=url, headers=headers)
        result = cls.get_with_pagination(url)

        ret = result
        return ret


