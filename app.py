# standard library
import threading
import webbrowser

from nicopaleis import create_app

app = create_app()


if __name__ == '__main__':
    url = 'http://localhost:5000/'
    threading.Timer(2.5, lambda: webbrowser.open(url, new=2)).start()
    app.run(debug=False)
