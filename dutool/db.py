#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql


class DBUtil:
    def __init__(self, config):
        self.username = config.get("username")
        self.password = config.get("password")
        self.host = config.get("host")
        self.port = int(config.get("port"))
        self.database = config.get("database")

    def conn(self):
        self.db = pymysql.connect(user=self.username, passwd=self.password, host=self.host, port=self.port, database=self.database)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def queryone(self, sql, args=None):
        self.conn()
        self.cursor.execute(sql, args)
        res = self.cursor.fetchone()
        self.close()
        return res

    def query(self, sql, args=None):
        self.conn()
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        self.close()
        return res

    def show(self, sql, args=None):
        self.conn()
        self.cursor.execute(sql, args)
        rows = self.cursor.fetchall()
        self.close()
        for row in rows:
            print(row)

    def __execute(self, sql, args):
        self.conn()
        count = self.cursor.execute(sql, args)
        self.db.commit()
        self.close()
        return count

    def insert(self, sql, args=None):
        return self.__execute(sql, args)

    def update(self, sql, args=None):
        return self.__execute(sql, args)

    def delete(self, sql, args=None):
        return self.__execute(sql, args)

    def execute(self, sql, args=None):
        self.conn()
        self.cursor.execute(sql, args)
        self.db.commit()
        self.close()

    def execute_list(self, sql_list):
        self.conn()
        for sql in sql_list:
            self.cursor.execute(sql)
        self.db.commit()
        self.close()
