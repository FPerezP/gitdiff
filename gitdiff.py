from flask import Flask
from flask import request
from flask import abort
from flask import render_template
from lib.author import Author
from lib.commit import Commit
from lib.sender import Sender
import json
import yaml
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='"%(asctime)s %(levelname)8s %(name)s - %(message)s"',
    datefmt='%H:%M:%S'
)

def parse_request(payload):
    """Parses POST requst from Github and
    returns list of Commit objects.
    """
    payload = json.loads(payload, encoding='utf-8')
    commits = []
    for commitInfo in payload['commits']:
        author = Author(name=str(commitInfo['author']['name']),
                        email=str(commitInfo['author']['email']))
        commit = Commit(commitId=str(commitInfo['id']),
                        author=author,
                        message=str(commitInfo['message']),
                        date=str(commitInfo['timestamp']),
                        url=str(commitInfo['url']))
        commits.append(commit)
    return commits

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_github_push():
    try:
        if not 'payload' in request.form:
            raise ValueError

        commitList = parse_request(request.form['payload'])
        sender = Sender(commitList)

        template = open('templates/layout.html').read() % sender.body
        sender.send(template)
        return 'Ok'
    except Exception, e:
        logging.error(e.message)
        abort(500)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    config = yaml.load(open('config.yaml'))
    web_config = config.get('web')
    app.run(host=web_config['host'], port=int(web_config['port']))