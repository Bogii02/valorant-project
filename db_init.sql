CREATE TABLE IF NOT EXISTS agent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    description VARCHAR(400),
    agent_image VARCHAR(255),
    background_image VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS ability (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(500),
    image VARCHAR(255),
    agent_id INTEGER,
    FOREIGN KEY (agent_id) REFERENCES agent(id)
);