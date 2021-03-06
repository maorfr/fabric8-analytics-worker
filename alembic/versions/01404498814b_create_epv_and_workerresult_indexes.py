"""Create EPV and WorkerResult indexes.

Revision ID: 01404498814b
Revises: d62464ca17ae
Create Date: 2017-05-22 07:49:50.619646

"""

# revision identifiers, used by Alembic.
revision = '01404498814b'
down_revision = 'd62464ca17ae'
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_ecosystems_url'), 'ecosystems', ['url'], unique=False)
    op.create_index(op.f('ix_packages_name'), 'packages', ['name'], unique=False)
    op.create_index(op.f('ix_versions_identifier'), 'versions', ['identifier'], unique=False)
    op.create_index(op.f('ix_worker_results_worker'), 'worker_results', ['worker'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_worker_results_worker'), table_name='worker_results')
    op.drop_index(op.f('ix_versions_identifier'), table_name='versions')
    op.drop_index(op.f('ix_packages_name'), table_name='packages')
    op.drop_index(op.f('ix_ecosystems_url'), table_name='ecosystems')
    # ### end Alembic commands ###
