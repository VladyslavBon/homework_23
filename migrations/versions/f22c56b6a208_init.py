"""Init

Revision ID: f22c56b6a208
Revises: 653c64216f34
Create Date: 2023-10-08 13:16:35.028397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f22c56b6a208'
down_revision: Union[str, None] = '653c64216f34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.alter_column('contacts', 'firstname',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('contacts', 'lastname',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=50),
               nullable=True)
    op.alter_column('contacts', 'birthdate',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.create_index(op.f('ix_contacts_birthdate'), 'contacts', ['birthdate'], unique=False)
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=True)
    op.create_index(op.f('ix_contacts_firstname'), 'contacts', ['firstname'], unique=False)
    op.create_index(op.f('ix_contacts_lastname'), 'contacts', ['lastname'], unique=False)
    op.create_index(op.f('ix_contacts_phone'), 'contacts', ['phone'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_phone'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_lastname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_firstname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_birthdate'), table_name='contacts')
    op.alter_column('contacts', 'birthdate',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    op.alter_column('contacts', 'email',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('contacts', 'lastname',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
    op.alter_column('contacts', 'firstname',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
    op.drop_column('contacts', 'updated_at')
    # ### end Alembic commands ###
