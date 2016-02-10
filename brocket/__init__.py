# -*- coding: utf-8 -*-

import sys

from urlobject import URLObject
import pyperclip


def process_url(url, tracking_id):
    amazon_url = URLObject(url)
    aa_tag = tracking_id

    # Sanity checking, make sure we have an amazon URL.
    valid_hosts = ['amazon.com', 'www.amazon.com']

    if amazon_url.hostname not in valid_hosts:
        print("""The URL "{}" is not an Amazon URL.""".format(str(amazon_url)))
        sys.exit(1)

    amazon_url = amazon_url.with_scheme('https')

    msg = "Adding the tag {} to the URL {} and putting it on the clipboard."

    print(msg.format(aa_tag, amazon_url))

    amazon_url = amazon_url.set_query_param('tag', aa_tag)

    print(amazon_url)

    pyperclip.copy(amazon_url)

    return amazon_url


def process_clipboard_url(tracking_id):
    process_url(pyperclip.paste(), tracking_id)
