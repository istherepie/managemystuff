# -- coding: utf-8 --

import rethinkdb as r


class RethinkdbInterface(object):
    """
    INTERFACE
    """

    def __init__(self, db=r, db_name="stuff"):
        self.db_name = db_name
        self.conn = r.connect(db=db_name)

    def table(self, table_name):
        """

        :param table_name:
        :return:
        """
        return r.table(table_name)

    def all(self, table_name):
        """

        :param table_name:
        :return:
        """
        query = self.table(table_name)
        result = self.runner(query)
        return list(result)

    def get(self, table_name, identifier):
        """

        :param table_name:
        :param identifier:
        :return:
        """

        identifier = str(identifier)

        query = self.table(table_name).get(identifier)
        return self.runner(query)

    def filter(self, table_name, **filter_opts):
        """

        :param table_name:
        :param filter_opts:
        :return:
        """
        query = self.table(table_name).filter(filter_opts)
        return self.runner(query)

    def insert(self, table_name, data):
        """

        :param table:
        :return:
        """

        if not isinstance(data, dict):
            raise TypeError("Gimme a dict you douche!")

        query = self.table(table_name).insert(data)

        return self.runner(query)

    def delete(self, table_name, identifier):

        identifier = str(identifier)

        stuff = self.table(table_name).get(identifier)

        delete = self.runner(
            stuff.delete()
        )

        return delete

    def runner(self, query):
        """

        :param query:
        :return:
        """
        return query.run(self.conn)
