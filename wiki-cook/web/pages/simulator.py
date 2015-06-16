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
						
			template_params['user'] = 'guest'
			template_params['loginUrl'] = User.loginUrl()
			self.redirect('/index')
			return
			
		else:
			template_params['logoutUrl'] = User.logoutUrl()
			template_params['user'] = user.email
			template_params['name_recipe'] = self.request.get('myvar')
			details = Recipe.getDetailsByName(self.request.get('myvar'))
			template_params['pic_url'] = details.pic_url
							
			recipeSteps=[]
			recipeSteps= details.step.split("\n");
			json_step = json.dumps(recipeSteps)
			template_params['recipeStep'] = json_step 
			most_recipes = Recipe.try_get_most_viewed()
			if (most_recipes):
				
				template_params['most_views'] = most_recipes
				
		html = template.render("web/templates/simulator.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/simulator', IndexHandler)
], debug=True)
