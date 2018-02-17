from . import antibiogram as abg

@abg.route('/')
def index():
    return '<h1>Antibiogram Page</h1>'