<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />

<!-- ABOUT THE PROJECT -->

## About The Project

<h3>I created this project for people who want to explore detailed profiles of all agents, showcasing their unique abilities and backgrounds in an interactive format.</h3>
<h3>Users can look through all the agents and all their abilities with pictures and descriptions. Currently, you can search for agents by their name, later on by role too.</h3>

### Built With

The following technologies were used during the project:

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![Postgresql][Postgres]][Postgres-url]
* [![Docker][Docker]][Docker-url]


<!-- GETTING STARTED -->

## Getting Started

### Installation

To get started with my Valorant project, follow these steps:

1. Clone the repository.
   ```sh
   git clone git@github.com:Bogii02/valorant-project.git
   ```
2. Change directory to valorant-project
   ```sh
   cd valorant-project
   ```
3. Change .env.sample file name to .env.
   ```sh
   mv .env.sample .env
   ```
4. Fill out .env file with necessary data. Port number can be the default postgres port (***5432***).

5. Start the project.
   ```sh
   docker compose up --build
   ```
<!-- CONTACT -->

## Contact

Boglárka Bakos - [@Boglárka Bakos_LinkedIn](https://linkedin.com/in/boglarka-bakos)

Project Link: [https://github.com/Bogii02/valorant-project](https://github.com/Bogii02/valorant-project)


[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org

[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/

[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com

