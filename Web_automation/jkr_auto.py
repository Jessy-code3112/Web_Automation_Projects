import time
import pandas as pd
from playwright.sync_api import sync_playwright


def run_jk_rowling_automation():
    with sync_playwright() as p:
        # Launch browser window visually
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Navigating Step
        print("🌐 Navigating to J.K. Rowling's Quotes page...")
        page.goto("http://quotes.toscrape.com/author/J-K-Rowling/")

        # 2. Screenshot Step
        print("📸 Taking a snapshot of the page...")
        page.screenshot(path="jk_rowling_quotes.png", full_page=True)

        # 3. Data Extraction and Saving Step (Behind the scenes)
        quotes_elements = page.query_selector_all(".quote")
        quotes_data = []

        for index, element in enumerate(quotes_elements, start=1):
            text_el = element.query_selector(".text")
            text = text_el.inner_text() if text_el else ""

            tag_elements = element.query_selector_all(".tags .tag")
            tags_list = [tag.inner_text() for tag in tag_elements]
            combined_tags = ", ".join(tags_list)

            quotes_data.append(
                {
                    "No.": index,
                    "Author": "J.K. Rowling",
                    "Quote": text,
                    "Tags": combined_tags,
                }
            )

        # Save to CSV quietly without printing the whole table to terminal
        df = pd.DataFrame(quotes_data)
        df.to_csv("jk_rowling_with_tags.csv", index=False)

        # 4. Success Dashboard Messages (The 2-3 lines you wanted!)
        print("💾 Screenshot successfully saved as 'jk_rowling_quotes.png'")
        print("🎉 CSV Report successfully generated as 'jk_rowling_with_tags.csv'")

        # 5. Keep page open for 30 seconds
        print("⏳ Keeping the browser open for 30 seconds...")
        time.sleep(30)

        browser.close()


if __name__ == "__main__":
    run_jk_rowling_automation()