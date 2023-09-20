from settings import SiteSettings
from site_API.utils.site_api_handler import SiteAPIInterface

site = SiteSettings()

headers = {
	"X-RapidAPI-Key": site.api_key.get_secret_value(),
	"X-RapidAPI-Host": site.host_api
}

url = "https://" + site.host_api

params = {"fragment":"true","json":"true"}

site_api = SiteAPIInterface()

if __name__ == '__main__':
    site_api()
