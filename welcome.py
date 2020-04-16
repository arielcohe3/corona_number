from flask import (Flask,render_template,abort,jsonify,request,redirect,url_for)
import model
import importall
import requests as req
import json
import lxml.html

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
        # allcountries=importall.rb
        country=model.db[index]
        return render_template("country.html",country=country,allcountries=importall.rb)
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

@app.route('/elie', methods=["GET"])
def return_json():
    x = req.get('https://jsonplaceholder.typicode.com/albums')
    y = json.loads(x.content)
    # y = model.returnjson(str(x))    
    return jsonify(y)

list = []
dict_to_send_json = {}
@app.route('/getall', methods=["GET"])
def getall():
    global dict_to_send_json
    global list
    global i
    response = req.get('https://www.worldometers.info/coronavirus/')
    content = str(response.content)
    html = lxml.html.fromstring(content)
    table = html.get_element_by_id("main_table_countries_today")
    trs = table.xpath("//tr")
    ths = table.xpath(".//th")
    for th in ths : 
            list.append(f"{th.text_content()}")
    for tr in trs : 
        # ths = tr.xpath(".//th")
        tds = tr.xpath(".//td")
        for td in tds:
            zero_counter()
            key=list[i]
            dict_to_send_json[key] = td.text_content()
            print(dict_to_send_json)
            i += 1         
            convert_dict_to_json()
    return jsonify({"ss":"ff"})
    
i=0
def zero_counter():
    global i
    if(i==13):
        i = 0
    # print(list[i])
    

def convert_dict_to_json():
    global dict_to_send_json
    if i==13:
        importall.rb.append(dict_to_send_json)
        importall.from_html_to_json(importall.rb)
        dict_to_send_json={}
