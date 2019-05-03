#!/usr/bin/python3

from twilio.rest import Client
import configargparse
import re
import sys
import textwrap

def parse_args():
    parser = configargparse.ArgumentParser(
        default_config_files=["/etc/smsscheme", "~/.smsscheme"],
        description="Send SMS messages using the sms URN scheme.",
        epilog=textwrap.dedent("""
            Send an SMS message. The "origin", "sid", and "token" parameters
            are required, but may be defined in a configuration file. The
            destination phone number and text may be specified via the
            "to" and "text" options, or via an SMS URN of the form
            "sms:+15555555555?<message>".
            """[1:-1]
        )
    )
    
    parser.add_argument(
        "-o", "--origin",
        help="the sending phone number (e.g. +15555555555)",
    )

    parser.add_argument(
        "-s", "--sid",
        help="the Twilio Account SID",
        metavar="ACCOUNT_SID",
    )

    parser.add_argument(
        "-t", "--token",
        help="the Twilio Auth Token",
        metavar="ACCOUNT_TOKEN",
    )

    parser.add_argument(
        "--to",
        help="the destination phone number",
    )

    parser.add_argument(
        "--text",
        help="the text to send",
    )

    parser.add_argument(
        "sms_urn",
        nargs="?",
        help="the sms URN",
        metavar="SMS_URN",
        default="",
    )

    args = parser.parse_args()

    match = re.search("^sms:([^\?]+?)\?(.+)$", args.sms_urn)
    if match:
        args.to = match.group(1)
        args.text = match.group(2)


    if not args.to:
        print("no To phone number found")
        sys.exit(1)

    if not args.text:
        print("no text found")
        sys.exit(1)

    return args

def main():
    args = parse_args()

    client = Client(
        args.sid,
        args.token,
    )

    message = client.messages.create(
        to=args.to,
        from_=args.origin,
        body=args.text,
    )

    print(message.sid)


if __name__ == "__main__":
    main()
