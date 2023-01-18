# input args
FROM_DATE = None
END_DATE = None

# Timeseries
TS_NAME = "varmelast_dk"
CONTAINER = "mcp-feed-varmelast-dk"
DESCRIPTION = "Denmark heat data from: https://www.varmelast.dk/"
TIMEZONE = "UTC"
TAGS = ["heat", "vermelast", "dk", "denmark"]
PRIMARY_KEYS = ["key", "created_at"]

# Other
ENDORSEMENT = "gold"
PROXIES = None
DATE_FORMAT = r"%Y-%m-%d"
ERRORS = []

# Logger
LOG_SEPARATOR = "-" * 65
LOG_LEVEL = "INFO"
LOG_FORMAT_STRING = "%(name)s %(asctime)s %(levelname)-8s %(processName)s [%(filename)s:%(lineno)d] %(message)s"
WARN_MSG_START = "\n---------------------------------- WARNING START ------------------------------------"
WARN_MSG_END = "\n----------------------------------- WARNING END -------------------------------------"
