from flask import send_from_directory, render_template, current_app
from . import main


@main.route('/')
def api():
    """ Route for API Docs welcome page """
    api_url = current_app.config['API_DOCS_URL']
    return render_template('welcome.html', doc_link=api_url)
