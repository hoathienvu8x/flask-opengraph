import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from opengraph import app

if __name__ == '__main__':
    app.run(debug=True) # host = '0.0.0.0', port = 5000, debug = False
