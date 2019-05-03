
## smsscheme

This application sends SMS messages based on an sms URN.

Eventually, it will work as an sms scheme handler, supporting e.g.
sms hrefs from a web browser.

Twilio credentials are required, either on the command line or in a
configuration file.

In typical usage, the origin phone number, Twilio account sid and token
are defined in ~/.smsscheme, and messages are sent with commands like:

    smsscheme "sms:+15555555555?Send Money!"

## Usage

    $ smsscheme -h
    usage: smsscheme.py [-h] [-o ORIGIN] [-s ACCOUNT_SID] [-t ACCOUNT_TOKEN]
                        [--to TO] [--text TEXT]
                        [SMS_URN]
    
    Send SMS messages using the sms URN scheme. Args that start with '--' (eg. -o)
    can also be set in a config file (/etc/smsscheme or ~/.smsscheme). Config file
    syntax allows: key=value, flag=true, stuff=[a,b,c] (for details, see syntax at
    https://goo.gl/R74nmi). If an arg is specified in more than one place, then
    commandline values override config file values which override defaults.
    
    positional arguments:
      SMS_URN               the sms URN
    
    optional arguments:
      -h, --help            show this help message and exit
      -o ORIGIN, --origin ORIGIN
                            the sending phone number (e.g. +15555555555)
      -s ACCOUNT_SID, --sid ACCOUNT_SID
                            the Twilio Account SID
      -t ACCOUNT_TOKEN, --token ACCOUNT_TOKEN
                            the Twilio Auth Token
      --to TO               the destination phone number
      --text TEXT           the text to send
    
    Send an SMS message. The "origin", "sid", and "token" parameters are required,
    but may be defined in a configuration file. The destination phone number and
    text may be specified via the "to" and "text" options, or via an SMS URN of
    the form "sms:+15555555555?<message>".
    
