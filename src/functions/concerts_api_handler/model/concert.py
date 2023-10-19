from __future__ import annotations

from datetime import datetime


class Concert:
    @staticmethod
    def validate(dto: dict) -> None:
        """
        Validate a concert data transfer object

        Example:
            dto = {
                "artist": "Madonna",
                "concert": "This is Madonna 2023",
                "ticket_sales": 5000000,
                "create_date": "2023-09-08T14:47:29.915661"
            }
            Concert.validate(dto)

        :param dict dto:                Must be DEFINED
        :param str dto.artist:          Must be DEFINED
        :param str dto.concert:         Must be DEFINED
        :param int dto.ticket_sales:    Must be DEFINED

        :return: A new concert

        :raises AssertionError: In case of invalid properties
        """
        assert bool(dto), 'concert DTO should not be empty'

        artist = dto.get('artist')
        assert bool(artist) and len(artist) > 2, 'artist must have minimal 2 characters'

        concert = dto.get('concert')
        assert bool(concert) and len(concert) > 2, 'concert must have minimal 2 characters'

        ticket_sales = dto.get('ticket_sales')
        assert bool(ticket_sales) and ticket_sales >= 0, 'ticket_sales must be a positive amount'

    @classmethod
    def from_dto(cls, dto: dict) -> Concert:
        """
        Create a concert from a data transfer object (dict)

        Example:
            dto = {
                "artist": "Madonna",
                "concert": "This is Madonna 2023",
                "ticket_sales": 5000000,
                "create_date": "2023-09-08T14:47:29.915661"
            }
            concert = Concert.from_dto(dto)

        :param dict dto: A concert DTO (dict)

        :return: A new concert

        :raises AssertionError: In case of invalid properties
        """
        cls.validate(dto)

        return cls(
            dto['artist'],
            dto['concert'],
            dto['ticket_sales'],
            datetime.fromisoformat(dto['create_date']) if dto.get('create_date') else None
        )

    def __init__(self, artist: str, concert: str, ticket_sales: int, create_date: datetime) -> None:
        self.artist = artist
        self.concert = concert
        self.ticket_sales = ticket_sales
        self.create_date = create_date

    @property
    def dto(self) -> dict:
        """
        :return: The Concert as data transfer object (dict). Example:
            {
                "artist": "Madonna",
                "concert": "This is Madonna 2023",
                "ticket_sales": 5000000,
                "create_date": "2023-09-08T14:47:29.915661"
            }
        """
        return {
            'artist': self.artist,
            'concert': self.concert,
            'ticket_sales': self.ticket_sales,
            'create_date': self.create_date.isoformat()
        }
