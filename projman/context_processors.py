from .core.models import Company

def get_company(request):
	print(Company.load())
	print("hui")
	return {
		"company" : Company.load()
	}