CREATE TABLE IF NOT EXISTS courses (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL ,
  description TEXT,
  publishedAt DATETIME NOT NULL
 );
