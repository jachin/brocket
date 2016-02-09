import brocket

import argparse

parser = argparse.ArgumentParser(
    description='Make an Amazon link and Amazon Associates link.'
)

parser.add_argument(
    '--tracking-id',
    dest='tracking_id',
    default=brocket.tracking_id,
    help='The tracking-id to use (default: saved tracking-id in settings.)'
)

parser.add_argument(
    '--show-tracking-id',
    dest='show_tracking_id',
    action='store_true',
    default=False,
    help='Print out the saved Amazon Associates tracking-id.'
)

parser.add_argument(
    '--set-tracking-id',
    dest='tracking_id',
    default=None,
    help='Set the tracking-id in the settings.'
)


def main():
    args = parser.parse_args()

    if args.show_tracking_id:
        print(brocket.tracking_id)


if __name__ == "__main__":
    main()
