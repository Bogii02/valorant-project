import requests
import data_manager

AGENTS_URL = "https://valorant-api.com/v1/agents"
WEAPONS_URL = "https://valorant-api.com/v1/weapons"
MAPS_URL = "https://valorant-api.com/v1/maps"


def encode_agent_name_for_url(agent_name):
    return agent_name.replace('/', '').capitalize()


def get_agents():
    agents = requests.get(AGENTS_URL).json()
    agents_data = []
    for agent in agents['data']:
        try:
            if agent['isPlayableCharacter']:
                name = agent['displayName']
                description = agent['description']
                agent_image = agent['fullPortraitV2']
                background_image = agent['background']
                role = agent['role']['displayName']

                abilities = []
                for ability in agent.get('abilities', []):
                    if ability['displayIcon'] is not None:
                        ability_name = ability['displayName']
                        ability_description = ability['description']
                        ability_image = ability['displayIcon']
                        abilities.append((ability_name, ability_description, ability_image))

                agents_data.append((name, description, role, agent_image, background_image, abilities))

        except Exception as e:
            print(f"Error processing agent or ability: {e}")
    return agents_data


def save_agents(agents_data):
    for agent_data in agents_data:
        name, description, role, agent_image, background_image, abilities = agent_data
        try:
            name = encode_agent_name_for_url(name)
            agent_name = data_manager.save_agent(name, description, agent_image, background_image, role)

            for ability in abilities:
                ability_name, ability_description, ability_image = ability
                data_manager.save_ability(ability_name, ability_description, ability_image, agent_name)

        except Exception as e:
            print(f"Error saving agent or ability: {e}")


def get_weapons():
    weapons = requests.get(WEAPONS_URL).json()
    weapons_data = []
    for weapon in weapons['data']:
        try:
            name = weapon['displayName']
            image = weapon['displayIcon']
            empty_image = weapon['killStreamIcon']

            shop_data = weapon.get('shopData')
            if shop_data is None:
                category = 'Melee'
            else:
                category = shop_data.get('category')

            skins = []
            for skin in weapon['skins']:
                if skin['displayName'] != "Random Favorite Skin" and "Standard" not in skin['displayName']:
                    skin_name = skin['displayName']
                    if skin['displayIcon'] is None:
                        skin_image = empty_image
                    else:
                        skin_image = skin['displayIcon']

                    skins.append((skin_name, skin_image))

            weapons_data.append((name, image, category, empty_image, skins))

        except Exception as e:
            print(f"Error processing weapon or skin: {e}")
    return weapons_data


def save_weapons(weapons_data):
    for weapon_data in weapons_data:
        name, image, category, empty_image, skins = weapon_data
        try:
            weapon_name = data_manager.save_weapon(name, image, category, empty_image)

            for skin in skins:
                skin_name, skin_image = skin
                data_manager.save_skin(skin_name, skin_image, weapon_name)

        except Exception as e:
            print(f"Error saving weapon or skin: {e}")


def get_maps():
    maps = requests.get(MAPS_URL).json()
    maps_data = []
    for map in maps['data']:
        try:
            name = map['displayName'],
            image = map['splash']

            maps_data.append((name, image))

        except Exception as e:
            print(f"Error processing map: {e}")
    return maps_data


def save_maps(maps_data):
    saved_maps = set()

    for map_data in maps_data:
        name, image = map_data
        if name not in saved_maps:
            try:
                data_manager.save_map(name, image)
                saved_maps.add(name)

            except Exception as e:
                print(f"Error saving map: {e}")
