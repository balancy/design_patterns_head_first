"""Main entrypoint for the Facade pattern example."""


from .facades import HomeTheaterFacade


def run_pattern_example() -> None:
    """Test facade pattern example.

    Run only one facade method to make all devices work toghether.
    """
    home_theater: HomeTheaterFacade = HomeTheaterFacade()
    home_theater.watch_movie()
    home_theater.end_movie()


if __name__ == '__main__':
    run_pattern_example()
