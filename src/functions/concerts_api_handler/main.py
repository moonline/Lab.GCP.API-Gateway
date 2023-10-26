import json
from flask import Flask, request, typing
import functions_framework

from controller.concert_controller import ConcertController
from repository.concert_repository import ConcertRepository


repository = ConcertRepository()
controller = ConcertController(repository)


app = Flask(__name__)


@app.route('/concerts', methods=['GET'])
def get_concerts() -> list[dict]:
    """
    Example:
        curl --location 'https://{API_GATEWAY_DOMAIN}/concerts?artist={ARTIST}'
        e.g.
        curl --location 'https://concerts-api-gateway-dev-5pksjh0d.nw.gateway.dev/concerts?artist=Madonna'

    :return: A list of concerts. Example:
        [
            {
                "artist": "Madonna",
                "concert": "This is Madonna 2023",
                "ticket_sales": 5000000,
                "create_date": "2023-09-08T14:47:29.915661"
            },
            ...
        ]
    :rtype: list
    """
    parameters: dict = request.args

    return controller.get_concerts_action(parameters, {})


@app.route('/concerts', methods=['PUT'])
def put_concert() -> dict:
    """
    Example:
        curl -X PUT --location '{API_GATEWAY_DOMAIN}/concerts' \
            -H 'Content-Type: application/json' \
            -d '{ ... }'
        e.g.
        curl -X PUT --location 'https://concerts-api-gateway-dev-5pksjh0d.nw.gateway.dev/concerts' \
            -H 'Content-Type: application/json' \
            -d '{"artist":"Madonna","concert":"This is Madonna 2023","ticket_sales": 5000000}'

    :return: The created concert. Example:
        {
            "artist": "Madonna",
            "concert": "This is Madonna 2023",
            "ticket_sales": 5000000,
            "create_date": "2023-09-08T14:47:29.915661"
        }
    :rtype: dict
    """
    # request.json returns Bad request and get_json(silent=True) returns None
    body: dict = json.loads(request.data) if bool(request.data) else None

    return controller.put_concert_action({}, body)


@functions_framework.http
def handler(http_request: request) -> typing.ResponseReturnValue:
    """
    Flask app router to dispatch requests.
    See https://medium.com/google-cloud/use-multiple-paths-in-cloud-functions-python-and-flask-fc6780e560d3

    :param http_request: An API Gateway request. Example:
        {
            "method": "GET",
            "scheme": "http",
            "server": ("0.0.0.0", 8080),
            "root_path": "",
            "path": "/",
            "query_string": b"artist=Madonna",
            "headers": EnvironHeaders(
                [
                    ("Host", "europe-west2-concerts-2023.cloudfunctions.net"),
                    ("Priority", "u=1"),
                    ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",),
                    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",),
                    # ...
                ]
            ),
            "remote_addr": "169.254.1.1",
            "environ": {
                # ...
                "REQUEST_METHOD": "GET",
                "QUERY_STRING": "artist=Madonna",
                "RAW_URI": "/?artist=Madonna",
                "SERVER_PROTOCOL": "HTTP/1.1",
                "HTTP_HOST": "europe-west2-concerts-2023.cloudfunctions.net",
                # ...
                "PATH_INFO": "/",
                "SCRIPT_NAME": "",
                "werkzeug.request": <Request 'http://europe-west2-concerts-2023.cloudfunctions.net/?artist=Madonna' [GET]>,
            },
            "shallow": False,
            "json_module": <flask.json.provider.DefaultJSONProvider object at 0x3e989de69850>,
            "url_rule": <Rule '/' -> run>,
            "view_args": {"path": ""},
            "host": "europe-west2-concerts-2023.cloudfunctions.net",
            "url": "http://europe-west2-concerts-2023.cloudfunctions.net/?artist=Madonna",
        }
    :type http_request: flask.request

    :return: Flask dispatch response
    :rtype: json
    """
    app_context = app.test_request_context(
        path=http_request.full_path,
        method=http_request.method
    )
    app_context.request.data = http_request.data
    app_context.request.headers = http_request.headers

    app_context.push()
    return_value = app.full_dispatch_request()
    app_context.pop()

    return return_value
