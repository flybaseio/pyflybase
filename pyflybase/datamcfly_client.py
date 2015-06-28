# -*- coding: utf-8 *-*
from pyflybase import database
from flybaseclient import FlybaseClient


class FlybaseClient(object):
    """Instance class with the API key located at
    https://app.flybase.io/

    Example usage:

    .. code-block:: python

       >>> from pyflybase import FlybaseClient
       >>> FlybaseClient("FlybaseAPIKey")
       FlybaseClient('FlybaseAPIKey', 'v1')

    .. note::
       The ``version`` parameter is optional, because it is planed for using in
       future versions of REST API.

    When your connection needs to set a proxy, you can to set an `str` with the
    Proxy url to ``proxy_url`` parameter. If you don't set a ``proxy_url``,
    then :class:`flybaseclient.client.FlybaseClient` gets system proxy
    settings.

    .. code-block:: python

       >>> from pyflybase import FlybaseClient
       >>> FlybaseClient("FlybaseAPIKey", proxy_url="https://127.0.0.1:8000")
       FlybaseClient('FlybaseAPIKey', 'v1')
    """

    def __init__(self, api_key, version="v1", proxy_url=None):
        self.api_key = api_key
        self.version = version
        self.__request = FlybaseClient(api_key, version, proxy_url)

    @property
    def request(self):
        """An instance of :class:`flybaseclient.client.FlybaseClient` used
        for internal calls to Flybase REST API via :mod:`flybaseclient`.
        """
        return self.__request

    def __eq__(self, other):
        if isinstance(other, FlybaseClient):
            us = (self.api_key, self.version)
            them = (other.api_key, other.version)
            return us == them
        return NotImplemented

    def __repr__(self):
        return "FlybaseClient(%r, %r)" % (self.api_key, self.version)

    def __getattr__(self, name):
        """Get a database using a attribute-style access.

        Example usage:

        .. code-block:: python

           >>> from pyflybase import FlybaseClient
           >>> con = FlybaseClient("FlybaseAPIKey")
           >>> con.database
           Database(FlybaseClient('FlybaseAPIKey', 'v1'), 'database')
        """
        return database.Database(self, name)

    def __getitem__(self, name):
        """Get a database using a dictionary-style access.

        Example usage:

        .. code-block:: python

           >>> from pyflybase import FlybaseClient
           >>> con = FlybaseClient("FlybaseAPIKey")
           >>> db = con["database"]
           Database(FlybaseClient('FlybaseAPIKey', 'v1'), 'database')
        """
        return self.__getattr__(name)

    def database_names(self):
        """Returns a list with your database names.

        Example usage:

        .. code-block:: python

           >>> from pyflybase import FlybaseClient
           >>> con = FlybaseClient("FlybaseAPIKey")
           >>> con.database_names()
           [u'database', u'otherdatabase']
        """
        return self.request.list_databases()
