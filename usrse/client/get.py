__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from usrse.main import Client


def main(args, parser, extra, subparser):

    cli = Client(quiet=args.quiet, baseurl=args.baseurl)
    result = cli.get(args.content_type)

    # Default limit is 25, unless --all provided
    limit = None
    if not args.all:
        limit = args.limit

    if args.json and not args.outfile:
        result.print_json()

    elif args.outfile:
        result.save(args.outfile)

    # Simple table output
    elif args.live:
        result.table_live(limit=limit)

    else:
        result.table(limit=limit)
