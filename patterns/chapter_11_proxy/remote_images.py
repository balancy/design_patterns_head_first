"""Abstract Remote Image Interface, it's implementation and proxy."""
import asyncio
from abc import ABC, abstractmethod

DOWNLOAD_DELAY = 2
REFRESH_RATE = 0.5


class AbstractRemoteImage(ABC):
    """Abstract Remote Image Interface."""

    @abstractmethod
    async def display(self):
        """Abstract display method.

        All child classes should implement this method.
        """
        pass


class RemoteImage(AbstractRemoteImage):
    """Remote Image class."""

    def __init__(self) -> None:
        """Initialize Remote Image.

        It's not downloaded by default.
        """
        self._is_downloaded = False

    async def download(self):
        """Download the image."""
        await asyncio.sleep(DOWNLOAD_DELAY)
        self._is_downloaded = True

    async def display(self):
        """Display the downloaded image."""
        print('Displaying the downloaded image.')

    @property
    def is_downloaded(self) -> bool:
        """Check if the image is downloaded."""
        return self._is_downloaded


class Proxy(AbstractRemoteImage):
    """Proxy class for Remote Image."""

    def __init__(self, remote_image: RemoteImage) -> None:
        """Initialize Proxy."""
        self._remote_image = remote_image

    async def display_fake(self):
        """Display fake image."""
        while not self._remote_image.is_downloaded:
            print('Displaying the fake image.')
            await asyncio.sleep(REFRESH_RATE)

    async def display(self):
        """Display the image.

        Displays the fake image while the real image is downloading.
        """
        task1 = asyncio.create_task(self._remote_image.download())
        task2 = asyncio.create_task(self.display_fake())

        await task1
        await task2
        await self._remote_image.display()
