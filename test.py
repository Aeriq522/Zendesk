import csv
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    with open('tickets.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            ticket_title = row[0]
            ticket_description = row[1]


            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://machnetworks.zendesk.com/agent/filters/360205088072")
            page.goto("https://machnetworks.zendesk.com/access/unauthenticated?return_to=https%3A%2F%2Fmachnetworks.zendesk.com%2Fagent%2Ffilters%2F360205088072")
            page.goto("https://machnetworks.zendesk.com/auth/v2/login/signin?return_to=https%3A%2F%2Fmachnetworks.zendesk.com%2Fagent%2Ffilters%2F360205088072&theme=hc&locale=1&brand_id=360005574752&auth_origin=360005574752%2Cfalse%2Ctrue&role=agent")
            page.get_by_label("Email").click()
            page.get_by_label("Email").fill("esanchez@machnetworks.com")
            page.get_by_label("Password").click()
            page.get_by_label("Password").fill("Esm522@@Zendesk")
            page.get_by_role("button", name="Sign in").click()

            # Create a new ticket
            page.locator("[data-test-id=\"header-toolbar-add-menu-new-ticket\"]").hover()
            page.locator("[data-test-id=\"header-toolbar-add-menu-new-ticket\"]").click()
            page.locator("[data-test-id=\"omni-header-subject\"]").click()
            page.locator("[data-test-id=\"omni-header-subject\"]").fill(ticket_title)
            page.locator("[data-test-id=\"omnichannel-channel-switcher-button\"]").click()
            page.get_by_text("Internal note").click()
            page.locator("[data-test-id=\"omnicomposer-rich-text-ckeditor\"]").get_by_role("paragraph").fill(ticket_description)
            page.get_by_placeholder("search name or contact info").fill("er")
            page.locator("[data-test-id=\"ticket-system-field-requester-menu\"]").get_by_text("ik Sanchez").click()
            page.locator("[data-test-id=\"assignee-field-take-it-button\"]").click()
            page.locator("[data-test-id=\"submit_button-menu-button\"]").hover()
            page.locator("[data-test-id=\"submit_button-menu-button\"]").click()
            page.get_by_text("Submit as Open").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

print("done")