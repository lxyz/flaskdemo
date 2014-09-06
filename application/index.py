__author__ = 'adamli'
import json
from flask import render_template, session, redirect, request, abort
from application import app
from application.models import *

@app.route('/')
@app.route('/<category>')
def indexpage(category=''):
    return render_template('index.html', category = category)

@app.route('/pic/<id>')
def info(id):
    subimgs = SubImage.query.filter_by(image_id=id).all()
    subimages = []
    for sub in subimgs:
        subimages.append(sub.as_dict())
    if not subimgs:
        abort(404)
    return render_template('pic.html', jsonstr = json.dumps(subimages))


@app.route('/api/autoload')
def autoload():
    try:
        page = int(request.args.get('page'))
        page_size = int(request.args.get('page_size'))
        c = request.args.get('c')
    except:
        page = 1
        page_size = 4
    if c:
        imageList = Image.query.filter_by(category=c).paginate(page, page_size, False).items
    else:
        imageList = Image.query.paginate(page, page_size, False).items
    imgs = []
    for img in imageList:
        imgs.append(img.as_dict())
    del imageList
    return json.dumps(imgs)