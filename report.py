import database
import reports.user_report

connection = database.get_connection()
cur = connection.cursor()
# Use the SQL queries to build the Analysis report
user_report = reports.user_report.UserReport(cur)
avgcompletedtime = user_report.avgcompletedtime()
avgspentime = user_report.avgspentime()
avgspentimePerCourse = user_report.avgspentimePerCourse()
fastestusers = user_report.fastusers()
slowestusers = user_report.slowestusers()
NbrCertifUser = user_report.NbrCertifUser()

print(f'The average  complete time of a course is {avgcompletedtime} months')
print(f'The average amount of users time spent in a course is {avgspentime} days')
print("The average amount of users time spent per course :")
print("\n")
for row in avgspentimePerCourse:
            print("Course name: ", row[0])
            print("Average time spent in days: ", row[1])
            print("\n")
print("fastest users versus slowest users :")
for f,s in zip(fastestusers,slowestusers):
            print(f[0]+" versus "+s[0])
            print("\n")
print(f' The amount of certificates per customer ')
for row in NbrCertifUser:
            print("Email: ", row[0])
            print("amount of certificates: ", row[1])
            print("\n")


