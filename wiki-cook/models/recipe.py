from google.appengine.ext import ndb

from user import User
import logging
class Recipe(ndb.Model):
	user = ndb.StringProperty()
	nameRecipe = ndb.StringProperty()
	ingredients = ndb.TextProperty()
	typeRecipe = ndb.StringProperty() # חלביבשרי
	step = ndb.TextProperty()
	pic_url=ndb.TextProperty()
	recipe_count=ndb.IntegerProperty()
	
	
		
	@staticmethod
	def getAllRecipe(user):
		recipes=[] # array for name recipe
		results= Recipe.query()  # get name recipe from table
		if (results):
			for recipe in results:
				recipes.append(recipe)
			return recipes
		return None
		
	@staticmethod
	def getDetailsByName(name_recipe):
		Details = Recipe.query(Recipe.nameRecipe == name_recipe).get()
		return Details
		
	@staticmethod
	def setCount(name_recipe):
		recipe = Recipe.query(Recipe.nameRecipe == name_recipe).get()
		recipe.recipe_count +=1
		recipe.put()
	
	@staticmethod
	def try_get_most_viewed():
		
		recipes=[]
		results= Recipe.query()
		max=-1;
		
		if (results):
			for recipe in results:
				if (recipe.recipe_count > max):
					max =  recipe.recipe_count 
					logging.info("ddddddd")
					max_recipe = recipe 
				
			return max_recipe
	#	most_viewed= Recipe.query.order(Recipe.recipe_count).get()
		return None
		

