#from google.appengine.api import users
from google.appengine.ext.webapp import template
from models.recipe import Recipe
from operator import itemgetter, attrgetter
from models.user import User
import webapp2
import logging
import json
import operator 

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		user = User.checkUser()
		if not user:
			template_params['loginUrl'] = User.loginUrl()
		else:
			template_params['logoutUrl'] = User.logoutUrl()
			template_params['user'] = user.email
			

		most_recipes = Recipe.try_get_most_viewed()
		recipess=[]
		if (most_recipes):
			for recipe in all_recipes:
				recipe_name = recipe.nameRecipe
				pic_url = recipe.pic_url

				if recipe_name:
					recipe_and_pic = [recipe_name,pic_url]
					recipess.append(recipe_and_pic)
			template_params['most_views'] = recipess
			
			
			
		
		html = template.render("web/templates/master_page.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/master_page', IndexHandler)
], debug=True)
