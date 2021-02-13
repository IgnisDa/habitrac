import time


class StatsMiddleware:
    """This middleware will add a header to the response to tell how much time
    was spent on the page generation in milliseconds."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)
        response["Debug-Authorization"] = request.headers.get("Authorization", None)

        duration = time.time() - start_time

        # Add the header for monitoring metric of page generation times
        response["X-Page-Generation-Duration-ms"] = int(duration * 1000)
        return response
