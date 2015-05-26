#from google.appengine.api import users
import config
import logging

from google.appengine.ext.webapp import template

from models.user import User
import webapp2

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		user = User.checkUser()
		
		if not user:
			self.redirect('/')
			return
		
		template_params['user'] = user.email
		template_params['logoutUrl'] = user.logoutUrl()

		
		html = template.render("web/templates/home.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/', IndexHandler),
	('/home', IndexHandler),

], debug=True)
