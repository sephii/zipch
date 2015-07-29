Swiss zipcodes database
=======================

This library provides an easy way to look up a swiss zipcode and get its canton
or municipality. Use it like this:

```python
>>> from zipch import ZipcodesDatabase
>>> zd = ZipcodesDatabase('/tmp/zipcodes')
>>> zd.get_location(1003)
Location(official_name=u'Lausanne', canton=u'VD', municipality=u'Lausanne')
```

Installation
------------

Zipch has been tested on Python 2.7 and Python 3.4. The easiest way to install
it is by using PyPI:

```sh
pip install zipch
```

Usage
-----

Start by creating a `ZipcodesDatabase` object. In the example below,
`/tmp/zipcodes` is a file that will be used as the zipcodes database. If the
file doesn't exist yet, it will be created by downloading the latest version of
the zipcodes database.

```python
>>> from zipch import ZipcodesDatabase
>>> zd = ZipcodesDatabase('/tmp/zipcodes')
```

You can then get all the zipcodes registered in the database as a {zipcode:
location} dict:

```python
>>> zd.get_locations()
{8192: Location(official_name=u'Zweidlen', canton=u'ZH', municipality=u'Glattfelden'), 8193: Location(official_name=u'Eglisau', canton=u'ZH', municipality=u'Eglisau'), ...}
```

The library packs with some utility functions, these are all things that can
be derived from `get_locations()` but that are here for convenience:

```python
>>> zd.get_location(1003)
Location(official_name=u'Lausanne', canton=u'VD', municipality=u'Lausanne')
>>> zd.get_zipcodes_for_municipality('Lausanne')
[1000, 1003, 1004, 1005, 1007, 1010, 1011, 1018, 1012]
>>> zd.get_zipcodes_for_canton('VD')
[1412, 1428, 1430, 1441, 1450, 1114, 1000, 1003, ...]
>>> zd.get_cantons()
[u'AG', u'AI', u'AR', u'BE', u'BL', u'BS', ...]
>>> zd.get_municipalities()
[u'Aadorf', u'Aarau', u'Aarberg', u'Aarburg', u'Aarwangen', ...]
```
