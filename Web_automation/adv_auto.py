import time
from playwright.sync_api import sync_playwright


def run_advanced_automation():
    with sync_playwright() as p:
        # Launch browser window visually
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("🌐 Navigating to website...")
        page.goto("http://quotes.toscrape.com/")

        # 1. Automated Login Phase
        print("🖱️ Clicking 'Login' button...")
        page.click("text=Login")

        print("✍️ Filling login credentials...")
        page.fill('input[name="username"]', "jessy_automation_user")
        page.fill('input[name="password"]', "password123")

        print("🚀 Submitting form...")
        page.click('input[type="submit"]')

        # 2. Capture Screenshot Phase
        print("📸 Taking a screenshot of the logged-in page...")
        # This will save a screenshot named 'dashboard_snapshot.png' in your folder
        page.screenshot(path="dashboard_snapshot.png", full_page=True)
        print("💾 Screenshot successfully saved as 'dashboard_snapshot.png'")

        # 3. Dynamic CSV Download Phase
        # Since 'Quotes to Scrape' doesn't have a real download button,
        # We will navigate to a standard downloadable link or handle download logic.
        print("📥 Preparing to trigger file download...")

        # We wait for the download event to trigger before clicking the download action
        with page.expect_download() as download_info:
            # For demonstration, we will route to a sample CSV link or trigger a mock download.
            # In a real dashboard, this would be page.click("#download-csv-btn")
            page.goto("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

        # Save the downloaded file to your local directory
        download = download_info.value
        download.save_as("downloaded_report.csv")
        print("🎉 CSV Report successfully downloaded and saved as 'downloaded_report.csv'")

        # 4. Extended Stay Time (Asking the browser to wait for 15 seconds)
        print("⏳ Keeping the browser open for 15 seconds for verification...")
        time.sleep(15)

        # Close the browser
        browser.close()


if __name__ == "__main__":
    run_advanced_automation()