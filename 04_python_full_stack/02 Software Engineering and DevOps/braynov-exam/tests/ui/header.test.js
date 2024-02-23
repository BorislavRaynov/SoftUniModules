const { test, expect } = require('@playwright/test');

test('Check header', async ({ page }) => {
    await page.goto('https://braynov-exam.onrender.com/'); 
    const homeLink = await page.$('[href="/"]');
    const text = await homeLink.textContent();
    expect(text).toBe('Home');
  });
  