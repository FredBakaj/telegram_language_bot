import argparse
import os
from peewee import SqliteDatabase, PostgresqlDatabase
from peewee_migrate import Router


def main():
  parser = argparse.ArgumentParser(
    description='Database migration tool for Peewee ORM.')
  parser.add_argument('--database', required=True, help='Database URL.')
  parser.add_argument('--directory',
                      required=True,
                      help='Migration directory.')
  args = parser.parse_args()

  if args.database.startswith('sqlite://'):
    # SQLite database URL
    db = SqliteDatabase(
      "/home/runner/telegramlanguagebot/data/database.sqlite3")
  else:
    # Postgres database URL
    db = PostgresqlDatabase.from_url(args.database)

  router = Router(db)
  # router.create('migration_name')

  # Run migration/migrations
  router.run('migration_name')

  print('Migrations applied successfully.')


if __name__ == '__main__':
  main()
  # from pathlib import Path
  # DIR = Path(__file__).absolute().parent
  # print(DIR)
