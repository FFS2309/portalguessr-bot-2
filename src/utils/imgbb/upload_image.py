import os

from hooks.aiohttp.make_request import make_request
from const import IMGBB_SERVER_URL

IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")


async def upload_image(url, name):
    params = {"key": IMGBB_API_KEY}
    data = {"image": (name, url)}
    response = await make_request(IMGBB_SERVER_URL, "POST", data=data, params=params)

    return response["data"]["url"]
