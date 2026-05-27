import time
import pandas as pd
from playwright.sync_api import sync_playwright


def run_book_automation():
    with sync_playwright() as p:
        # Launch browser window visually
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("🌐 Navigating to Books Store...")
        page.goto("https://books.toscrape.com/")

        # 1. Playful Interaction: အော်တိုမေးရှင်းကို ဘယ်ဘက်က "Travel" အမျိုးအစားခလုတ်ကို လှမ်းနှိပ်ခိုင်းမယ်
        print("🖱️ Automatically clicking 'Travel' category from the sidebar...")
        # Exact matching using text selector
        page.click("text=Mystery")

        # 2. Stay and Capture Screenshot
        print("📸 Taking a beautiful snapshot of the Mystery Books page...")
        page.screenshot(path="Mystery_books_dashboard.png", full_page=False)

        # 3. Extracting the list of books in that specific category
        print("📥 Gathering all books inside Mystery category...")
        book_elements = page.query_selector_all(".product_pod")
        mystery_books = []

        for index, element in enumerate(book_elements, start=1):
            title_el = element.query_selector("h3 a")
            title = title_el.get_attribute("title") if title_el else ""

            price_el = element.query_selector(".price_color")
            price = price_el.inner_text() if price_el else ""

            mystery_books.append({"No.": index, "Title": title, "Price": price})

        # Save to CSV
        df = pd.DataFrame(mystery_books)
        df.to_csv("mystery_books_report.csv", index=False)

        # 4. Final Verification Message
        print("\n🏆 --- Automation Success Dashboard ---")
        print("💾 Screenshot captured: 'travel_books_dashboard.png'")
        print("📊 Data Exported: 'travel_books_report.csv'")

        # Keep browser open for 20 seconds to enjoy the view
        print("⏳ Browser will stay open for 20 seconds...")
        time.sleep(20)

        browser.close()


if __name__ == "__main__":
    run_book_automation()