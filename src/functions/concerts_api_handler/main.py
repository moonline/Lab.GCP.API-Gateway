import flask

import functions_framework

from controller.concerts_controller import ConcertsController
from repository.concerts_repository import ConcertsRepository


repository = ConcertsRepository()
controller = ConcertsController(repository)


@functions_framework.http
def get_concerts(request: flask.request) -> flask.typing.ResponseReturnValue:
    """
    Example:
        curl --location 'TODO.../concerts?artist=Madonna'
        e.g.
        curl --location 'TODO.../concerts?artist=Madonna'

    :return: A list of concerts. Example:
        [
            {
                "artist": "Madonna",
                "concert": "This is Madonna 2023",
                "ticket_sales": 5000000,
                "created_date": "2023-09-08T14:47:29.915661"
            },
            ...
        ]
    """
    parameters: dict = request.args

    return controller.get_concerts_action(parameters, {})


@functions_framework.http
def put_concert(request: flask.request) -> flask.typing.ResponseReturnValue:
    """
    Example:
        curl --location 'TODO.../concerts' \
            -H 'Content-Type: application/json' \
            -d '{ ... }'
        e.g.
        curl -X PUT --location 'TODO.../concerts' \
            -H 'Content-Type: application/json' \
            -d '{"artist":"Madonna","concert":"This is Madonna 2023","ticket_sales": 5000000}'

    :return: The created concert. Example:
        {
            "artist": "Madonna",
            "concert": "This is Madonna 2023",
            "ticket_sales": 5000000,
            "created_date": "2023-09-08T14:47:29.915661"
        }
    """
    body: dict = request.json

    return controller.put_concert_action({}, body)