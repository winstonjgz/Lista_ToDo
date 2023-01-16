from flask import(
    Blueprint, flash, g, redirect, render_template, url_for
)

from werkzeug.exceptions import abort

from todo.auth import login_required

from todo.db import get_db

bp = Blueprint('todo', __name__)


@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
            'select t.id, t.description, u.username, t.completed, t.created_at from todo t JOIN user u on t.created_by = u.id order by created_at desc'
        )
    todos = c.fetchall()

    return render_template('todo/index.html', todos = todos)

    
@bp.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    return " "


@bp.route('/update', methods=['POST', 'GET'])
@login_required
def update():
    return " "