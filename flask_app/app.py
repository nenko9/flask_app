# from crypt import methods
from flask import Flask, render_template, request
# export FLASK_DEBUG=1


app = Flask(__name__)
# app.run(debug=True)
@app.route("/", methods=["GET", "POST"])

        
def IndexPage():
        # def Searcher():
        #         return 'find'

        if request.method=='POST':
                # vv = request.form['search']
                search_query = request.form['search_query']
                # print('Post was reciev', vv)
                # return render_template('index.html')
        else:
                return render_template('index.html')

        return render_template('index.html')

if __name__ =='__main__':
        app.run()