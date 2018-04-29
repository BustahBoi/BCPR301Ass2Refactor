from interpreter.database_remote import DBRemote
from unittest import TestCase


# Wesley
class TestRemote(TestCase):
    # Wesley
    def setUp(self):
        self.db = DBRemote()
        self.db.connect("localhost", "root", "", "test")
        self.maxDiff = None
        self.db.create_table()

    # Wesley
    def tearDown(self):
        self.db.drop_table()
        self.db.close()
        self.db = None

    # Wesley
    def test_db_insert_values(self):
        """Create a table, insert data and check the return data is what was inserted"""
        expected = [(1, b'dskjhflkasdjlfkj23543'), (2, b'dskjhflkasdjlasdfdsafkj23543')]
        self.db.insert_record("dskjhflkasdjlfkj23543")
        self.db.insert_record("dskjhflkasdjlasdfdsafkj23543")
        self.db.commit()
        result = self.db.get_db()
        self.assertEqual(expected, result)

    # def test_empty_db(self):
    #     expected = list()

    def test_db_get(self):
        """Getting an empty database"""
        expected = list()
        result = self.db.get_db()
        self.assertEqual(expected, result)

    def test_db_insert_dict(self):
        """Insert a dictionary into the database"""
        expected = [(1, b'dskjhflkasdjlfkj23543'), (2, b'dskjhflkasdjlasdfdsafkj23543')]
        data = {1: 'dskjhflkasdjlfkj23543', 2: "dskjhflkasdjlasdfdsafkj23543"}
        self.db.insert_dictionary(data)
        result = self.db.get_db()
        # print(result)
        self.assertEqual(expected, result)

    def test_db_update(self):
        """Insert a dictionary into the database"""
        expected = [(1, b'dskjhflkasdjlfkj23543'), (2, b'changed')]
        data = {1: 'dskjhflkasdjlfkj23543', 2: "dskjhflkasdjlasdfdsafkj23543"}
        self.db.insert_dictionary(data)
        self.db.update_record(2, "changed")
        result = self.db.get_db()
        self.assertEqual(expected, result)

    def test_db_delete(self):
        """Insert a dictionary into the database"""
        expected = [(1, b'dskjhflkasdjlfkj23543')]
        data = {1: 'dskjhflkasdjlfkj23543', 2: "dskjhflkasdjlasdfdsafkj23543"}
        self.db.insert_dictionary(data)
        self.db.delete_record("2")
        result = self.db.get_db()
        self.assertEqual(expected, result)




