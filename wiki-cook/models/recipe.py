from google.appengine.ext import ndb

from user import User
 
class Recipe(ndb.Model):
	user = ndb.KeyProperty(kind=User)
	nameRecipe = ndb.StringProperty()
	ingredients = ndb.TextProperty()
	typeRecipe = ndb.StringProperty() # חלביבשרי
	step = ndb.TextProperty()
	pic_url=ndb.TextProperty()
	
	def setType(self):
		self.typeRecipe = 'jkch'
		self.ingredients = 'bla bla'
		self.user = user.key
		self.nameRecipe = 'omlete'
		self.step = 'omlete'
		self.put()
		
	@staticmethod
	def getAllRecipe(user):
		recipes=[] # array for name recipe
		results= Recipe.query()  # get name recipe from table
		if (results):
			for recipe in results:
				recipes.append(recipe)
			return recipes
		return None
	
