from playwright.sync_api import sync_playwright


def search_google(query):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        page.goto(
            "https://www.google.com"
        )

        page.wait_for_load_state()

        search_box = page.locator(
            'textarea[name="q"]'
        )

        search_box.fill(query)

        search_box.press("Enter")

        page.wait_for_timeout(5000)

        headings = page.locator("h3")

        count = headings.count()

        results = []

        for i in range(min(count, 10)):

            try:

                title = headings.nth(i).inner_text()

                results.append({
                    "title": title
                })

            except Exception:
                pass

        return results