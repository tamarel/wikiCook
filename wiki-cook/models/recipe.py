from google.appengine.ext import ndb

from user import User
import logging
class Recipe(ndb.Model):
	user = ndb.StringProperty()
	nameRecipe = ndb.StringProperty()
	ingredients = ndb.TextProperty()
	typeRecipe = ndb.StringProperty() 
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
	def getRecipeByUser	(user):
		recipes=[] # array for name recipe
		results= Recipe.query()  # get name recipe from table
		if (results):
			for recipe in results:
				if ( recipe.user ==  user.email):
					recipes.append(recipe)
			return recipes
		return None
		

	@staticmethod
	def setCount(name_recipe):
		recipe = Recipe.query(Recipe.nameRecipe == name_recipe).get()
		recipe.recipe_count +=1
		recipe.put()
	
	@staticmethod
	def try_get_most_viewed():
		
		recipes=[]
		results= Recipe.query()
		max_h=-1
		max_t=-1
		recipe_name_one=' '
		recipe_name_two=' '
		recipe_and_pic_one =[]
		recipe_and_pic_two =[]
		pic_one=' '
		pic_two=' '
		if (results):
			for recipe in results:
				if (recipe.recipe_count > max_h):
					max_t = max_h
					max_h =  recipe.recipe_count 
					
					recipe_name_two = recipe_name_one 
					recipe_name_one = recipe.nameRecipe 
					
					pic_two=pic_one
					pic_one=recipe.pic_url

					recipe_and_pic_one =[ recipe_name_one , pic_one ]
					recipe_and_pic_two = [ recipe_name_two , pic_two ]
					
				elif (recipe.recipe_count > max_t):
					max_t = recipe.recipe_count
					
					
					recipe_name_two = recipe.nameRecipe 
				
					
					pic_two=recipe.pic_url
					recipe_and_pic_two = [ recipe_name_two , pic_two ]				
			recipes =[ recipe_and_pic_one, recipe_and_pic_two]	
			return recipes
	#	most_viewed= Recipe.query.order(Recipe.recipe_count).get()
		return None
		
	@staticmethod
	def deleterecipes(recipename):
		
		recipe=Recipe.getDetailsByName(recipename)
		if recipe is not None:
			recipe.key.delete();
		return
