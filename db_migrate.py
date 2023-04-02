from peewee_migrate import Router
from peewee import SqliteDatabase

router = Router(SqliteDatabase('sqlite:///data/database.sqlite3'))

# Create migration
router.create('migration_name')

# Run migration/migrations
router.run('migration_name')

# Run all unapplied migrations
# router.run()