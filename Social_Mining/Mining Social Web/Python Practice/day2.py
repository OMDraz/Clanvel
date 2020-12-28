import re 
import os 

line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re 
fields = re.split(r'[:\s]\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

filenames = os.listdir('.')
[name for name in filenames if name.endswith(('.c', '.h')) ]
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen 

def read_data(name):
    if name.startswith(('http','https:','ftp:')):
        return urlopen(name).read() 
    else:
        with open(name) as f:
            return f.read()


