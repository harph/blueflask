from flask import Blueprint, Flask
import importlib
import os
import sys


BP_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'blueprints'
)
# Add blueprints to the path
sys.path.insert(0, BP_PATH)


def _get_blueprint_module(pkg_name, module_name):
    try:
        return importlib.import_module(
            '.' + module_name,
            package=pkg_name
        )
    except ImportError:
        # TODO add logging here
        return None


def _load_blueprints(app):
    for pkg_name in os.listdir(BP_PATH):
        pkg_path = os.path.join(BP_PATH, pkg_name)
        if os.path.isdir(pkg_path):
            config_module = _get_blueprint_module(pkg_name, 'config')
            urls_module = _get_blueprint_module(pkg_name, 'urls')

            blueprint_init = getattr(config_module, 'BLUEPRINT_INIT', {})
            bp = Blueprint(pkg_name, pkg_name, **blueprint_init)

            for route in getattr(urls_module, 'ROUTES', []):
                bp.add_url_rule(**route)

            app.register_blueprint(bp)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    _load_blueprints(app)
    return app


app = create_app()
