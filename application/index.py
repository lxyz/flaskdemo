__author__ = 'adamli'
import json
from flask import render_template, session, redirect, request, abort
from application import app
from application.models import *

@app.route('/')
@app.route('/<category>')
def indexpage(category=''):
    return render_template('index.html', category = category)

@app.route('/pic/<int:id>')
def info(id):
    subimgs = SubImage.query.filter_by(image_id=id).all()
    subimages = []
    for sub in subimgs:
        subimages.append(sub.as_dict())
    if not subimgs:
        abort(404)
    return render_template('pic.html',  imglist = subimages)


@app.route('/api/autoload')
def autoload():
    page = int(request.args.get('page', 1, type=int))
    page_size = int(request.args.get('page_size', 10, type=int))
    c = request.args.get('c', '')
    if c:
        imageList = Image.query.filter_by(category=c).paginate(page, page_size, False).items
    else:
        imageList = Image.query.paginate(page, page_size, False).items
    imgs = []
    for img in imageList:
        imgs.append(img.as_dict())
    del imageList
    return json.dumps(imgs)