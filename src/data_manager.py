from database import connection_handler


@connection_handler
def save_agent(cursor, name, description, agent_image, background_image, role):
    query = """
        INSERT INTO agent(name, description, agent_image, background_image, role)
        VALUES (%(name)s, %(description)s, %(agent_image)s, %(background_image)s, %(role)s)
        RETURNING id;
        """
    cursor.execute(query, {
        'name': name,
        'description': description,
        'agent_image': agent_image,
        'background_image': background_image,
        'role': role
    })
    return cursor.fetchone()[0]


@connection_handler
def save_ability(cursor, name, description, image, agent_id):
    query = """
        INSERT INTO ability(name, description, image, agent_id)
        VALUES (%(name)s, %(description)s, %(image)s, %(agent_id)s)
        """
    cursor.execute(query, {
        'name': name,
        'description': description,
        'image': image,
        'agent_id': agent_id
    })


@connection_handler
def get_agents(cursor):
    query = """ 
        SELECT * FROM agent
        """
    cursor.execute(query)
    return cursor.fetchall()
