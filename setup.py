from distutils.core import setup

setup(name = "Cloudflare DDNS",
    version = "1.0",
    description = "DDNS service for cloudflare",
    author = "Sylkos",
    packages = ["cloudflare", "requests", "python-dotenv"])