import views


ROUTES = (
    # url routes are defined using dictionaries that match
    # add_url_rule parameters.
    # http://flask.pocoo.org/docs/0.11/api/
    # rule, endpoint=None, view_func=None, **options
    {
        'rule': '/', 'endpoint': 'index', 'view_func': views.demo,
        'methods': ['GET', 'POST']
    },
    # Example of a URL using class-based-view
    {'rule': '/about/', 'view_func': views.About.as_view('about')},
)
