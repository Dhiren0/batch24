from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
	app.run(debug=True)
	return render_template('index.html')

@app.route('/<string:pagenm>')
def f(pagenm):
	app.run(debug=True)
	return render_template(pagenm)

def write_data(data):
	with open('database.txt',mode='a') as database:
		email = data['email']
		message = data['message']
		file = database.write(f'\n{email},{message}')

def write_csv(data):
	with open('database.csv',mode='a',newline='') as database:
		email = data['email']
		message = data['message']
		r= csv.writer(database, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		r.writerow([email,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method =="POST":
		try:
			#data = request.form['email']
			data = request.form.to_dict()
			write_csv(data)
			E = data['email']
			splited = E.split('@')
			usern = splited[0]
			do = splited[1]
			domain = do.split('.')
			d = domain[1]
			print("User Name:",usern)
			print("Domain: ."+d)
			#return data
			return render_template("/thank.html",username=usern,dom=d)
			#return redirect("/thank.html",username=usern,dom=d)	
		except:
			return 'did not save to database'

	else:
		return "Something went wrong. Try again!"