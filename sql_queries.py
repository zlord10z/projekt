def sql_query(number):
    sql_query= open("sqlqueries.txt", "r")
    sql_query = sql_query.read()
    sql_query = sql_query.split("$")
    for i in range(len(sql_query)):
        sql_query[i] = sql_query[i].replace('\n', '')
    return sql_query[number]


