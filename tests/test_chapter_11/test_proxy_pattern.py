"""Module for testing pattern Proxy."""
import pytest

from patterns.chapter_11_proxy.remote_images import Proxy, RemoteImage


@pytest.mark.asyncio
async def test_proxy_pattern():
    """Test proxy pattern.

    Proxy displaying fake image while remote image is downloaded.
    """
    remote_image = RemoteImage()
    proxy = Proxy(remote_image)

    assert not remote_image.is_downloaded
    await proxy.display()
    assert remote_image.is_downloaded
