import os
from pathlib import Path
from flask import Flask, request, render_template


version = 'v2.1'


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
    )
    instance_path = Path(app.instance_path)
    print(instance_path)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=instance_path/'nicopaleis.sqlite',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    instance_path.mkdir(parents=True, exist_ok=True)


    @app.context_processor
    def inject_version():
        return dict(version=version)

    # a simple page that says hello
    @app.route('/')
    @app.route('/nicopaleis')
    def home():
        return render_template('home.html')

    @app.route('/shutdown')
    def shutdown():
        shutdown_server()
        return 'Server shutting down...'

    from nicopaleis import db
    db.init_app(app)

    from nicopaleis.blueprints import (
        parameters,
        snippets,
        layouts,
        messages,
        settings,
        xml,
        booklet,
        transfer,
    )
    app.register_blueprint(parameters.bp)
    app.register_blueprint(snippets.bp  )
    app.register_blueprint(layouts.bp   )
    app.register_blueprint(messages.bp  )
    app.register_blueprint(settings.bp  )
    app.register_blueprint(xml.bp       )
    app.register_blueprint(booklet.bp   )
    app.register_blueprint(transfer.bp  )

    return app
