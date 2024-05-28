from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.models import db, Post, Comment

#Парсер данных о постах
post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help='Title is required')
post_parser.add_argument('content', type=str, required=True, help='Content is required')

#Парсер данных о комментариях
comment_parser = reqparse.RequestParser()
comment_parser.add_argument('post_id', type=int, required=True, help='Post ID is required')
comment_parser.add_argument('author_name', type=str, required=True, help='Author name is required')
comment_parser.add_argument('comment_text', type=str, required=True, help='Comment text is required')

class PostResource(Resource):
    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        post = Post(title=args['title'], content=args['content'])
        db.session.add(post)
        db.session.commit()
        return {'message': 'Post created', 'post': post.id}, 201

    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return {'title': post.title, 'content': post.content, 'published_date': post.published_date}

    @jwt_required()
    def put(self, post_id):
        post = Post.query.get_or_404(post_id)
        args = post_parser.parse_args()
        post.title = args['title']
        post.content = args['content']
        db.session.commit()
        return {'message': 'Post updated'}

    @jwt_required()
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {'message': 'Post deleted'}

class CommentResource(Resource):
    @jwt_required()
    def post(self):
        args = comment_parser.parse_args()
        comment = Comment(post_id=args['post_id'], author_name=args['author_name'], comment_text=args['comment_text'])
        db.session.add(comment)
        db.session.commit()
        return {'message': 'Comment created', 'comment': comment.id}, 201

    def get(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        return {'post_id': comment.post_id, 'author_name': comment.author_name, 'comment_text': comment.comment_text, 'created_date': comment.created_date}

    @jwt_required()
    def put(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        args = comment_parser.parse_args()
        comment.author_name = args['author_name']
        comment.comment_text = args['comment_text']
        db.session.commit()
        return {'message': 'Comment updated'}

    @jwt_required()
    def delete(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return {'message': 'Comment deleted'}
