from flask import Blueprint
import pybo.naverapi as nv
from flask import request

bp = Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/blog')
def blog():
    key = request.args.get('keyword')
    result = nv.naver_blog(key)
    return {'result' : result}
