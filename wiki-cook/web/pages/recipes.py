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
			all_recipes=Recipe.getAllRecipe(user)
			recipes=[]
			if (all_recipes):
				for recipe in all_recipes:
					recipe_name = recipe.nameRecipe
					pic_url = recipe.pic_url
					if pic_url is None:
						pic_url="http://crossfit-marietta.com/wp-content/plugins/nertworks-all-in-one-social-share-tools/images/no_image.png"
					recipe_and_pic = [recipe_name,pic_url]
					recipes.append(recipe_and_pic)
				template_params['recipes'] = recipes
		html = template.render("web/templates/recipes.html", template_params)
		self.response.write(html)
		return

app = webapp2.WSGIApplication([
	('/recipes', IndexHandler)
], debug=True)
