import json
import sys
import argparse
from collections import defaultdict
import os.path
from datetime import datetime
from json import JSONEncoder

from collections import Counter

parser = argparse.ArgumentParser(description='Change directories intelligently')
parser.add_argument(
    'directory',
    help="directory to change to",
    nargs='+'
)

class Entry():
    def __init__(self, content):
        self.body = content
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.type = "entry"

    def __str__(self):
        return "> " + self.body

    def __repr__(self):
        return self.__str__()


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def from_json(dict):
    if 'type' in dict and dict['type'] == 'entry':
        e = Entry(dict['body'])
        e.time = dict['time']
        return e
    else:
        return dict

def emit(path): # can either chdir or print the path
    print(path)

def sanitize(path):
    return os.path.abspath(os.path.expanduser(path))

def load_cache(cache_file):
    try:
        with open(cache_file, 'r+') as f:
            d = json.load(f, object_hook=from_json)
            cache = defaultdict(Counter, {k: Counter(v) for k, v in d.items()})
    except FileNotFoundError:
        cache = defaultdict(Counter)
    
    return cache

def complete_path(directory, cache):
    """
        finds a matching full directory in cache matching the partial name directory

        directory (string) -- partial name
        cache (default dict of Counters) -- used for storing historic data

        returns: 
            updated cache
    """

    if directory in cache.keys():
        basename = os.path.basename(directory)
        
        if len(cache[directory]) == 0:
            raise FileNotFoundError('Directory {} does not exist.'.format(directory))

        fullpath = cache[directory].most_common(1)[0][0]

        cache[basename].update([fullpath])

        if not os.path.exists(fullpath) or not os.path.isdir(fullpath):
            del cache[basename][fullpath]
            return complete_path(directory, cache)

        emit(fullpath)

        return cache
    else:
        raise FileNotFoundError('Directory {} does not exist.'.format(directory))

def main():
    cache_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache.json')

    args = sys.argv

    if len(args) == 1 or len(args[1]) == 0:
        emit(os.path.expanduser('~'))
        return
    elif args[1] == '..':
        emit('..')
        return

    args = parser.parse_args(args[1:])
    directory = args.directory[0]

    cache = load_cache(cache_file)

    # list of directories with name and counts. when a new directory is accessed increment the count, keep it sorted.
    if os.path.exists(directory) and os.path.isdir(directory):
        basename = os.path.basename(directory.strip('/'))
        fullpath = sanitize(directory)
        cache[basename].update([fullpath])
        
        emit(fullpath)

        with open(cache_file, 'w+') as f:
            json.dump(dict(cache), f, cls = MyEncoder)

        return

    cache = complete_path(directory, cache)

    with open(cache_file, 'w+') as f:
        json.dump(dict(cache), f, cls=MyEncoder)

if __name__ == '__main__':
    main()
