from .core.models import Company

def get_company(request):
	return {
		"company" : Company.load()
	}