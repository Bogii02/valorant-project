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
        VALUES (%(name)s, %(description)s, %(image)s, %(agent_name)s);
        """
    cursor.execute(query, {
        'name': name,
        'description': description,
        'image': image,
        'agent_name': agent_name
    })


@connection_handler
def save_weapon(cursor, name, image, category, empty_image):
    query = """
        INSERT INTO weapon(name, image, category, empty_image)
        VALUES (%(name)s, %(image)s, %(category)s, %(empty_image)s)
        RETURNING name;
        """
    cursor.execute(query, {
        'name': name,
        'image': image,
        'category': category,
        'empty_image': empty_image
    })
    return cursor.fetchone()[0]


@connection_handler
def save_skin(cursor, name, image, weapon_name):
    query = """
        INSERT INTO skin(name, image, weapon_name)
        VALUES (%(name)s, %(image)s, %(weapon_name)s);
        """
    cursor.execute(query, {
        'name': name,
        'image': image,
        'weapon_name': weapon_name
    })


@connection_handler
def save_map(cursor, name, image):
    query = """
        INSERT INTO map(name, image)
        VALUES (%(name)s, %(image)s);
    """
    cursor.execute(query, {
        'name': name,
        'image': image
    })


@connection_handler
def get_all_agents(cursor):
    query = """ 
        SELECT * FROM agent;
        """
    cursor.execute(query)
    return cursor.fetchall()


@connection_handler
def get_agent_by_name(cursor, agent_name):
    query = """
        SELECT * FROM agent
        WHERE name = %(agent_name)s;
        """
    cursor.execute(query, {
        'agent_name': agent_name
    })
    return cursor.fetchall()


@connection_handler
def get_abilities_by_agent(cursor, agent_name):
    query = """
        SELECT name, description, image
        FROM ability
        WHERE agent_name = %(agent_name)s;
        """
    cursor.execute(query, {
        'agent_name': agent_name
    })
    return cursor.fetchall()


@connection_handler
def get_agents_by_role(cursor, role):
    query = """
        SELECT * FROM agent
        WHERE role = %(role)s;
        """
    cursor.execute(query, {
        'role': role
    })
    return cursor.fetchall()


@connection_handler
def get_all_weapons(cursor):
    query = """
        SELECT * FROM weapon;
    """
    cursor.execute(query)
    return cursor.fetchall()


@connection_handler
def get_all_skins(cursor):
    query = """
        SELECT * FROM skin;
    """
    cursor.execute(query)
    return cursor.fetchall()


@connection_handler
def get_skins_by_weapon(cursor, weapon_name):
    query = """
        SELECT * FROM skin
        WHERE weapon_name = %(weapon_name)s;
    """
    cursor.execute(query, {
        'weapon_name': weapon_name
    })
    return cursor.fetchall()