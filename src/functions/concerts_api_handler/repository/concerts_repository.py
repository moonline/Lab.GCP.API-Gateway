from __future__ import annotations

import os
from datetime import datetime
from functools import reduce

import firebase_admin
from firebase_admin import firestore

from model.concert import Concert


firebase_admin.initialize_app()
firestore_client = firestore.client()


class ConcertsRepository:
    @staticmethod
    def to_record(concert: Concert) -> dict:
        return {
            'artist': concert.artist,
            'concert': concert.concert,
            'ticket_sales': concert.ticket_sales,
            'create_date': concert.create_date
        }

    def __init__(self) -> ConcertsRepository:
        """
        Example:
            os.environ['TABLE_NAME'] = 'concerts'

            from repository.concerts_repository import ConcertsRepository

            repository = ConcertsRepository()

        :return: A ConcertsRepository instance
        """
        self.collection_name = os.environ.get('COLLECTION_NAME')

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
                "create_date": "2023-09-08T14:47:29.915661"
            },
            {
                "artist": "Madonna",
                "concert": "In Time",
                "ticket_sales": 56565135,
                "create_date": "2021-06-06T15:57:39.915661"
            },
            {
                "artist": "DJ Bobo",
                "concert": "Freedom",
                "ticket_sales": 6688,
                "create_date": "2020-10-11T05:44:22.915661"
            },
            {
                "artist": "Sophie Ellis Bextor",
                "concert": "Murder on the dance floor",
                "ticket_sales": 45687974,
                "create_date": "2022-01-01T17:36:45.915661"
            }
        ]
        return [record for record in records if record['artist'] == artist]
    
        # documents = (
        #     firestore_client.collection(self.collection_name)
        #     .where(filter=FieldFilter("artist", "==", artist))
        #     .stream()
        # )
        # return [document.to_dict() for document in documents]


    def create_concert(self, concert: Concert) -> Concert:
        """
        Add a new concert to the database

        Example:
            repository = ConcertsRepository()
            concert = Concert(
                'Zoe',
                'French tales',
                80000
            )
            repository.add_concert(concert)

        :param Concert concert: A concert object to be persisted

        :return: The persisted concert
        """
        concert.create_date = datetime.now()
        record = self.to_record(concert)
        firestore_client.collection(self.collection_name).add(record)
        return concert
    



