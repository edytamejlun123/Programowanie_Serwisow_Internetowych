from dependency_injector import containers, providers
from services.weather_service import WeatherService
import os

if os.environ['zmienna'] == '1':
    from repositories.weather_repo_db import WeatherRepo
else:
    from repositories.weather_repo_txt import WeatherRepo



class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repo = providers.Singleton(
        WeatherRepo,
    )

    service = providers.Factory(
        WeatherService,
        repo=repo,
    )
