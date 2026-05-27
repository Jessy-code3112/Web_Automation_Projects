import time
from playwright.sync_api import sync_playwright


def run_automation():
    # Start Playwright
    with sync_playwright() as p:
        # Launch a real browser window (headless=False means we want to see it visually)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("🌐 Navigating to website...")
        page.goto("http://quotes.toscrape.com/")

        # 1. Click on the 'Login' link
        print("🖱️ Clicking 'Login' button...")
        page.click("text=Login")

        # 2. Fill in the Username (Targeting by input element ID or name)
        print("✍️ Typing username...")
        page.fill('input[name="username"]', "my_username_jessy")

        # 3. Fill in the Password
        print("✍️ Typing password...")
        page.fill('input[name="password"]', "securepassword123")

        # 4. Click the 'Log In' submit button
        print("🚀 Submitting login form...")
        page.click('input[type="submit"]')

        # Pause for a few seconds so you can see the magic happen
        print("🎉 Successfully Logged In! Keeping browser open for 5 seconds...")
        time.sleep(5)

        # Close the browser
        browser.close()


if __name__ == "__main__":
    run_automation()