#from google.appengine.api import users
from google.appengine.ext.webapp import template


import webapp2
import json
from models.user import User
from models.recipe import Recipe


class IndexHandler(webapp2.RequestHandler):

	def get(self):
		template_params = {}
		user = User.checkUser()
		if not user:
			template_params['loginUrl'] = User.loginUrl()
		else:
			recipe = Recipe();
			recipe.nameRecipe = self.request.get('nameRecipe')
			recipe.ingredients= self.request.get('ingredients')
			recipe.typeRecipe= self.request.get('typeRecipe')
			recipe.step= self.request.get('step')
			recipe.put()
			
		html = template.render("web/templates/addrecipes.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/addrecipes', IndexHandler)
], debug=True)
