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
			template_params['loginUrl'] = User.loginUrl('editrecipe')

		else:
			template_params['user'] = user.email
			template_params['logoutUrl'] = user.logoutUrl()
			template_params['name_recipe'] = self.request.get('myvar')
		
		details = Recipe.getDetailsByName(self.request.get('myvar'))
		
		most_recipes = Recipe.try_get_most_viewed()
		
		if (most_recipes):
			
			template_params['most_views'] = most_recipes
			
		template_params['pic_url'] = details.pic_url
		
		
		ingredients=[]
		ingredients= details.ingredients.split("\n");
		template_params['ingredients'] = details.ingredients
		
		
	
		
		template_params['recipeStep'] = details.step
			
			
		html = template.render("web/templates/editrecipe.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/editrecipe', IndexHandler)
], debug=True)
