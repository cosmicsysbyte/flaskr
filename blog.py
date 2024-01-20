from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__,)

@bp.route('/index')
@login_required
def index():
    db = get_db()
    
    return render_template('blog/index.html')

@bp.route('/addlink')
@login_required
def addlink():
    db = get_db()
    
    return render_template('blog/addlink.html')