from peewee_migrate import Router
from peewee import SqliteDatabase

db = "/home/runner/telegramlanguagebot/data/database.sqlite3"
router = Router(SqliteDatabase(db))

# # Create migration
# router.create('migration_name')

# Run migration/migrations
router.run('002_Init.py')