# HTTP Crawler

This scenario shows basic usage of a HTTP crawler based on Python scripts. The script works as follows:

1. Page form the defined address is downloaded.

2. URL links in the given domain are extracted, shuffled and add to a list to visit.

3. Script waits random interval between 0 and 10 seconds, selects next address to visit and go to point 1.

There are available three backend for crawling pages:

- Headless **chrome**
- Crawler based on **urllib** library
- Crawler based on **wget** utility

All three backend tries to download not only html code of a web page but also a page content like images,
css files, and javascript files. 

More detailed info can be gathered by inspecting the source code.

## Usage


```
python run.py -p https://www.example.com -c chrome
```

```
python run.py -p https://www.example.com -c wget
```

```
python run.py -p https://www.example.com -c urllib
```
