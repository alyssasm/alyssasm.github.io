
import webapp2
import jinja2
import os


jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__))) 


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class MadlibHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('alyssasmadlibs.html')
		self.response.write(template.render())

	def post(self):
		character_name = self.request.get('cName')
		adjective = self.request.get('adj')
		age = self.request.get('age')
		role = self.request.get('role')
		show_name = self.request.get('showname')
		age2 = self.request.get('age2')
		character_name2 = self.request.get('cName2')
		shorttime = self.request.get('shorttime')
		date = self.request.get('date')
		adverb = self.request.get('adv')
		numyears = self.request.get('numyears')
		newshow = self.request.get('newshow')
		newshowcharacter = self.request.get('newshowcharacter')
		
		template = jinja_environment.get_template('alyssasmadlibs_out.html')
		self.response.write(template.render(
			{
				'character' : character_name,
				'adjective' : adjective,
				'age' : age,
				'role' : role,
				'showname' : show_name,
				'age2': age2,
				'character2' : character_name2,
				'shorttime': shorttime,
				'date' : date,
				'adverb': adverb,
				'numyears' : numyears,
				'newshow' : newshow,
				'newshowcharacter' : newshowcharacter,
				
			}))
		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/alyssasmadlib', MadlibHandler)
], debug=True)
