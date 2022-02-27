.. _getting_started-installation:

============
Installation
============

US-RSE Python can be installed from pypi, or from source. 

Pypi
====

The module is available in pypi as `usrse <https://pypi.org/project/usrse/>`_,

.. code:: console

    $ pip install usrse


GitHub
======
        
You can also clone from the repository and install with pip (in development or regular mode):

.. code:: console

    $ git clone https://github.com/USRSE/usrse-python
    $ cd usrse-python
    $ pip install -e .
    $ pip install .

And that's probably the easiest way to install it. You can also grab a release tag if desired.


Setup
======

Installation will place an executable ``usrse`` in your bin directory associated with your Python install.


.. code:: console

    $ which usrse
    /home/vanessa/Desktop/Code/usrse-python/env/bin/usrse
    
    
And offer the following functions:

.. code:: console

    $ usrse --help

    usage: usrse [-h] [--debug] [--quiet] [--baseurl BASEURL] [--version] {version,shell,get} ...

    USRSE Client

    optional arguments:
      -h, --help           show this help message and exit
      --debug              use verbose logging to debug.
      --quiet              suppress additional output.
      --baseurl BASEURL    change the default baseurl to something else
      --version            show software version.

    actions:
      actions

      {version,shell,get}  actions


Check out the :ref:`getting-started` pages for more detail to use the client.

