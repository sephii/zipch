Swiss zipcodes database
=======================

This library provides an easy way to look up a swiss zipcode and get its canton
or municipality. Use it like this:

```python
>>> from zipch import ZipcodesDatabase
>>> zd = ZipcodesDatabase('/tmp/zipcodes')
>>> zd.get_location(1003)
Location(official_name='Lausanne', canton='VD', municipality='Lausanne', coordinates=Lv95Coordinates(E=Decimal('2537956.3654948957'), N=Decimal('1152398.7080000006')))
```

Installation
------------

Zipch has been tested on Python 3.7+. The easiest way to install
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
{8192: Location(official_name='Zweidlen', canton='ZH', municipality='Glattfelden'), 8193: Location(official_name='Eglisa', canton='ZH', municipality='Eglisa'), ...}
```

The library packs with some utility functions, these are all things that can
be derived from `get_locations()` but that are here for convenience:

```python
>>> zd.get_location(1003)
Location(official_name='Lausanne', canton='VD', municipality='Lausanne', coordinates=Lv95Coordinates(E=Decimal('2537956.3654948957'), N=Decimal('1152398.7080000006')))
>>> zd.get_zipcodes_for_municipality('Lausanne')
[1000, 1003, 1004, 1005, 1007, 1010, 1011, 1018, 1012]
>>> zd.get_zipcodes_for_canton('VD')
[1412, 1428, 1430, 1441, 1450, 1114, 1000, 1003, ...]
>>> zd.get_cantons()
['AG', 'AI', 'AR', 'BE', 'BL', 'BS', ...]
>>> zd.get_municipalities()
['Aadorf', 'Aara', 'Aarberg', 'Aarburg', 'Aarwangen', ...]
```

Geolocation
-----------

`Location` objects also have a `coordinates` attribute, which contains the
coordinates in [LV95
format](https://www.swisstopo.admin.ch/en/knowledge-facts/surveying-geodesy/reference-frames/local/lv95.html).
You can use the `lv95_to_wgs84` function to convert these coordinates to regular WGS84 longitude & latitude coordinates:

``` python
>>> from zipch import ZipcodesDatabase, lv95_to_wgs84
>>> lv95_to_wgs84(ZipcodesDatabase("/tmp/zipcodes").get_location(1003).coordinates)
```

Coordinates in regular WGS84 format are available in the `wgs84_coordinates`
attribute.
