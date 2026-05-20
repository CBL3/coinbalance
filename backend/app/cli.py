import click
from flask.cli import with_appcontext
from flask_migrate import upgrade

from app.modules.identity.seed_fase1 import run_seed


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Executa as migrations (Alembic) e popula o banco de dados com a fundação (Seed)."""
    click.echo("==> LÓGICA: Aplicando migrations do banco configurado...")
    upgrade()
    click.echo("==> LÓGICA: Migrations aplicadas com sucesso.")
    
    click.echo("==> RETÓRICA: Materializando dados fundacionais (Seed)...")
    run_seed()
    click.echo("==> GRAMÁTICA: Ambiente unificado e inicializado com sucesso.")
