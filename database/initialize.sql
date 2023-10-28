-- Create players table
CREATE TABLE IF NOT EXISTS players (
    id_player SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    avatar TEXT,
    level INT DEFAULT 1,
    status VARCHAR(50),
    wins INT DEFAULT 0,
    loses INT DEFAULT 0,
    two_factor_auth BOOLEAN DEFAULT FALSE
);