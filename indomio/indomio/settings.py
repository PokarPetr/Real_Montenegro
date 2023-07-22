# Scrapy settings for indomio project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "indomio"

SPIDER_MODULES = ["indomio.spiders"]
NEWSPIDER_MODULE = "indomio.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "indomio (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'propertySearchPreferences=eyJpdiI6ImZHSk52NjZ3dGxMVjNBRmc3UGdoQ2c9PSIsInZhbHVlIjoiRXNFZTFxb3h5ZUYxOTFvWGJiZmlyQnNEczVuaytXS29MZkxIOHpIbHIyRitBejltbmZLSHVwdmNLcEF0R2ZXNlRQdElOWVwvSmhcLzZXU1JjbVpLK1psdGtrT1Y1NkNxXC9mU0lxN0dBYWxBeXdKamVNM1BQb3YxSDNWWmE4bmlWeW0iLCJtYWMiOiI3ODkzNDY2ZDdmNmU3MGY2YTViNTYzNDA2MDExYzc0YTcwNzJmNDdjZTYzMzc0OTUzM2U2MjhjZGU2MmI3NzBjIn0^%^3D; currency=eyJpdiI6IkxEVVNDajR3WUo3QUJyVm5RbkZoSkE9PSIsInZhbHVlIjoibzN4VGQ3bnZiYmZuVFwveDNTSDJEZFBXVE5cLzQxeVE4TVhWMkJqejN5K2REaFBxXC8zNTU3U2VMeEhYa3JmenJBVXh3S2hXMFd5djEzY3ZxRnFRaHV2TTVhQ2xcL3RlaXpud3RseTFnSUkrUURnPSIsIm1hYyI6ImE2YjJlZTNlODY5YWFhZWY0YzZjZjc2ZDQyNzZmNTJiYWYzY2FlYzM5MGM5OTViN2JkMzE0NjhlNjQ1N2RiYzAifQ^%^3D^%^3D; _ga_QJBK7MGZ7Y=GS1.1.1690008920.26.1.1690012368.37.0.0; _ga=GA1.2.1779439527.1688834624; __qca=P0-1638739619-1688834620842; _fbp=fb.1.1688834627990.1842749429; _hjSessionUser_1349006=eyJpZCI6IjFmZWMxY2NlLWViYjItNTVlYS04OTljLWZhYTFkNjMwMjMxNCIsImNyZWF0ZWQiOjE2ODg4MzQ2MjgyMjcsImV4aXN0aW5nIjp0cnVlfQ==; _oid=6b7a11ad-4512-409a-b600-25c9b6f8d60e; _cc_id=80fc0e87127cd6cba1c28517e65462cc; reese84=3:kgGFXUhfiu3rQ7uXmFdohw==:otnVovSCXC+HTiCvsYc5C/dDEBoxiVZfRCPrVUfACpsLNvDprNAS/SeAge/KlXWSD8b+lgmFfgo2/vU9LlytAPEIoDJZXXUSJcu7NRaIVv/py3aot+Gnkq9L15eHRX5Vvbmy9WJB5npHzQQmVq4csl/oB28ymmjGq9PvQjH2CLwAlkGFLC5ist91lJ2763Elir7eiz5eln3CCy7VBgjGkhG1/l/QhH5+tbyV9IJdc2XgyNznWR6yRora7iPZJsT2nOm1rQg4Hvyb0Eoq8xVrhUIYac2TzWHUIqZllN5ek0cTXfhGI702ZT7MO2ygLOAEvmib+HYvo2oV6TxB+2J6iHato039lJmRCVAqr+q1Y9xbBkWUNZbuV6fktU/1goNbtJDZYSwF+f1UMCw8WcbOzkj36Zh6BWhoxfT9M4wAIBpFFWCclXJTip+m8ctC/NNX4wFjOEKL+Xd8aoZAJ9bx/8Z0mM7dntser4fhkcnOcVj/z/vihFfkX9pCBcsqYvzL:JKXznXS3JLqZrc8TJQ7yNsZGWrQUhPzWpA5aqIEEXFQ=; _pbjs_userid_consent_data=6683316680106290; cto_bundle=KUBV_F8waXNuY2cwUWVMTmtQdzdlMVUxUzNweGhobkFPaDBTVEpjVVdLSTBIQkZmVXYzRDFWSG40eUxWSlRwd2NXV01ZRlBLZ2cyMmI4OEZ3aXBJUVBqUHFIeUFoMyUyRmdNdkxNWUslMkJnMjN3YTRHVHM4SGt0bDUwVHZibmJZTU56JTJGUjNqVUhGd1dOcVJXdEdOeHhaakh4N1g0bmclM0QlM0Q; cto_bidid=avU7UV9ZelZnbE1hVlRhb3lqWk9mS0NUVEp6TE1FWmpVQXROTng1QkNUcmFjOGN5M1VjOGg5eTJZQ3Q1V0ZMNnV3V21TT0VNaWRGRDNDOFduMGpUek1BUUdzVmdqTGpnZ3IyYjl4TGhNSldoZW4wVSUzRA; cto_dna_bundle=SupnvV8waXNuY2cwUWVMTmtQdzdlMVUxUzNuJTJGYmFuT08zUjQ5NEE3JTJGUlpDYWFTblNZQjUwJTJGM1M4WGplZmJZaHJzcHdIM2RMMUolMkJLbVc0ZVQ4QXQlMkZRMG1FZ3clM0QlM0Q; __gads=ID=22929856d79b0786:T=1688834909:RT=1690011773:S=ALNI_MZ_v5vRJeV0-GpKXCs7xeZ2Uz3GFA; __gpi=UID=00000c6572d11917:T=1688834909:RT=1690011773:S=ALNI_MZ1TigDvHGRqUEV6H_2_kHzjRtxLw; _gid=GA1.2.1907128062.1689406209; panoramaId_expiry=1690034579768; XSRF-TOKEN=eyJpdiI6IlR0YVdFb0xIT05iek5vdzNXNVwvZ0JRPT0iLCJ2YWx1ZSI6InJnSnNlUFBtTmIybjhLUFRNZ29GemtHTnR4bnI3VHFcL0tVa2pjaFM0dUdUK2hacE1zVmdFb05KZnQ5MndcLytZTzZDM1g3ZnhoTzJcLzdacHJwdU9oOUZBPT0iLCJtYWMiOiIyMGFkMmYxOTQ1Y2NhZDU2ZjZmNDZkMDhlMzA3YjU2YzY2YTQ4NDc2Zjg1YmQ2ZjgzODVmYjcxMDJmZmYxZWIxIn0^%^3D; laravel_session=eyJpdiI6IkQ5SWwzTUtRTUhCVTk5TnI4amx0bVE9PSIsInZhbHVlIjoiQVJmTTNDRkN6Y2dCcCs1cTVjTW9WbUFIR2s1YWJUZjVabk96Y2tCU21mVlBjYkRQZG1TanFFQ05DWFMwOTl0amxuMXlxdjdVUTlweXdtYTJYWHlmOWc9PSIsIm1hYyI6ImQ5OGQwN2MzMzAyYjhmMGY2ZWE5NzUyMTBiNTllNzgyMzA1Y2U3YTA4MjZkMTMxOTcwZGYyYWZjZDQwOGU4ODMifQ^%^3D^%^3D; _hjIncludedInSessionSample_1349006=0; _hjSession_1349006=eyJpZCI6ImIzOWJkNjRkLWFlNjctNDM0NS05NGYwLTA5Y2ZmMjJlZDY0MSIsImNyZWF0ZWQiOjE2OTAwMDg5MjEwNTEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-126591797-1=1; XSRF-TOKEN=eyJpdiI6Im1XQllCbis5Mm92QUw0dlE0QjFacUE9PSIsInZhbHVlIjoidVpoc2U4TTZoNTR6cklQUmttZXNvcTB0eFZlYjA5UDNESjlkeTdyWXZjMjBQc2Z3clFGaHFaU0NsUlF6ZlwveUxMRWo5dVJKWjFURFpzbXNQVTVYSTN3PT0iLCJtYWMiOiJkYjBjMDcyODBmYWM3Y2NiYmNhZDlkMDkxMGU5MGExYjg1MDk1NWQ2Yjg1ZWU5ZGJhZmU2NDI3MTY2NTViNDBhIn0%3D; currency=eyJpdiI6IithUEV3UXVYalJoYk9cL293VW5keG5BPT0iLCJ2YWx1ZSI6IkJja0R0WEpLS05EQ1poXC9ZQzJmVzArTDVcL1dqZjRJUlFyRXl1cGY3Z29pTkVFalZYN3JKSUI3dVBTMVN5RmZEamRFMFR6cHBuVHhuVE5TXC9cL3RJUEI3VklIcTIyOHpneklyZXk2RGJGbEE3Yz0iLCJtYWMiOiI2MjA1YmM4NjU3ZTdhNTI3YTdmODZiZjQzYTkzMDIyZGM1NzVmZWMwZDliMDcyYWRhNWQ2ZGQwOTMxM2VmYWM4In0%3D; laravel_session=eyJpdiI6IkE1OGp6dWJUZWRvckdoKzN1RDJ2RHc9PSIsInZhbHVlIjoiVlwvVW5XT1l1Tk9BU2thOHZqOFRMdFNVVjRzQWY1RWRqQ1R2MUpLYXNlK1kzcU82OFN1V01pSFFpTUZaT0hjRWhLQVplSEhYcjg0Nm1hckhDYXExZmxBPT0iLCJtYWMiOiI5ZmNjZmY5NTkyOTNmM2E5Y2Q1MDg0MTMxMTQyMzQ4NDcxM2IwODIzMDM2OTNjNTNmMjI2NzYwMzJlZmQxZjI4In0%3D; propertySearchPreferences=eyJpdiI6IkR2QjQ4Y2phWW1mN2NSVmV3dFIrTXc9PSIsInZhbHVlIjoiTUpEUUFhV0V1TjN1XC9ENlwva1daTzlrdXQyR3ZzT2pCSEdHQW41ZjhNMCtodHBzM2kyM2x0ZUM0aEo5dERNWjJwZ0xcL1RXSlwvOFkyaEwxMkUwa2FPYTZlbFVSYXRUSU1DMVFWVlV1OFZ2SHBtTUVBdjZmYWVBQmpnVHJONDNGZzV2IiwibWFjIjoiZjBmMDUwOGZkMGVjZWFhOTdkYTg0NTRiMTlhYzlkMmM2MDU2MTIwMmQxYWE4ZmE1ZjE1OTAzODJiYjVkNWQyNSJ9',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'trailers'
        }
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "indomio.middlewares.IndomioSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "indomio.middlewares.IndomioDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "indomio.pipelines.IndomioPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
