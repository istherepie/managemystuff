# -- coding: utf-8 --

import rethinkdb as r
from datastore import RethinkdbInterface


class DbHelper(RethinkdbInterface):

    def __init__(self):
        super().__init__()

    def bootstrap(self):
        status = self.check_if_instance_exists()

        if not status:
            self.setup_database()

        print("Initialized Mofo!")


    def check_if_instance_exists(self):
        """

        :return:
        """

        query = r.db_list()
        db_list = self.runner(query)

        if self.db_name not in db_list:
            return False

        return True

    def setup_database(self):
        """

        :return:
        """

        createdb = self.runner(
            r.db_create(self.db_name)
        )

        print(createdb)

        self.conn.use(self.db_name)

        tables = [
            "stuff",
            "more_stuff"
        ]

        for table in tables:
            create_table = self.runner(
                r.table_create(table)
            )

            print(create_table)


if __name__ == "__main__":
    db = DbHelper()
    db.bootstrap()