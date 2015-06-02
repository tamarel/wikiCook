#from google.appengine.api import users
from google.appengine.ext.webapp import template
from operator import itemgetter, attrgetter
from models.recipe import Recipe
from models.user import User
import operator 
import webapp2
import json

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		
		user = User.checkUser()
		if not user:
			template_params['loginUrl'] = User.loginUrl()

		else:
			template_params['name_recipe'] = self.request.get('myvar')
			
			details = Recipe.getDetailsByName(self.request.get('myvar'))
			template_params['ingredients'] = details.ingredients
			
			template_params['pic_url'] = details.pic_url
							
		html = template.render("web/templates/featured.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/featured', IndexHandler)
], debug=True)
