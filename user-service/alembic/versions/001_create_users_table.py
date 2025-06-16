"""create users table

Revision ID: 001
Revises: 
Create Date: 2023-07-13 14:00:18.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create users table with enum type
    op.execute("""
    DO $$ BEGIN
        CREATE TYPE userrole AS ENUM ('admin', 'customer', 'seller');
    EXCEPTION
        WHEN duplicate_object THEN null;
    END $$;
    
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        hashed_password VARCHAR(255) NOT NULL,
        full_name VARCHAR(100) NOT NULL,
        phone VARCHAR(20),
        role userrole NOT NULL DEFAULT 'customer',
        is_active BOOLEAN NOT NULL DEFAULT true,
        is_verified BOOLEAN NOT NULL DEFAULT false,
        created_at TIMESTAMP NOT NULL DEFAULT now(),
        updated_at TIMESTAMP NOT NULL DEFAULT now(),
        last_login TIMESTAMP
    );
    
    CREATE UNIQUE INDEX ix_users_email ON users(email);
    CREATE UNIQUE INDEX ix_users_phone ON users(phone);
    """)

def downgrade() -> None:
    op.execute("""
    DROP TABLE users;
    DROP TYPE userrole;
    """)
