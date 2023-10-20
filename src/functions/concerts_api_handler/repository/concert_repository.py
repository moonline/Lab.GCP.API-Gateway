from __future__ import annotations

import os
from datetime import datetime
from functools import reduce

import firebase_admin
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

from model.concert import Concert


firebase_admin.initialize_app()
firestore_client = firestore.client()


class ConcertRepository:
    @staticmethod
    def concert_to_document(concert: Concert) -> dict:
        return {
            'artist': concert.artist,
            'concert': concert.concert,
            'ticket_sales': concert.ticket_sales,
            'create_date': concert.create_date
        }

    @staticmethod
    def document_to_concert(record: dict) -> Concert:
        return Concert(**record)

    def __init__(self) -> ConcertRepository:
        """
        Example:
            os.environ['COLLECTION_NAME'] = 'concerts'

            from repository.concerts_repository import ConcertRepository

            repository = ConcertRepository()

        :return: A ConcertRepository instance
        :rtype: ConcertRepository
        """
        self.collection = firestore_client.collection(
            os.environ.get('COLLECTION_NAME')
        )

    def find_concerts_by_artist(self, artist: str) -> list[Concert]:
        """
        Finds all concerts that match the given artist

        Example:
            repository = ConcertRepository()
            repository.find_concerts_by_artist('Madonna')

        :param artist: An artist name
        :type artist: str

        :return: A list of concerts
        :rtype: list
        """
        concert_documents = (
            self.collection
                .where(filter=FieldFilter("artist", "==", artist))
                .stream()
        )
        return [
            self.document_to_concert(concert_document.to_dict())
            for concert_document in concert_documents
        ]

    def create_concert(self, concert: Concert) -> Concert:
        """
        Add a new concert to the database

        Example:
            repository = ConcertRepository()
            concert = Concert(
                'Zoe',
                'French tales',
                80000
            )
            repository.add_concert(concert)

        :param concert: A concert object to be persisted
        :type concert: Concert

        :return: The persisted concert
        :rtype: Concert
        """
        concert.create_date = datetime.now()
        record = self.concert_to_document(concert)
        # TODO check success
        self.collection.add(record)
        return concert
