#from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.api import mail
from models.recipe import Recipe
from models.user import User
import webapp2
import json
import string

class IndexHandler(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		user = User.checkUser()
		if not user:
			template_params['loginUrl'] = User.loginUrl()
		else:
			template_params['logoutUrl'] = User.logoutUrl()
			template_params['user'] = user.email
#			html = self.redirect('/salesEvents')
			most_recipes = Recipe.try_get_most_viewed()
			
			if (most_recipes):
				
				template_params['most_views'] = most_recipes
		html = template.render("web/templates/about.html", template_params)
		self.response.write(html)

app = webapp2.WSGIApplication([
	('/about', IndexHandler)
], debug=True)


class sendMailContactUs(webapp2.RequestHandler):
	def get(self):
		template_params = {}
		mailfrom = self.request.get('mailfrom')
		name = self.request.get('name')
		message = self.request.get('message')
		if not mail.is_email_valid(mailfrom):
			return
		mail.send_mail(sender="wiki-cook.appspot.com <tamareliyahou@gmail.com>",
						to="tamareliyahou@gmal.com<tamareliyahou@gmail.com>",
						subject="USER CONTACT US",
						body="""
FROM: """+name+"""
MAIL: """+mailfrom+"""
"""+message+"""
______________________________________________________________________________________
The wikiCook Team. www.wiki-cook.appspot.com.
""")
		self.response.write(json.dumps({'status':'OK'}))


app = webapp2.WSGIApplication([
	('/about', IndexHandler),
	('/sendcontactus',sendMailContactUs)
], debug=True)