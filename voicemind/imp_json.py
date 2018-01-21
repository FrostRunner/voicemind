#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-


class SQLExecuteError(Exception):
    pass


def sql_connection(method):
    def f(self, *args, **kwargs):
        with self.conn as connection:
            result = method(self, connection, connection.cursor(), *args, **kwargs)
        return result

    return f


class SQLManager:
    def __init__(self, database_path, shell=None):
        self.db_path = database_path
        if shell:
            self.remote_sql = shell.get_remote_module("sqlite3")
            self.conn = self.remote_sql.connect(self.db_path)
        else:
            self.conn = sqlite3.connect(self.db_path)

    @sql_connection
    def get_all_data(self, connection, cursor):
        # cursor.execute('SELECT * FROM Property')
        cursor.execute('SELECT * FROM movie_app_movie')
        return cursor.fetchall()

    @sql_connection
    def insert_row(self, connection, cursor, table, keys, values):
        formated_values = ["'" + str(x).strip("\'").strip("\"").replace("\'", "\"") + "'" for x in values]
        try:

            cursor.execute("INSERT INTO {} ({}) VALUES ({})".format(table, ", ".join(keys),
                                                                    ", ".join(formated_values)))
            if not connection.total_changes:
                raise SQLExecuteError("Database not changed")
            connection.commit()
        except Exception:
            raise Exception(keys, values)

    @sql_connection
    def update_row(self, connection, cursor, table, key, value, filter_key, filter_value):
        formated_value = "'" + str(value).strip("\'").strip("\"") + "'"
        formated_filter_value = "'" + str(filter_value).strip("\'").strip("\"") + "'"
        cursor.execute(
            "UPDATE {} set {} = {} where {}={}".format(table, key, formated_value, filter_key,
                                                       formated_filter_value))
        if not connection.total_changes:
            raise SQLExecuteError("Database not changed")
        connection.commit()

    @sql_connection
    def delete_row(self, connection, cursor, table, key, value):
        formated_value = "'" + str(value).strip("\'").strip("\"") + "'"
        cursor.execute("DELETE from {} where {}={}".format(table, key, formated_value))
        if not connection.total_changes:
            raise SQLExecuteError("Database not changed")
        connection.commit()

    @sql_connection
    def is_key_exist(self, connection, cursor, table, key, value):
        response = cursor.execute("SELECT {} from {}".format(key, table))
        for row in response:
            if value in row:
                return True
        return False


import json
import sqlite3

def import_data_from_json():
    sql = SQLManager("/Users/FrostRunner/github_rep/voicemind/db.sqlite3")

    with open("/Users/FrostRunner/Downloads/movies_foreign.json", "r", encoding="utf-8") as f:
        root = json.load(f)
        report = root["report"]
        movies = report["movies"]
        movies_keys = []
        for item in movies:
            for block_key, block_value in item["block"].items():
                item[block_key] = block_value
            item.pop("block", None)
            item["poster"] = "movie/default/poster/default.png"
            item["trailer"] = "/media/movie/default/trailer/default.mp4"

            keys = []
            values = []
            for x, y in item.items():
                keys.append(x)
                values.append(y)
            sql.insert_row("movie_app_movie", keys, values)

    print(sql.get_all_data())

import_data_from_json()