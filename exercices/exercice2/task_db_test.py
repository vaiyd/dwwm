import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from task_db import Base, create_task, get_task_from_id

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.engine =create_engine('sqlite:///:memory:')
        self.session = Session(bind=self.engine)
        Base.metadata.create_all(self.engine)
                          
    def test_create_get_task(self):
        create_task(session=self.session, title="title1", description="dc1")
        task = get_task_from_id(session=self.session, id=1)

        self.assertIsNotNone(task)
        self.assertEqual(task.title, "title1")
        self.assertEqual(task.description, "dc1")

if __name__ == '__main__':
    unittest.main()