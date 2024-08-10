CREATE TABLE IF NOT EXISTS agent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    description VARCHAR(400),
    agent_image VARCHAR(255),
    background_image VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS ability (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    description VARCHAR(500),
    image VARCHAR(255),
    agent_name VARCHAR(20),
    FOREIGN KEY (agent_name) REFERENCES agent(name) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS weapon (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE ,
    image VARCHAR(128),
    empty_image VARCHAR(128),
    category VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS skin (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    image VARCHAR(255),
    weapon_name VARCHAR(50),
    FOREIGN KEY (weapon_name) REFERENCES weapon(name) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS map (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    image VARCHAR(128)
);