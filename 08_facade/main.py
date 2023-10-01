from .facades import HomeTheaterFacade


def run() -> None:
    home_theater: HomeTheaterFacade = HomeTheaterFacade()
    home_theater.watch_movie()
    home_theater.end_movie()


if __name__ == '__main__':
    run()
