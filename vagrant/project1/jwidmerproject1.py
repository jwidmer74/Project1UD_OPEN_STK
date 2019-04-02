#! /usr/bin/env python3
import psycopg2

def main():
    """
    main function
    """
    print("1. What are the most popular three articles of all time?")
    get_popular_articles()
    print("2. Who are the most popular article authors of all time?")
    get_popular_authors()
    print("3. On which days did more than 1% of requests lead to errors?")
    get_error_requests()
def get_popular_articles():
    """
    Returns the most popular articles from the database
    """
    try:
        database = psycopg2.connect("dbname=news")
        conn = database.cursor()
        conn.execute("select * from populararticles")
        rows = conn.fetchall()
        for row in rows:
            print(" " + '"{}"'.format(row[0]) + " -- " + str(row[1]) + " views")
        print("\n")
        database.close()
    except psycopg2.OperationalError as error:
        print(error)
def get_popular_authors():
    """
    Returns the most popular authors from the database
    """
    try:
        database = psycopg2.connect("dbname=news")
        conn = database.cursor()
        conn.execute("select * from rankedauthors")
        rows = conn.fetchall()
        for row in rows:
            print(" *" + " " + row[0] + " -- " + str(row[1]) + " views")
        print("\n")
        database.close()
    except psycopg2.OperationalError as error:
        print(error)
def get_error_requests():
    """
    Returns the number of errors from the database
    """
    try:
        database = psycopg2.connect("dbname=news")
        conn = database.cursor()
        conn.execute("select day,percent from percents where percent > .02")
        rows = conn.fetchall()
        for row in rows:
            result = "{:.1%}".format(row[1])
            print(" *" + " " + str(row[0].strftime('%B %d, %Y')) + ' -- ' + result + " errors")
        print("\n")
        database.close()
    except psycopg2.OperationalError as error:
        print(error)
if __name__ == '__main__':
    main()
