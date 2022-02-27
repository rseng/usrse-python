__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import usrse.main.endpoints as endpoints


def main(args, parser, extra, subparser):
    for endpoint in endpoints.register_names:
        print(endpoint)
