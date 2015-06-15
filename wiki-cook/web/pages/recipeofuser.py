﻿#from google.appengine.api import users
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
			all_recipes = Recipe.getRecipeByUser(user)
			recipes=[]
			if (all_recipes):
				for recipe in all_recipes:
					recipe_name = recipe.nameRecipe
					pic_url = recipe.pic_url

					if recipe_name:
						recipe_and_pic = [recipe_name,pic_url]
						recipes.append(recipe_and_pic)
				template_params['recipes'] = recipes
			template_params['user'] = user.email
			template_params['logoutUrl'] = user.logoutUrl()
			
			most_recipes = Recipe.try_get_most_viewed()
			recipess=[]
			if (most_recipes):
				
				template_params['most_views'] = most_recipes
				
		html = template.render("web/templates/recipeofuser.html", template_params)
		self.response.write(html)
		return

app = webapp2.WSGIApplication([
	('/recipeofuser', IndexHandler)
], debug=True)
