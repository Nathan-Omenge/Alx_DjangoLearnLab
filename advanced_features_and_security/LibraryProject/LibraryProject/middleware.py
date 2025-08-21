class SimpleCSPMiddleware:
    """
    Minimal CSP – allows only same-origin assets. Extend as needed.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resp = self.get_response(request)
        resp.headers["Content-Security-Policy"] = "default-src 'self'"
        return resp