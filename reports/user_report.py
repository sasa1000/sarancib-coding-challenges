class UserReport:
  def __init__(self, database_cursor):
    self.cur = database_cursor

  def displaycol(self,tablename):
    self.cur.execute("select * from "+tablename)
    return self.cur.fetchall()

  def avgcompletedtime(self):
    self.cur.execute("SELECT cast((avg(cast(( JulianDay(A.CompletedDate) - JulianDay(B.publishedAt) ) As Integer )) /30) As Integer)from certificates A inner INNER JOIN courses B on A.course = B.id")
    return self.cur.fetchone()[0]

  def avgspentime(self):
    self.cur.execute("SELECT CAST(avg(cast(( JulianDay(CompletedDate) - JulianDay(startDate) ) As Integer )) As Integer)from certificates")
    return self.cur.fetchone()[0]

  def avgspentimePerCourse(self):
    self.cur.execute("SELECT  B.title cource_name , CAST(avg(cast(( JulianDay(A.CompletedDate) - JulianDay(A.startDate) ) As Integer )) As Integer ) average_timespent from certificates A INNER JOIN courses B on  A.course= B.id GROUP BY  B.title ")
    return self.cur.fetchall()

  def fastusers(self):
    self.cur.execute(" SELECT  F.fastestusers FROM (  SELECT A.email fastestusers , avg(cast(( JulianDay(CompletedDate) - JulianDay(startDate) ) As Integer )) timespent from  users A INNER JOIN certificates B on A.id= B.user GROUP BY user  order by timespent ASC ) F ")
    return self.cur.fetchall()

  def slowestusers(self):
    self.cur.execute(" SELECT S.slowestusers FROM ( SELECT A.email slowestusers , avg(cast(( JulianDay(CompletedDate) - JulianDay(startDate) ) As Integer )) timespent from  users A INNER JOIN certificates B on A.id= B.user GROUP BY user  order by timespent  DESC ) S")
    return self.cur.fetchall()

  def NbrCertifUser(self):
    self.cur.execute(" SELECT  A.email,  COUNT(B.user) from users A INNER JOIN certificates B ON A.id= B.user GROUP BY A.email")
    return self.cur.fetchall()



