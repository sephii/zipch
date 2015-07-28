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
