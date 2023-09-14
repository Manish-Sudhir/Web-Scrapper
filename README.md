
# Football Analytics Web-Scraper

## Overview

This project is a data collection pipeline designed to scrape football team information from a prominent football analytics website ( https://www.transfermarkt.co.uk) using Selenium. The scraped data is then stored in a PostgreSQL database hosted on Amazon AWS, utilizing data engineering philosophies and technologies.

![Transfermarkt Page where data will be scrapped](https://github.com/Manish-Sudhir/Web-Scrapper/blob/main/screen.png?raw=true "Transfermarkt Page where data will be scrapped")

### Project Goals

- Scrape football team information efficiently from a website.
- Store the collected data in a PostgreSQL database on Amazon AWS.
- Apply data engineering principles to ensure data quality and reliability.
- Utilize Python packages for web scraping, data manipulation, and database interaction.

## Project Structure

The project consists of the following main components:

- `main.py`: This script initializes the web scraper, searches for a football team (e.g., PSG), and collects team information.

- `utils/mal.py`: Contains the generic `Scrapper` class, which hosts functions for web scraping, and the `PlayerScrapper` class, a child class designed for this specific web scraping use case.

- `setup.py`: A Python package configuration file listing project dependencies.

- `requirements.txt`: A file listing the project's dependencies for easy installation.
  
-  `Dockerfile`: The Dockerfile used to containerize the project.

![Created a general web-scrapper class](https://github.com/Manish-Sudhir/Web-Scrapper/blob/main/scrapper.png?raw=true "Created a general web-scrapper class")

![Scrapper that scrapes for player data](https://github.com/Manish-Sudhir/Web-Scrapper/blob/main/scrapper.png?raw=true "Scrapper that scrapes for player data")

## Installation

To run the project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/football-analytics-scraper.git

2. Install project dependencies using pip:
   ```bash
    pip install -r requirements.txt

## Usage

1. Open the main.py file and modify the database connection details as needed:
   ```bash
    engine = create_engine('postgresql+psycopg2://your-username:your-password@your-database-url:5432/your-database-name')

2. Run the web-scrapper script
   ```bash
   python main.py

## Docker Containerization

You can also run the project within a Docker container. A Dockerfile is provided for your convenience. Here's how to use it:

1. Build the Docker image from the project directory:
   ```bash
   docker build -t football-analytics-scraper .

2. Run the Docker container:
   ```bash
   docker run football-analytics-scraper
This will execute the web scraper script within the Docker container.

3.Ensure you have the necessary database and AWS credentials configured within the Docker environment for database interaction.

## Dependencies

-selenium: Web automation library for web scraping.
-webdriver_manager: Manages web driver installations for Selenium.
-pandas: Data manipulation library for handling scraped data.
-sqlalchemy: SQL toolkit and Object-Relational Mapping (ORM) library for database interaction.
-psycopg2-binary: PostgreSQL adapter for Python.

## Contributing

Contributions to this project are welcome! If you have ideas for improvements or new features, please open an issue or create a pull request.

## License

This project is licensed under the MIT License.







