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


class ConcertsRepository:
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

    def __init__(self) -> ConcertsRepository:
        """
        Example:
            os.environ['TABLE_NAME'] = 'concerts'

            from repository.concerts_repository import ConcertsRepository

            repository = ConcertsRepository()

        :return: A ConcertsRepository instance
        """
        collection_name = os.environ.get('COLLECTION_NAME')
        self.collection = firestore_client.collection(collection_name)

    def find_concerts_by_artist(self, artist: str) -> list[dict]:
        """
        Finds all concerts that match the given artist

        Example:
            repository = ConcertsRepository()
            repository.find_concerts_by_artist('Madonna')

        :param string artist: An artist name

        :return: A list of concerts
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
        record = self.concert_to_document(concert)
        self.collection.add(record)
        return concert
