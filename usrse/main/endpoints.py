__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import usrse.defaults as defaults
import sys

# Registered endpoints (populated on init)
register = {}
register_names = []


class Endpoint:
    dont_truncate = ["url"]
    emoji = "calendar"

    def __init__(self, baseurl):
        self.baseurl = baseurl or defaults.baseurl
        for attr in ["name", "path"]:
            if not hasattr(self, attr):
                sys.exit(
                    "Misconfigured endpoint %s missing %s attribute" % (self, attr)
                )

    @property
    def url(self):
        return self.baseurl + self.path

    @property
    def title(self):
        return "US-RSE " + self.name.capitalize()

    def _get_attribute_or_list(self, name):
        listing = []
        if hasattr(self, name):
            listing = getattr(self, name, []) or []
        return listing

    @property
    def truncate_list(self):
        return self._get_attribute_or_list("dont_truncate")

    @property
    def skip_list(self):
        return self._get_attribute_or_list("skips")


class Dei(Endpoint):
    name = "dei"
    path = "/api/dei.json"
    skips = ["repeated", "published", "description"]
    emoji = "sparkles"


class Newsletters(Endpoint):
    name = "newsletters"
    path = "/api/newsletters.json"
    emoji = "newspaper"
    skips = ["published"]


class Posts(Endpoint):
    name = "posts"
    path = "/api/posts.json"
    skips = ["published"]
    emoji = "pencil"


class Events(Endpoint):
    name = "events"
    path = "/api/events.json"
    skips = ["repeated", "published", "description"]


for endpoint in [Dei, Newsletters, Posts, Events]:
    register_names.append(endpoint.name)
    register[endpoint.name] = endpoint
