PythonEw
=========

This is an updating of the [PythonEw](https://github.com/osop/osop-python-ew) Python 2.x compatible modules by [OSOP](http://www.osop.com.pa).

```python_ew``` is a Python wrapper for accessing a Earthworm shared memory rings, allowing you to extend the Earthworm system with Python code.

Earthworm is a set of opensource programs, tools and libraries that are used in the development of software for maintaining seismic networks, research and other seismological and geophysical applications. 
http://vps.isti.com/trac/ew/

### Installation

In order to follow theses steps, Earthworm needs to be previously
installed in your computer. Also, note that these are steps for GNU/Linux - UNIX only.

1. Ensure that the `EW_HOME` environment variable points to the folder that contains the ```/include/``` and ```/lib/``` folders for earthworm.
2. Build the ```ringreader.o``` and ```ringwriter.o``` earthworm interface code, and copy them and their associated header files to the appropriate places in the earthworm distribution:

       cd ring_access
       make
       cp ringreader.o ringwriter.o ${EW_HOME}/lib
       cp ringreader.h ringwriter.h ${EW_HOME}/include

3. Install the python module:
    
       python3 setup.py build
       python3 setup.py install

### Example usage

Reading ```TYPE_TRACEBUF2``` message from a ring.  Let's assume your ring is named ```WAVE_RING```.

    python3
    >>> from python_ew.tracebuf2.tracebuf2ring import Tracebuf2Ring
    >>> ring = Tracebuf2Ring('WAVE_RING', 'MOD_WILDCARD')
    >>> packets = ring.read()
    >>> packets[0]
    {'pinno': 0, 'nsamp': 100, 'starttime': 1564770703.968393, 'endtime': 1564770704.958393, 'samprate': 100.0, 'sta': 'FOO', 'net': 'XX', 'chan': 'HNN', 'loc': '--', 'version': '20', 'datatype': 'i4', 'quality': '', 'pad': '', 'samples': [-22129, -22130, -22131, -22132, -22129, -22130, -22128, -22128, -22130, -22128, -22130, -22128, -22128, -22129, -22129, -22129, -22129, -22130, -22127, -22128, -22129, -22128, -22128, -22130, -22131, -22128, -22131, -22131, -22128, -22128, -22132, -22130, -22125, -22128, -22129, -22126, -22128, -22130, -22133, -22132, -22131, -22132, -22130, -22131, -22128, -22129, -22132, -22127, -22129, -22129, -22129, -22132, -22130, -22127, -22129, -22131, -22127, -22128, -22131, -22128, -22128, -22130, -22129, -22130, -22129, -22128, -22133, -22128, -22129, -22133, -22131, -22130, -22128, -22131, -22130, -22128, -22132, -22132, -22129, -22127, -22129, -22132, -22130, -22132, -22133, -22128, -22129, -22130, -22129, -22130, -22128, -22129, -22130, -22131, -22130, -22128, -22129, -22130, -22129, -22129]}
    

