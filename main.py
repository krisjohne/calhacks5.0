import webapp2
import jinja2
import os
import logging
import json
from google.appengine.api import *

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexPage(webapp2.RequestHandler):
    def get(self):
        mypage = env.get_template('templates/index.html')
        self.response.write(mypage.render())

app = webapp2.WSGIApplication([
    ('/', IndexPage)
], debug=True)
