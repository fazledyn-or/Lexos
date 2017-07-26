import re
import time
from flask import Flask
from jinja2 import evalcontextfilter
from markupsafe import Markup, escape
import lexos.helpers.constants

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['MAX_CONTENT_LENGTH'] = lexos.helpers.constants.MAX_FILE_SIZE
# open debugger when we are not on the server
app.debug = not lexos.helpers.constants.IS_SERVER
app.jinja_env.filters['type'] = type
app.jinja_env.filters['str'] = str
app.jinja_env.filters['tuple'] = tuple
app.jinja_env.filters['len'] = len
app.jinja_env.filters['unicode'] = str
app.jinja_env.filters['time'] = time.time()


def int_key(s):
    """
    Returns the key to sort by.

    Args:
        A key

    Returns:
        A key converted into an int if applicable
    """
    if isinstance(s, tuple):
        s = s[0]
    return tuple(int(part) if re.match(r'[0-9]+$', part) else part
                 for part in re.split(r'([0-9]+)', s))


@app.template_filter('natsort')
def natsort(l):
    """
    Sorts lists in human order (10 comes after 2, even when both are strings)

    Args:
        A list

    Returns:
        A sorted list
    """
    return sorted(l, key=int_key)


# http://flask.pocoo.org/snippets/28/
# http://stackoverflow.com/questions/12523725/
# why-is-this-jinja-nl2br-filter-escaping-brs-but-not-ps
@app.template_filter()  # Register template filter
@evalcontextfilter  # Add attribute to the evaluation time context filter
def nl2br(eval_ctx, value):
    """
    Wraps a string value in HTML <p> tags and replaces internal new line
    esacapes with <br/>. Since the result is a markup tag, the Markup()
    function temporarily disables Jinja2's autoescaping in the evaluation time
    context when it is returned to the template.
    """
    _paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
    result = '\n\n'.join('<p>%s</p>' % p.replace('\n', Markup('<br/>\n'))
                         for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


# this imports needs to be here
# since it depends on `app`.
import lexos.interfaces

if __name__ == '__main__':
    app.run()
