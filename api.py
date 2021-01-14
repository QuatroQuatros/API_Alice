from flask import Flask
from flask_restful import Api
from resources.anime import RandomAnime, Anime


app = Flask(__name__)
api = Api(app)

api.add_resource(RandomAnime, '/random')
api.add_resource(Anime, '/anime/<string:anime_name>')

if __name__ == '__main__':
	app.run(debug=True)
