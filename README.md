datamcfly-python
================

Python library for Data McFly API

This is still a work in progress but you can install with the following com.

PyDataMcFly is a Python_ client library that contains tools for accessing to
DataMcFly databases via the `DataMcFly REST API`_ using a similar syntax to PyMongo_.

Useful in cases where network barriers (firewalls, etc.)  prevent use of the
standard MongoDb driver.

```python
>>> from pydatamcfly import DataMcFlyClient
>>> con = DataMcFlyClient("DataMcFlyAPIKey")
>>> db = con.database
>>> col = db.collection.find()
>>> list(col)
[{u'_id': ObjectId('50243d38e4b00c3b3e75fc94'), u'foo': u'bar', u'tld': u'com'},
{u'_id': ObjectId('50004d646cf431171ed53846'), u'foo': u'bar', u'tld': u'org'}]
```

Installation
============

You can to use pip_ to install PyDataMcFly::

	$ pip install pydatamcfly

Or using last source::

	$ pip install git+git://github.com/DataMcFly/pydatamcfly.git
