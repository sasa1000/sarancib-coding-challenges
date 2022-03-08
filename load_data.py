# Please add code here to fetch data from APIs into SQLite database
import requests
import requests
import json
import database
import reports.user_report


def ReadFromApi(baseurl,tablename):
    # Fetching data from API
    response_API = requests.get(baseurl+tablename)
    data = response_API.text
    parse_json = json.loads(data)
    return (parse_json)

def LoadIntoDB(parse_json,tablename,connection):
    cur = connection.cursor()
    value = []
    user_report = reports.user_report.UserReport(cur)
    # Get column names of a table
    user_report.displaycol(tablename)
    columns = list(map(lambda x: x[0], cur.description))
    # Generate variables for a table
    Gvariables = '?'
    Gvariables = Gvariables + ",?" * (len(columns) - 1)

    for record in parse_json:
            for i in columns:
               # Get values for each record

                value.append(dict(record).get(i))

            # Generate the insert query and apply it

            sql = 'INSERT OR IGNORE INTO ' + tablename + '(' + ','.join(columns) + ') VALUES(' + Gvariables + ')'
            cur.execute(sql, tuple(value))
            connection.commit()
            value.clear()
    print('data added')

def parseandload(connection):
    # Combine the previous functions and make use of them for albums and todos
    baseurl='https://raw.githubusercontent.com/perseusEngineering/candidate-coding-challenges/master/data-engineer/'
    print('add users data...')
    parse_json = ReadFromApi(baseurl, 'users.json')
    LoadIntoDB(parse_json, 'users', connection)
    print('add courses data...')
    parse_json = ReadFromApi(baseurl, 'courses.json')
    LoadIntoDB(parse_json, 'courses', connection)
    print('add courses data...')
    parse_json = ReadFromApi(baseurl, 'courses.json')
    LoadIntoDB(parse_json, 'courses', connection)
    print('add certificates data...')
    parse_json = ReadFromApi(baseurl, 'certificates.json')
    LoadIntoDB(parse_json, 'certificates', connection)


if __name__ == '__main__':
    connection = database.get_connection()
    parseandload(connection)