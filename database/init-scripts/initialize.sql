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

-- Create chatroom table
CREATE TABLE IF NOT EXISTS chatroom (
    id_chatroom SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    isPublic BOOLEAN DEFAULT TRUE,
    password TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create message table
CREATE TABLE IF NOT EXISTS message (
    id_message SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    player_id INT REFERENCES players(id_player)
);

-- Create game_history table
CREATE TABLE IF NOT EXISTS game_history (
    id_gamehistory SERIAL PRIMARY KEY,
    mode VARCHAR(50),
    winner INT REFERENCES players(id_player),
    winner_score INT,
    loser INT REFERENCES players(id_player),
    loser_score INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create relation table
CREATE TABLE IF NOT EXISTS relation (
    id_relation SERIAL PRIMARY KEY,
    relationStatus VARCHAR(50),
    sender INT REFERENCES players(id_player),
    receiver INT REFERENCES players(id_player)
);

-- Create membership table
CREATE TABLE IF NOT EXISTS membership (
    id_membership SERIAL PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50),
    isBanned BOOLEAN DEFAULT FALSE,
    isMuted BOOLEAN DEFAULT FALSE,
    player_id INT REFERENCES players(id_player),
    chatroom_id INT REFERENCES chatroom(id_chatroom)
);