from requests import get

class TronaldDump:
	def __init__(self) -> None:
		self.api = "https://api.tronalddump.io"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
		}
	
	def get_tag_by_value(self, value: str) -> dict:
		return get(
			f"{self.api}/tag/{value}",
			headers=self.headers).json()
	
	def get_all_tags(self) -> dict:
		return get(
			f"{self.api}/tag",
			headers=self.headers).json()
	
	def get_quotes_by_id(self, quote_id: str) -> dict:
		return get(
			f"{self.api}/quote-source/{quote_id}",
			headers=self.headers).json()
	
	def get_author_by_id(self, author_id: str) -> dict:
		return get(
			f"{self.api}/author/{author_id}",
			headers=self.headers).json()
	
	def search_quote(
			self,
			query: str,
			page: int) -> dict:
		return get(
			f"{self.api}/search/quote?query={query}&page={page}",
			headers=self.headers).json()
	
	def get_quote_by_id(self, quote_id: str) -> dict:
		return get(
			f"{self.api}/quote/{quote_id}",
			headers=self.headers).json()
	
	def get_random_meme(self) -> dict:
		return get(
			f"{self.api}/random/meme",
			headers=self.headers).json()
	
	def get_random_quote(self) -> dict:
		return get(
			f"{self.api}/random/quote",
			headers=self.headers).json()
