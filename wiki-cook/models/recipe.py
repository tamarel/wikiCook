from google.appengine.ext import ndb

from user import User
 
class Recipe(ndb.Model):
	user = ndb.KeyProperty(kind=User)
	nameRecipe = ndb.StringProperty()
	ingredients = ndb.TextProperty()
	type = ndb.IntegerProperty() # חלביבשרי
	step = ndb.TextProperty()
	

	def setType(self):
		self.type = 0
		self.ingredients = 'bla bla'
		self.user = user.key
		self.nameRecipe = 'omlete'
		self.step = 'omlete'
		self.put()
	
