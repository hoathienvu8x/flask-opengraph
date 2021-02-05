from opengraph import app
from flask import render_template, Markup, jsonify, make_response, request
import markdown
from api import OpenGraph

# https://developpaper.com/question/flask-jinja2-sqlite3-how-to-save-markdown-format-articles/
"""
Markdown text is stored in the database, and a filter is implemented on the server side in jinja2, 
rendering HTML to display markdown. The filter I defined is as follows:

```python
from app import app
from flask import Markup
import markdown

@app.template_filter('markdown')
def neomarkdown(markdown_content):
    content = Markup(markdown.markdown(markdown_content))
    return content
```

Usage:

```jinja2
{{ html_content | markdown }}
```
"""

@app.template_filter('markdown')
def neomarkdown(markdown_content):
    return Markup(markdown.markdown(markdown_content))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods = [ 'GET', 'POST' ])
def do_fetch():
    if request.method == "POST":
        req = request.form
    else:
        req = request.args
    url = req.get('u','')
    if not url:
        return make_response(jsonify({ 'error' : 'Not Found' }), 404)
    ogp = OpenGraph(url)
    if ogp.is_valid():
        return jsonify(ogp.to_json())
    return make_response(jsonify({ 'error' : 'Not Found' }), 404)
