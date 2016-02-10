brocket
=======

A command line tool for building `Amazon Associates`_ links with as few actions as possible.

If you have a link in the clipboard, run this script, then the link on the clipboard becomes an `Amazon Associates`_ link.

Setup
-----

After you ``pip install brocket`` just run ``brocket``. It will prompt you for your tracking-id. Enter it.

If you want you can make sure it's correct by running ``brocket --show-tracking-id``.

How to Make Links
-----------------

Once it's setup, the easiest thing to do is

 1. Browse to an Amazon URL you want an affiliate link for.
 2. Copy the URL
 3. Run the ``brocket`` command. This will tag the URL with your tracking-id and put the new URL on the clipboard.
 4. Paste the URL where ever you want it to go.

Brocket Deer
------------

This little utility is named for the `Brocket Deer`_ which lives around the Amazon river. It also sounds like Rocket, but with a 'B' and I was looking for something fast.

.. _Amazon Associates: https://affiliate-program.amazon.com
.. _Brocket Deer: https://en.wikipedia.org/wiki/Brocket_deer
