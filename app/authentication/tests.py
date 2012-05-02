from django.utils import unittest
from Music.app.models import Track
from django.db import IntegrityError

class TrackTests(unittest.TestCase):
    def setUp(self):
        self.track1 = Track.objects.create(title="Space", artist="Something Corporate",
                album="Leaving Through the Window",
                albumartist="Leaving Through the Window")

    def testTrackDuplicates(self):
        self.assertRaises(IntegrityError, Track.objects.create, title="Space",
            artist="Something Corporate", album="Leaving Through the Window",
            albumartist="Leaving Through the Window")

