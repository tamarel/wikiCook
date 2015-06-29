#from google.appengine.api import users
from google.appengine.ext.webapp import template


import webapp2
import json
from models.user import User
from models.recipe import Recipe


class IndexHandler(webapp2.RequestHandler):

	def get(self):
		template_params = {}
		user = User.connect()
		user = User.checkUser()
		most_recipes = Recipe.try_get_most_viewed()
		
		if (most_recipes):
				
			template_params['most_views'] = most_recipes	
			
		if not user:
			template_params['loginUrl'] = User.loginUrl('save')

		else:
			Recipe.deleterecipes(self.request.get('nameold'))
			template_params['user'] = user.email
			template_params['logoutUrl'] = user.logoutUrl()
			recipe = Recipe();
			recipe.nameRecipe = self.request.get('nameRecipe')
			recipe.ingredients = self.request.get('ingredients')
			recipe.typeRecipe = self.request.get('typeRecipe')
			recipe.step = self.request.get('list_of_step')
			recipe.pic_url = self.request.get('pic_url')
			recipe.recipe_count=0
			recipe.user = user.email
			recipe.put()
			
		html = template.render("web/templates/recipeofuser.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/save', IndexHandler)
], debug=True)
