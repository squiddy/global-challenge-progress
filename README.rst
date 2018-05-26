globale-challenge-progress 
==========================

During the Virgin Pulse Global Challenge, this script generates an image that
depicts the current progress across all teams in the same organization.

Usage
-----

To start, copy ``.env_example`` to ``.env`` and add your login credentials.

.. code-block:: console

    # This will load your .env automatically, if you do not use pipenv,
    # don't forget to source the file manually.
    $ pipenv shell
    $ python create_image.py > progress.svg
    $ firefox progress.sv

TODO
----

Right now the script merely outputs the progress of all teams in a tabular
format in SVG. I want the output to show the current position of the teams on
a map.