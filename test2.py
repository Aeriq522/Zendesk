import csv
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
     with open('tickets.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            Ticket_title = row[0]
            ticket_description = row[1]
            Location = row[1]
            Carrier = row[2]
            Download = row[3]
            Upload = row[4]
            Mount = row[5]
            Facp = row[6]
            Primary = row[7]
            Secondary = row[8]
            Burglar = row[9]
            Intercomm = row[10]
            Elevator = row[11]
            Elevator_notes = row[12]
            Fax = row[13]
            Total_dids = row[14]
            Notes = row[15]

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

            #Sign In
            page.locator("[data-test-id=\"header-toolbar-add-menu-new-ticket\"]").hover()
            page.locator("[data-test-id=\"header-toolbar-add-menu-new-ticket\"]").click()
            
            # Create a new ticket
            page.locator("[data-test-id=\"omni-header-subject\"]").click()
            page.locator("[data-test-id=\"omni-header-subject\"]").fill(Ticket_title)
            page.locator("[data-test-id=\"ticket-footer-macro-menu-autocomplete-input\"]").get_by_text("Apply macro").click()
            page.locator("#downshift-4-item-4").click()
            page.locator("[data-test-id=\"omnicomposer-rich-text-ckeditor\"]").click()
            page.get_by_text("Site Survey:").click()

     # Only update the text that is in the CSV file
            for index, value in enumerate(row):
                if index in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
                    template = page.get_by_text(f"{value}")
                    template.fill(row[index])
                    print(template)
                # page.get_by_text("{Location}").fill(Location)
                # page.get_by_text("{Carrier}").fill(Carrier)
                # page.get_by_text("{Download}").fill(Download)
                # page.get_by_text("{Upload}").fill(Upload)
                # page.get_by_text("{Mount}").fill(Mount)
                # page.get_by_text("{FACP}").fill(Facp)
                # page.get_by_text("{Primary}").fill(Primary)
                # page.get_by_text("{Secondary}").fill(Secondary)
                # page.get_by_text("{Burglar}").fill(Burglar)
                # page.get_by_text("{Intercomm_Number}").fill(Intercomm)
                # page.get_by_text("{Elevator}").fill("{Elevator}", Elevator)
                # page.get_by_text("{Elevator Notes}").fill(Elevator_notes)
                # page.get_by_text("{Fax}").fill(Fax)
                # page.get_by_text("{Total DiDs}").fill(Total_dids)
                # page.get_by_text("{Notes}").fill(Notes)
            page.locator("[data-test-id=\"ticket-system-field-requester-select\"]").click()
            page.get_by_placeholder("search name or contact info").fill("erik")
            page.get_by_text("esanchez@machnetworks.com").click()
            page.locator("[data-test-id=\"submit_button-menu-button\"]").click()
            page.locator("[data-test-id=\"submit_button-menu-open\"]").get_by_text("Submit as Open").click()

            # ---------------------
            context.close()
            browser.close()


with sync_playwright() as playwright:
    run(playwright)

print("done")