import movies
import bottle


@bottle.route('/hello')
def hello():
    return "Hello World!"

bottle.run(host='localhost', port=8080, debug=True)