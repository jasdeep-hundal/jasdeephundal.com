import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return page('about')

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template(path + '.html', page=page, pages=pages)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
        freezer.freeze()
    else:
        app.run(debug=True)
