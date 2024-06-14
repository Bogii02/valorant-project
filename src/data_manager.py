from database import connection_handler


@connection_handler
def save_agent(cursor, name, description, agent_image, background_image, role):
    query = """
        INSERT INTO agent(name, description, agent_image, background_image, role)
        VALUES (%(name)s, %(description)s, %(agent_image)s, %(background_image)s, %(role)s)
        RETURNING name;
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
def save_ability(cursor, name, description, image, agent_name):
    query = """
        INSERT INTO ability(name, description, image, agent_name)
        VALUES (%(name)s, %(description)s, %(image)s, %(agent_name)s)
        """
    cursor.execute(query, {
        'name': name,
        'description': description,
        'image': image,
        'agent_name': agent_name
    })


@connection_handler
def get_all_agents(cursor):
    query = """ 
        SELECT * FROM agent
        """
    cursor.execute(query)
    return cursor.fetchall()


@connection_handler
def get_one_agent(cursor, agent_name):
    query = """
        SELECT * FROM agent
        WHERE agent_name = %(agent_name)s
        """
    cursor.execute(query, {
        'agent_name': agent_name
    })
    return cursor.fetchall


@connection_handler
def get_abilities_by_agent(cursor, agent_name):
    query = """
        SELECT name, description, image
        FROM ability
        WHERE agent_name = %(agent_name)s
        """
    cursor.execute(query, {'agent_name': agent_name})
    return cursor.fetchall()
