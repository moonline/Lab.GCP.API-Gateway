from __future__ import annotations

import os
from datetime import datetime
from functools import reduce

from model.concert import Concert


class ConcertsRepository:
    def __init__(self) -> ConcertsRepository:
        """
        Example:
            os.environ['TABLE_NAME'] = 'concerts'

            from repository.concerts_repository import ConcertsRepository

            repository = ConcertsRepository()

        :return: A ConcertsRepository instance
        """
        # TODO
        self.table_name = os.environ.get('TABLE_NAME')

    def find_concerts_by_artist(self, artist: str) -> list[dict]:
        """
        Finds all concerts that match the given artist

        Example:
            repository = ConcertsRepository()
            repository.find_concerts_by_artist('Madonna')

        :param string artist: An artist name

        :return: A list of concerts
        """
        records = [
            {
                "artist": "Madonna",
                "concert": "This is Madonna 2023",
                "ticket_sales": 5000000,
                "created_date": "2023-09-08T14:47:29.915661"
            },
            {
                "artist": "Madonna",
                "concert": "In Time",
                "ticket_sales": 56565135,
                "created_date": "2021-06-06T15:57:39.915661"
            },
            {
                "artist": "DJ Bobo",
                "concert": "Freedom",
                "ticket_sales": 6688,
                "created_date": "2020-10-11T05:44:22.915661"
            },
            {
                "artist": "Sophie Ellis Bextor",
                "concert": "Murder on the dance floor",
                "ticket_sales": 45687974,
                "created_date": "2022-01-01T17:36:45.915661"
            }
        ]
        return [record for record in records if record['artist'] == artist]


    def create_concert(self, concert: Concert) -> Concert:
        """
        Add a new concert to the DB

        Example:
            repository = ConcertsRepository()
            repository.add_concert({
                'artist': 'Zoe',
                'concert': 'French tales',
                'ticket_sales': 80000
            })

        :param Concert concert: A concert object to be persisted

        :return: The persisted concert
        """
        record = {
            **concert,
            'created_date': datetime.now().isoformat()
        }
        return record
