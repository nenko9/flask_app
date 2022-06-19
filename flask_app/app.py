# from crypt import methods
from unittest.mock import seal
from flask import Flask, render_template, request
from search_engine import Search, GetResult
# export FLASK_DEBUG=1

class Advertisment():
        def __init__(self, title, price):
                self.title=title
                self.price=price


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def IndexPage():
        a0=Advertisment('default','default')
        a1=Advertisment('Razer Balde',120000)
        a2=Advertisment('HP Omen Beast',70000)
        al=[a0, a1, a2]
        # return render_template('adv.html')
        if request.method=='POST':
                search_data=request.form['search_query']
                if search_data: 
                        Search(search_data)
                else:
                        return render_template('index.html')
                # print(GetResult(search_data))
                return render_template('adv.html', data=GetResult(search_data))
        else:
                return render_template('index.html')

if __name__ =='__main__':
        app.run()