#from google.appengine.api import users
from google.appengine.ext.webapp import template

from models.user import User
import webapp2

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		user = User.connect()
		if not user:
			self.redirect('/')
		else:
			self.redirect('/home')

app = webapp2.WSGIApplication([
	('/home', IndexHandler)
], debug=True)
