import unittest
from models.record_label import RecordLabel

class TestRecordLabel(unittest.TestCase):

    def setUp(self):
        self.record_label = RecordLabel("Castleface Records", "San Francisco")

    def test_record_label_has_name(self):
        self.assertEqual("Castleface Records", self.record_label.name)

    def test_record_label_has_location(self):
        self.assertEqual("San Francisco", self.record_label.location)