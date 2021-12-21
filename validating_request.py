from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

videos_put_args = reqparse.RequestParser()
videos_put_args.add_argument("name", type=str, help="Invalid name!", required=True)
videos_put_args.add_argument("views", type=int, help="Invalid views!", required=True)
videos_put_args.add_argument("likes", type=int, help="Invalid likes!", required=True)

videos = {}

def video_check(video_id):
    if video_id not in videos:
        abort(404, "Could not find the video...")

class Video(Resource):
    def get(self, video_id):
        video_check(video_id)
        return videos[video_id]
    def put(self, video_id):
        args = videos_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
