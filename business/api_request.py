import json
import textwrap

import allure
import requests

from logger import Logger


class APIRequest:
    logger = Logger.setup_logger(__name__)

    def __init__(self, waiting_time = None, global_debug=True):
        self._session = requests.Session()
        self.waiting_time = waiting_time
        self.global_debug = global_debug

    @allure.step("[{method}] {url}")
    def _send_request(self, method: str, url: str, debug=None, **kwargs):

        acceptable_waiting_time = kwargs.pop(
            'waiting_time', None) or self.waiting_time

        if debug is None:
            debug = self.global_debug  # Use the global setting if debug is not specified

        # Ensure that globalDebug always overrides individual debug settings
        debug = self.global_debug if self.global_debug else debug

        try:
            response = self._session.request(method, url, **kwargs)
            duration = response.elapsed.total_seconds()
            assert duration <= acceptable_waiting_time, (
                f"Response Time > {acceptable_waiting_time}s, Cost: {duration}s")
            if debug:
                self._debug_print(response=response)
        except requests.exceptions.RequestException as e:
            response = None
            if debug:
                print(textwrap.dedent('''
                    ---------------- response ----------------
                    Request Error
                    {method} {url}
                    Kwargs: {kwargsstr}
                    Error : {e}
                    Response: {response}
                    ''').format(
                    method=method,
                    url=url,
                    e=str(e),
                    kwargsstr=f"{kwargs}",
                    resp=response
                ))

        return response

    def _debug_print(self, response: requests.Response):
        request_body = response.request.body
        if request_body:
            request_body = json.loads(request_body)

        try:
            response_body = json.dumps(
                response.json(), indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            response_body = response.text or f"{response.status_code} {response.reason}"

        format_header = lambda x_item: '\n'.join(
            f'{k}: {v}' for k, v in x_item.items())

        self.logger.debug(textwrap.dedent('''
                    ---------------- request ----------------
                    {req.method} {req.url}
                    {request_header}
                    Request Body :
                    {request_body}
                    ---------------- response ----------------
                    {resp.status_code} {resp.reason} {resp.url}
                    {resp_header}
                    Duration : {resp_duration}
                    Response Context :
                    {response_body}
                    ''').format(
            req=response.request,
            request_body=json.dumps(
                request_body, indent=4, ensure_ascii=False),
            resp=response,
            response_body=response_body,
            resp_duration=response.elapsed.total_seconds(),
            request_header=format_header(response.request.headers),
            resp_header=format_header(response.headers),
        ))
