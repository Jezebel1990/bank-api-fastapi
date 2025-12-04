from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from src.config import settings
from src.database import metadata

# IMPORTANTE: importe seus modelos para o autogenerate funcionar
from src.models.transaction import transactions  # noqa
from src.models.account import accounts  # noqa

# Carrega config do Alembic
config = context.config

# ============================================================
# 🔥 CORREÇÃO CRÍTICA:
# Alembic NÃO funciona com URLs async.
# Então removemos "+aiosqlite" da URL utilizada SOMENTE nas migrations.
# ============================================================
sync_url = settings.database_url.replace("+aiosqlite", "")

# Substitui a URL do alembic.ini pela versão síncrona
config.set_main_option("sqlalchemy.url", sync_url)

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadados para autogenerate funcionar
target_metadata = metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=sync_url,  # usa URL síncrona aqui também
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    # Engine síncrono, obrigatório para Alembic
    connectable = engine_from_config(
        {**config.get_section(config.config_ini_section), "sqlalchemy.url": sync_url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Escolhe modo online/offline
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()