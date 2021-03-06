__title__ = 'Amino.py'
__author__ = 'Slimakoi'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2020-2020 Slimakoi'
__version__ = '1.1.0'

from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .lib.util import device, exceptions, headers, helpers, objects
from .socket import Callbacks, SocketHandler
from requests import get
from json import loads

if __version__ != loads(get("https://pypi.python.org/pypi/Amino.py/json").text)["info"]["version"]:
    raise exceptions.LibraryUpdateAvailable