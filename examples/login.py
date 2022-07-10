import restfly

from pycheckpoint_api.firewallManagement import FirewallManagementAPI
import logging

# Setup the logger configuration. If you have any trouble, turn the logging mode to logging.DEBUG
logging.basicConfig(
    filename="pycheckpoint_api-example-login.log",
    encoding="utf-8",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# GLOBAL VARIABLE
HOSTNAME = ""
PORT = 443
API_KEY = ""
VERSION = "1.8"
DOMAIN = ""

# Initialize the API
api = None

try:
    # Please note that, as it's an example, we enabled the SSL verify to False to avoid having SSL certificate issues.
    # However, it's highly recommanded to use certificates with know certificate authorities.
    logger.info("Trying to login to the API...")

    with FirewallManagementAPI(
        hostname=HOSTNAME,
        port=PORT,
        api_key=API_KEY,
        version=VERSION,
        domain=DOMAIN,
        ssl_verify=False,
    ) as api:

        logger.info(
            "Connection is successfull, we have a token: "
            + api._session.headers["X-chkp-sid"]
        )
        logger.info("Trying to logout from the API...")

    logger.info("Logout is successfull")
except restfly.errors.BadRequestError as e:
    print(e)
    for p in dir(e.response.request):
        print(p, getattr(e.response.request, p))
