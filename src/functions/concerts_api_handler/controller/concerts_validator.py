def validate_get_concerts_event(event: dict) -> None:
    """
    Validates a GET concerts Lambda event

    Example:
        self.validate_get_concerts_event(
            { "artist": "Madonna" }
        )

    :param dict event:          Must be DEFINED
    :param str event.artist:    Must be DEFINED

    :raises AssertionError: In case of invalid properties
    """
    assert bool(event), 'event empty'

    expected_parameters = set(['artist'])
    unexpected_parameters = expected_parameters.symmetric_difference(
        set(event.keys())
    )
    assert len(unexpected_parameters) == 0, \
        f'Unexpected event parameters: {",".join(unexpected_parameters)}. Expected only: {",".join(expected_parameters)}'


def validate_put_concert_event(event: dict) -> None:
    """
    Validates a PUT concert Lambda event

    Example:
        self.validate_get_concerts_event({
            "artist": "Madonna",
            "concert": "This is Madonna 2023",
            "ticket_sales": 5000000
        })

    :param dict event:              Must be DEFINED
    :param str event.artist:        Must be DEFINED
    :param str event.concert:       Must be DEFINED
    :param int event.ticket_sales:  Must be DEFINED

    :raises AssertionError: In case of invalid properties
    """
    assert bool(event), 'event empty'

    expected_parameters = set(['artist', 'concert', 'ticket_sales'])
    unexpected_parameters = expected_parameters.symmetric_difference(
        set(event.keys())
    )
    assert len(unexpected_parameters) == 0, \
        f'Unexpected or missing event parameters: {",".join(unexpected_parameters)}. Expected only: {",".join(expected_parameters)}'
