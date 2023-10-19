from __future__ import annotations

from datetime import datetime


class Concert:
    @staticmethod
    def validate(dto: dict) -> None:
        artist = dto.get('artist')
        assert bool(artist) and len(artist) > 2, 'artist must have minimal 2 characters'

        concert = dto.get('concert')
        assert bool(concert) and len(concert) > 2, 'concert must have minimal 2 characters'

        ticket_sales = dto.get('ticket_sales')
        assert ticket_sales >= 0, 'ticket_sales must be a positive amount'

    @classmethod
    def from_dto(cls, dto: dict) -> Concert:
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
        return {
            'artist': self.artist,
            'concert': self.concert,
            'ticket_sales': self.ticket_sales,
            'create_date': self.create_date.isoformat()
        }
