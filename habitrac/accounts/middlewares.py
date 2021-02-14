import time

from django.conf import settings


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


class DelayResponseMiddleware:
    """This middleware will add a delay of `settings.DEBUG_RESPONSE_DELAY` before
    sending back the response to each request. Mostly used to test loading animations
    on the frontend client."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time.sleep(int(settings.DEBUG_RESPONSE_DELAY))
        response = self.get_response(request)
        return response
