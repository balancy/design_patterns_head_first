"""Proxy Pattern example module."""

import asyncio

from .remote_images import Proxy, RemoteImage


async def run_pattern_example() -> None:
    """Run proxy example.

    While remote image is downloaded, proxy displays fake image.
    """
    remote_image = RemoteImage()
    proxy = Proxy(remote_image)

    task1 = asyncio.create_task(remote_image.download())
    task2 = asyncio.create_task(proxy.display())

    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(run_pattern_example())
