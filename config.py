from main import token_yan
URL = "https://cloud-api.yandex.net/v1/disk/resources"
Headers = {
    "Authorization": f"OAuth {token_yan}"
}
Params = {
   "path": "/1"
}