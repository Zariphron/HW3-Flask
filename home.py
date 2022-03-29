from flask import Flask

myapp_obj = Flask(__name__)

name = "Lisa"
@myapp_obj.route("/")
def home():
    city_list = ['Paris', 'London', 'Rome', 'Tahiti']
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

#myapp_obj.run()
