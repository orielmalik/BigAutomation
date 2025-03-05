from playwright.async_api import async_playwright
import pytest

class AsyncPlaywright:
    def __init__(self):
        self.browser = None
        self.page = None

    async def start_browser(self):
        async with async_playwright() as p:
            self.browser = await p.chromium.launch(headless=False)
            self.page = await self.browser.new_page()

    async def close_browser(self):
        await self.browser.close()

    async def go_to_url(self, url):
        await self.page.goto(url)

    async def get_title(self):
        return await self.page.title()