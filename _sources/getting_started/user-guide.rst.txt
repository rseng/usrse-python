.. _getting_started-user-guide:

==========
User Guide
==========

US-RSE Python is a library in Python to make it easy to retrieve data from the US-RSE
site, which is available via our `static apis <https://us-rse.org/wg/website/#feeds>`_.
With US-RSE Python we can:

 - Quickly see updated content (newsletters, posts, dei or other events) in the terminal
 - Pipe or save a json of the same data to file

And then enable automation that is external to our main site that requires it!
We are excited about what tools we can build around this, and please
`give us a ping <https://github.com/US-RSE/usrse-python>`_. if you have an idea!


.. raw:: html

    <script id="asciicast-472034" src="https://asciinema.org/a/472034.js" data-speed="2" async></script>


Quick Start
===========

Once you have usrse installed, you likely quickly want to get data

.. code-block:: console

    $ usrse get posts
    $ usrse get newsletters
    $ usrse get dei
    $ usrse get events
    $ usrse get member-counts
    $ usrse get jobs

Or snazz things up a bit!

.. code-block:: console

    $ usrse get posts --live
    $ usrse get newsletters --live
    $ usrse get dei --live
    $ usrse get events --live
    $ usrse get member-counts --live
    $ usrse get jobs --live

Or output as json or save to json for later.

.. code-block:: console

    $ usrse get dei --json
    $ usrse get events --outfile events.json


You can then easily install, load, and use modules:


.. _getting_started-commands:

Commands
========

The following commands are available! 

.. _getting_started-commands-list:

List
----

The first thing you might want to do is see what endpoints are available.
You can do that with ``list``:

.. code-block:: console

    $ usrse list
    dei
    events
    jobs
    member-counts
    newsletters
    posts


This is also nice to pipe into a bash loop for doing something:

.. code-block:: console

    for endpoint in $(usrse list); do
       # do something here
       echo $endpoint;
    done

Once you know endpoints, then you can ``get`` them, discussed next.

.. _getting_started-commands-get:

Get
---

The most basic functionality is to get content. Here are all the types we can ask for:

.. code-block:: console

    usage: usrse get [-h] [--json] [--all] [--live] [--limit LIMIT] [--outfile OUTFILE] content_type

    get USRSE content

    positional arguments:
      content_type          content type
                            events
                            posts
                            dei
                            newsletters
                            member-counts
                            jobs

    optional arguments:
      -h, --help            show this help message and exit
      --json                output json
      --all                 output json
      --live, -k            get a live and interactive table!
      --limit LIMIT         limit of posts to show (defaults to show, use --all for all posts)
      --outfile OUTFILE, -o OUTFILE
                            write content to output file


And an example for how to ask:

.. code-block:: console

    $ usrse get posts


By default, we set of a limit of 25 for the 25 most recent results. If you want to change the limit:

.. code-block:: console

    $ usrse get posts --limit 10


Or ask for them all!

.. code-block:: console

    $ usrse get posts --all
    

Output json instead of a table (json does not set limits):

.. code-block:: console

    $ usrse get posts --json


or save json to file:

.. code-block:: console

    $ usrse get posts --outfile posts.json

 
Here are all the content types you can ask for:

.. code-block:: console

    $ usrse get posts
    $ usrse get newsletters
    $ usrse get dei
    $ usrse get events
    $ usrse get member-counts
    $ usrse get jobs

Want to have some fun? Try the live tables!


.. code-block:: console

    $ usrse get posts --live
    $ usrse get newsletters --live
    $ usrse get dei --live
    $ usrse get events --live
    $ usrse get member-counts --live
    $ usrse get jobs --live


Changing the baseurl
^^^^^^^^^^^^^^^^^^^^

You can also use a baseurl for local development, e.g., let's say we do:

.. code-block:: console

    $ git clone https://github.com/USRSE/usrse.github.io
    $ cd usrse.github.io
    $ bundle exec jekyll serve

 
And then in another terminal:

.. code-block:: console
    
    $ usrse --baseurl http://127.0.0.1:4000 get posts


.. _getting_started-commands-shell:
 
 
 
Shell
-----

If you are a developer and want to create a quick client to test or interact with,
we are looking out for you!  For example:

.. code-block:: console

    $ usrse shell
    Python 3.8.8 (default, Apr 13 2021, 19:58:26) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.29.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: client
    Out[1]: [usrse-client]

    In [2]: result = client.get("newsletters")
    GET https://us-rse.org/api/newsletters.json
    In [3]: result.to_dict()


Container
=========

If you need to build a quick container, we provide a Dockerfile in the repository:


.. code-block:: console

    docker build -t usrse-python .


This library is under development and we will have more endpoints and functionality
coming soon!
