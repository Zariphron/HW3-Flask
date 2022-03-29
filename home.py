from flask import Flask

myobj = Flask(__name__)

name = "Lisa"
city_list = ['Paris', 'London', 'Rome', 'Tahiti']
@myobj.route("/")
def home():
    outs = ""
    for city in city_list:
        outs = outs + f'<li>{city}</li>'
    final_out = '''
    <html>
        <body>
            <h1>Welcome ''' + name + '''!</h1>
            <a href="www.google.com">not google</a>
            <ul>''' + outs + '''</ul>
        </body>
    </html>'''
    return final_out

#myobj.run()
