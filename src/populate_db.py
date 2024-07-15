import requests
import data_manager

AGENT_URL = "https://valorant-api.com/v1/agents"

response = requests.get(AGENT_URL)
data = response.json()


def encode_agent_name_for_url(agent_name):
    return agent_name.replace('/', '').capitalize()


def get_agents():
    agents_data = []
    for agent in data['data']:
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
