from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskapp.auth import login_required
from flaskapp.db import get_db

bp = Blueprint('blog', __name__,)

@bp.route('/index')
@login_required
def index():
    db = get_db()
    
    return render_template('blog/index.html')