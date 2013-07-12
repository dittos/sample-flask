import datetime
import flask
from bbs import db, models

def init_app(app):
    app.register_blueprint(board)

    # The trailing parenthesises make the filter name
    # same with the function name (`static`).
    @app.template_filter()
    def static(filename):
        # We don't use `url_for('static')` directly.
        # It's hard to override the default URL generation.
        # Sometimes you will need to change the host to CDN, for example.
        # TODO: consider static files per blueprint.
        return flask.url_for('static', filename=filename)

board = flask.Blueprint('board', __name__)

@board.route('/')
def index():
    page = flask.request.args.get('page', default=1, type=int)
    posts = models.Post.query.order_by(models.Post.id.desc())
    paging = posts.paginate(page)
    return flask.render_template('list.html', paging=paging)

@board.route('/posts/new')
def write():
    return flask.render_template('write.html')

@board.route('/posts/new', methods=['POST'])
def write_save():
    # TODO: use library for validation (WTForms or FormEncode)
    form = flask.request.form
    post = models.Post()
    post.author_name = form['author_name']
    post.title = form['title']
    post.body = form['body']

    db.session.add(post)
    db.session.commit()

    # `post.id` has been populated after the flush.
    # (`commit` implies `flush`)
    rv = flask.redirect(flask.url_for('.show', id=post.id))

    # Make sure that `rv` is a `flask.Request` instance.
    rv = flask.make_response(rv)
    # Set the name cookie
    age = datetime.timedelta(days=30).total_seconds()
    rv.set_cookie('author_name', post.author_name, max_age=age)

    return rv

@board.route('/posts/<int:id>')
def show(id):
    post = models.Post.query.get_or_404(id)
    return flask.render_template('show.html', post=post)

@board.app_template_filter()
def post_body(post):
    return post.body
