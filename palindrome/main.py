
import webapp2
import jinja2
import os
import random



def is_palindrome(word):
	first_half = None
	second_half = None

	if len(word) % 2 == 0:
		first_half = len(word) / 2
		second_half = len(word) /2 
	else: 
		first_half = (len(word) / 2) + 1
		second_half = len(word) / 2

	first_half= word[:first_half]
	second_half= word[second_half:]
	second_half= second_half[::-1]

	if first_half == second_half:
		return word + ' is a palindrome!'
	else:
		return word + ' is not a palindrome...'

class PalHandler(webapp2.RequestHandler):
	def get(self) :
		self.response.write (is_palindrome('kayak '))
		self.response.write (is_palindrome('racecar '))
		self.response.write (is_palindrome('katniss everdeen '))



jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__))) 

class TemplateHandler(webapp2.RequestHandler):
	def get(self):
		palindrome_output = (
			is_palindrome('kayak'))
		template = (
			jinja_environment.get_template('temp.html'))
		self.response.write(template.render(
			{'palindrome': palindrome_output}))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		palindrome_output= is_palindrome('kayak')
		self.response.write(palindrome_output)

class FortuneHandler(webapp2.RequestHandler):
	def get(self):
		fortunes = [
			'something bad',
			'something good',
			'something mysterious',
			'IDK'
			]
		rand_fortune= random.choice(fortunes)
	
		template = (
			jinja_environment.get_template('fortunes.html'))
		self.response.write(template.render(
			{
				'random_fortune' : rand_fortune
			}))

class SumHandler(webapp2.RequestHandler):
	def get(self):
		first_num = self.request.get('num1')
		second_num = self.request.get('num2')

		first_num = int(first_num)
		second_num = int(second_num)

		sum_o_nums = first_num + second_num

		template = jinja_environment.get_template('sum.html')
		self.response.write(template.render(
			{
				'first_num' : first_num,
				'second_num' : second_num,
				'sum': sum_o_nums,
			}))		
# enter numbers in your url  after /sum : ?num1=10&num2=10 ; 
#10s are just random numbers

class MovieHandler(webapp2.RequestHandler):
	def get(self):
		name = self.request.get('name') or 'n/a'
		length = self.request.get('length') or 0
		num_reviews = self.request.get ('num_reviews') or 0
		stars = self.request.get('stars') or 0

		name = name
		length = int(length)
		num_reviews = int(num_reviews)
		stars = int(stars)

		# if num_reviews>30 and stars>3 :
		# 	self.response.write('This movie must be great!')
		# elif num_reviews<5 and stars<5 :
		# 	self.response.write('Im not sure about this movie')
		# elif num_reviews==0 :
		# 	self.response.write('This movie needs some reviews. Be the first to review!')


		template = jinja_environment.get_template('movies.html')
		self.response.write(template.render(
			{
				'name' : name,
				'length' : length,
				'num_reviews': num_reviews,
				'stars': stars,
			}))

# localhost:8080/movies?name=Spotlight&length=120&num_reviews=30&stars=5

class MadlibHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('madlib.html')
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
		
		template = jinja_environment.get_template('madlib_out.html')
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
			}))
		



app = webapp2.WSGIApplication([
	('/', PalHandler),
	('/template', TemplateHandler),
	('/fortune', FortuneHandler),
	('/sum', SumHandler),
	('/movies', MovieHandler),
	('/madlib', MadlibHandler)
],debug=True)
