#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  hzsunshx
# Created: 2015-01-27 15:52

"""
flask html editor support image upload
"""

import os
import json
import flask

UPLOAD_FOLDER = 'static/upload'
PORT = os.getenv('PORT') or '9999'

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.redirect('/static/demo.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print flask.request.files
    print flask.request.files.keys()
    file = flask.request.files['Filedata']
    print 'upload:', file.filename
    target_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(target_path)
    return json.dumps(dict(image_path='/'+target_path, success=True, message='Good'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT), debug=True)
