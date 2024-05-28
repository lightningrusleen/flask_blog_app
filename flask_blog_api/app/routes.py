# from flask import Blueprint
# from flask_restful import Api
# from .resources import PostResource, CommentResource

# bp = Blueprint('api', __name__)
# api = Api(bp)


# api.add_resource(PostResource, '/posts', '/posts/<int:post_id>')
# api.add_resource(CommentResource, '/comments', '/comments/<int:comment_id>')

from flask import Blueprint
from flask_restful import Api
from .resources import PostResource, CommentResource

bp = Blueprint('api', __name__)
api = Api(bp)

api.add_resource(PostResource, '/posts', '/posts/<int:post_id>')
api.add_resource(CommentResource, '/comments', '/comments/<int:comment_id>')

