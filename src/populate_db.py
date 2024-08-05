import requests
import data_manager

AGENTS_URL = "https://valorant-api.com/v1/agents"
WEAPONS_URL = "https://valorant-api.com/v1/weapons"

agents = requests.get(AGENTS_URL).json()
weapons = requests.get(WEAPONS_URL).json()


def encode_agent_name_for_url(agent_name):
    return agent_name.replace('/', '').capitalize()


def get_agents():
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
            print(f"Error processing agent: {e}")
    return agents_data


def save_agents(agents_data):
    for agent_data in agents_data:
        name, description, role, agent_image, background_image, abilities = agent_data
        try:
            name = encode_agent_name_for_url(name)
            agent_name = data_manager.save_agent(name, description, agent_image, background_image, role)

            for ability_data in abilities:
                ability_name, ability_description, ability_image = ability_data
                data_manager.save_ability(ability_name, ability_description, ability_image, agent_name)

        except Exception as e:
            print(f"Error saving agent or abilities: {e}")


def get_weapons():
    weapons_data = []
    for weapon in weapons['data']:
        try:
            name = weapon['displayName']
            image = weapon['displayIcon']

            shop_data = weapon.get('shopData')
            if shop_data is None:
                category = 'Melee'
            else:
                category = shop_data.get('category')

            weapons_data.append((name, image, category))

        except Exception as e:
            print(f"Error processing weapon: {e}")
    return weapons_data


def save_weapons(weapons_data):
    for weapon_data in weapons_data:
        name, image, category = weapon_data
        try:
            weapon_id = data_manager.save_weapon(name, image, category)

        except Exception as e:
            print(f"Error saving weapon or skins: {e}")


save_weapons(get_weapons())
