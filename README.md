### About

Accepts github PUSH requests with information about commits beeing pushed to repository and sends emails with diffs. May be run as [Heroku](http://www.heroku.com/) app.

### Installation
This app is built on top of [Flask](http://flask.pocoo.org/) thus runs like a typical WSGI application. 

The installation is simple:

```bash
# clone repository
git clone git://github.com/kalimatas/gitdiff.git

# make a virtual environment and activate it
virtualenv --distribute --system-site-packages venv
source venv/bin/active

# install requirements
pip install -r requirements.txt

# copy sample config and edit it
cp config.example.yaml config.yaml 
```

If you use Heroku you can run a development server:

```bash
# starts a server at http://0.0.0.0:5000
foreman start
```


### Usage
Add a webhook to your Github repository as described [here](https://help.github.com/articles/post-receive-hooks) and point it to your running app.
