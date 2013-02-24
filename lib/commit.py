import urllib2
from lib.author import Author
import logging

class Commit:
    def __init__(self, commitId, author, message, date, url):
        if not isinstance(author, Author):
            raise ValueError('Author must be an instance of Author class')

        self.commitId = commitId
        self.author = author
        self.message = message
        self.date = date
        self.url = url

    def getDiff(self):
        try:
            req = urllib2.Request(self.url + '.diff')
            rsp = urllib2.urlopen(req)
            return rsp.read()
        except Exception, e:
            logging.error('Cannot get diff: ' + e.message)
            return ''

    def __str__(self):
        return 'Commit class'