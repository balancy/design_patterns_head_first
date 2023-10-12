"""Proxy Pattern example module."""

import asyncio

from .remote_images import Proxy, RemoteImage


async def run_pattern_example() -> None:
    """Run proxy example.

    While remote image is downloaded, proxy displays fake image.
    """
    remote_image = RemoteImage()
    proxy = Proxy(remote_image)

    await proxy.display()


if __name__ == "__main__":
    asyncio.run(run_pattern_example())
