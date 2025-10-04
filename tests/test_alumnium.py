import os
from alumnium import Alumni
from playwright.sync_api import sync_playwright, expect
from dotenv import load_dotenv
load_dotenv()

def test_service_now(my_page):        
    # setup alumnium
    al = Alumni(my_page)

    # start test
    my_page.goto(os.environ["SNOW_URL"])
    
    al.do(f"log in with { os.environ["SNOW_USER"] } and { os.environ['SNOW_PASSWORD'] }")
    al.check("ServiceNow text is visible in the top nav")
    al.do("click Favorites on top nav, and click 'incidents' menu item")
    al.check("page title contains Incidents")

    # al.do("click 'New' button on top right of nav bar")
    my_page.click("button:has-text('New', exact=True)")  # AI is facing hard timeto find this button
    al.check("text 'New record' present in top left")
    al.do("fill in the 'short description' with 'Test incident from alumnium'")
    al.do("set the 'Urgency' to '1 - High'")    
    al.do("click the 'Submit' button on top right")

    al.check("the 'incidents' list visible")
    al.check("the incident with Short description 'Test incident from alumnium' visible in the list")

    my_ele = al.find("the number column for the found incident")
    expect(my_ele).to_have_text(r"INC\d+")

