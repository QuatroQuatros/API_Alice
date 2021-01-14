import requests
import json
import random
from flask_restful import Resource, reqparse



class RandomAnime(Resource):
	def get(self, img=0):
		randomNumber = random.randint(1,9000)
		req = requests.get(f"https://api.jikan.moe/v3/anime/{randomNumber}/")
		dc = json.loads(req.text)
		return dc


class Anime(Resource):
	def get(self, anime_name):
		req = requests.get(f"https://api.jikan.moe/v3/search/anime?q={anime_name}&genre=16&genre_exclude=0&limit=1")
		dc = json.loads(req.text)
		return dc
