from google.appengine.ext import ndb

from user import User
 
class Recipe(ndb.Model):
	#user = ndb.KeyProperty(kind=User)
	nameRecipe = ndb.TextProperty()
	ingredients = ndb.TextProperty()
	typeRecipe = ndb.StringProperty() # חלביבשרי
	step = ndb.TextProperty()
	

	def setType(self):
		self.typeRecipe = 'jkch'
		self.ingredients = 'bla bla'
		self.user = user.key
		self.nameRecipe = 'omlete'
		self.step = 'omlete'
		self.put()
	
