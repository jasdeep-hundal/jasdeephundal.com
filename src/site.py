from flask import Flask, render_template
from flask_flatpages import FlatPages

FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route('/')
def index():
    return page('about')

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template(path + '.html', page=page, pages=pages)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0')
