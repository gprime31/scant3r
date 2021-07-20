from .xss_param import XssParam
from urllib.parse import urlparse as ur
from core.libs import show_error

def main(opts,r):
    # If Query in the URL 
    if ur(opts['url']).query:
        XssParam(opts,r).start()
    else: 
        show_error('xss_param', "No query in the URL")
    