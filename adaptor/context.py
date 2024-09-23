#
# TODO -- This is not a good design. There are better patterns for
# passing configuration information and "secrets" to applications and services.
#
# THIS HAS TO BE IN GITIGNORE
#
# TODO -- There is SO MUCH BAD in this implementation.
#
import json
import os


class Context:


    @classmethod
    def get_courseworks_token(cls):

        result = Context.default_courseworks_access_token

        return result
