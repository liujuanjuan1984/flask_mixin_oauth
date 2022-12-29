import os

import config_private as PVT

MIXIN_CLIENT_ID = PVT.MIXIN_CLIENT_ID
MIXIN_CLIENT_SECRET = PVT.MIXIN_CLIENT_SECRET


MIXIN_BASEURL = "https://api.mixin.one/"
MIXIN_AUTH_TOKEN_URL = "https://api.mixin.one/oauth/token"

# scope = "PROFILE:READ"
# scope = 'PROFILE:READ+PHONE:READ+CONTACTS:READ+ASSETS:READ'
# scope = "PROFILE:READ+PHONE:READ+CONTACTS:READ+ASSETS:READ+COLLECTIBLES:READ"

scope = "PROFILE:READ+COLLECTIBLES:READ"

MIXIN_AUTH_URL = "".join(
    [
        "https://mixin.one/oauth/authorize?client_id=",
        MIXIN_CLIENT_ID,
        "&scope=",
        scope,
        "&response_type=code&return_to=",
    ]
)
