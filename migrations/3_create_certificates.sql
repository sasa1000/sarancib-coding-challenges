CREATE TABLE IF NOT EXISTS certificates (
  course TEXT NOT NULL REFERENCES courses(id),
  'user' TEXT NOT NULL REFERENCES users(id),
  completedDate DATETIME NOT NULL,
  startDate DATETIME NOT NULL,
  PRIMARY KEY(course,'user')

 );


