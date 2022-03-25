from urllib.parse import urljoin


class HoneygainAPIEndpoints:
    def __init__(self, protocol: str = "https", domain: str = "dashboard.honeygain.com", prefix: str = "api", version: str = "v1") -> None:
        self.base_url = f"{protocol}://{domain}/{prefix}/{version}"