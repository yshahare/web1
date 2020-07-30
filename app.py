from flask import Flask, render_template,request
#from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='', server='localhost', database='website1')
#db = SQLAlchemy(app)

#class Enquiry(db.Model):
#	srno = db.Column(db.Integer, primary_key=True)
#	fi#rstname = db.Column(db.String(80),unique=False, nullable=False )
#	las#tname = db.Column(db.String(80),unique=False, nullable=False )
#	emai#l= db.Column(db.String(80), nullable=False )
#	need=db.Column(db.String(80),unique=False, nullable=False )
#	contactno=db.Column(db.Integer, nullable=False )
#	address=db.Column(db.String(80),unique=False, nullable=False )
#	message=db.Column(db.String(80),unique=False, nullable=False )


    
    
	
		

@app.route('/')

def Home():

	return render_template('index.html')

@app.route('/about')

def about():
	
	return render_template('about.html')

@app.route('/services')

def services():
	
	return render_template('services.html')

@app.route('/products')

def products():
	
	return render_template('products.html')
	
@app.route('/thermo')
def thermo():
		return render_template('thermocouple-tips.html')

@app.route('/temparature')
def temparature():
		return render_template('temperature-measuring-instrument.html')

@app.route('/carbons')
def carbons():
		return render_template('carbon-silicon-analyzer.html')

@app.route('/carbonc')
def carbonc():
		return render_template('carbon-cups.html')

@app.route('/samplers')
def samplers():
		return render_template('samplers.html')

@app.route('/accessories')
def accessories():
		return render_template('accessories.html')

@app.route('/spares')
def spares():
		return render_template('spares.html')


@app.route('/newsevents')

def newsevents():
	
	return render_template('newsevents.html')

@app.route('/globalp')

def globalp():
	
	return render_template('globalp.html')

@app.route('/contacts')

def contacts():
	
	return render_template('contacts.html')

@app.route('/enquiry', methods=['GET','POST'])

def enquiry():
	
	#if(request.method=='POST'):
	#	name =request.form.get('name')
	#	surname=request.form.get('surname')
#	#	Email=request.form.get('Email'#)
#	#	specify=request.form.get('speci#fy')
#	#	contact=request.form.get('contac#t')
#	#	address=request.form.get('address#')
#	#	message=request.form.get('message'#)
#	#	entry=Enquiry(firstname=name, lastn#ame=surname, email=Email, need=specify, contactno=contact, address=address, message=message)
#	#	db.session.add(entry)#
#		db.session.commit()	#
#	  #
	return render_template('enquiry.html')	

if __name__ == '__main__':
	
	app.run(debug=True)		


	
