#! /usr/bin/env python

import psycopg2

DBNAME = "news"

# Define queries based on the following requests.

# Request_1. What are the most popular three articles of all time ?

query_1 = (""" SELECT
    title,
    count (*) as views
    FROM
    articles ar,
    log lg
    WHERE
    ar.slug = substring(lg.path, 10)
    GROUP BY
    title
    ORDER BY
    views DESC LIMIT 3;""")

# Request_2. Who are the most popular article athors of all time ?

query_2 = (""" SELECT
    au.name,
    COUNT(*) AS views
    FROM
    authors au
    JOIN
    articles art
    ON au.id = art.author
    JOIN
    log lg
    ON lg.path = CONCAT('/article/', art.slug)
    GROUP BY
    au.name
    ORDER BY
    views DESC;""")

# Request_3. On which days did more than 1% of requests lead to errors?

query_3 = (""" SELECT
    sum.date,
    ROUND(((100.0*er.error_requests) / sum.requests), 3) AS error
    FROM
    (
    SELECT
    date_trunc('day', time) "date",
    count(*) AS error_requests
    FROM
    log lg
    WHERE
    status >= '400'
    GROUP BY
    date
    )
    AS er
    JOIN
    (
    SELECT
    date_trunc('day', time) "date",
    count(*) AS requests
    FROM
    log lg
    GROUP BY
    date
    )
    AS sum
    ON sum.date = er.date
    WHERE
    (
    ROUND(((100.0*er.error_requests) / sum.requests), 3) > 1
    )
    ORDER BY
    error DESC;""")

# Connect to the Database "news" to execute queries


def define_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()

# Print results


def print_result_query_1(query):
    result = define_query(query)
    print('\n1. The most popular three articles of all time are:\n')
    for res in result:
        print '  ' + res[0] + ' with', res[1], 'views'


def print_result_query_2(query):
    result = define_query(query)
    print('\n2. The most popular article authors of all time are:\n')
    for res in result:
        print '  ' + res[0] + ' with', res[1], 'views.'


def print_result_query_3(query):
    result = define_query(query)
    print('\n3. Days with more than 1% of requests lead to errors are:\n')
    for res in result:
        date = res[0].strftime('%d %b %Y')
        print '  ' + date + ' ' + str(res[1]) + '% of requests lead to errors.'

print_result_query_1(query_1)
print_result_query_2(query_2)
print_result_query_3(query_3)
