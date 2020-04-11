from flask import (Flask,render_template,abort,jsonify,request,redirect,url_for)
import model

app =Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=["GET","POST"])
def add_country():
    if request.method =="POST":
        country= {"country":request.form['country'],
                  "patients":request.form['patients']}
        country1 = request.form['country']
        patients1 = request.form['patients']
        number_of_current = model.number_of_curent_patients(country1)
        if model.check_if_alredy_exist(country1):
            counter = model.number_in_json(country1)
            total=model.add_key_to_dict(country1,patients1,number_of_current)
            model.db[counter-1]['total']=total 
            model.db[counter-1]['patients']=patients1 
            model.save_db(model.db)      
            return redirect(url_for('view_country', index =counter-1))
        else:
            model.db.append(country)
            model.save_db(model.db)
        return redirect(url_for('view_country', index =len(model.db)-1))
    else:
        return render_template("welcome.html")
        


@app.route('/country/<int:index>')
def view_country(index):
    try:
        country=model.db[index]
        return render_template("country.html",country=country)
    except IndexError:
     abort(404)
    
@app.route('/viewcountries')
def view_all_countries():
    return render_template("all_countries.html",countries=model.db)

@app.route('/api/viewcountries')
def view_all_countries_api():
    return jsonify(model.db)

@app.route('/api/country/<int:index>')
def view_country_api(index):
    try:
      return model.db[index]
    except IndexError:
        abort(404)


# @app.route('/remove_country/<int:index>', methods=["GET","POST"])
# def remove(index):
#     if request.method == "POST":
#       del db[index]
#       save_db()
#       return redirect(url_for('welcome.html'))
#     else:
#       return render_template("remove_country.html",country=db[index])