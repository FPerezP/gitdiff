import urllib2
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
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
        self.diff_html = ''

    def getDiff(self):
        try:
            req = urllib2.Request(self.url + '.diff')
            raw_diff = urllib2.urlopen(req).read()

            lexer = get_lexer_by_name('diff')
            formatter = HtmlFormatter(noclasses=True)
            self.diff_html = highlight(raw_diff, lexer, formatter)
            return self.diff_html
        except Exception, e:
            logging.error('Cannot get diff: ' + e.message)
            return ''

    def __str__(self):
        return "<div class='commit'>" \
        + "<div><strong>Author: </strong>" + str(self.author) + "</div>" \
        + "<div><strong>Message: </strong>" + self.message + "</div>" \
        + "<div><strong>Date: </strong>" + self.date + "</div>" \
        + "<div><strong>Id: </strong><a href='" + self.url + "'>" + self.commitId + "</a></div>" \
        + self.diff_html \
        + "<br /><br />" \
        + "</div>"