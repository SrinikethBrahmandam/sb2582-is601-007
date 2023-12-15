import pytest

@pytest.fixture()
def app():
    from ..main import create_app
    from ..sql.db import DB
    app = create_app()
    # insert dummy record to test at a negative index so it doesn't collide with valid values
    # note: this will likely still trigger auto_increment
    DB.insertOne("INSERT INTO IS601_Sample (id, name, val) VALUES (-1, 'tc','tcval')")
    # other setup can go here

    yield app

    # clean up / reset resources here
    DB.delete("DELETE FROM IS601_Sample WHERE id = -1")

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_edit_page(client):
    # https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/
    response = client.get("/sample/edit?id=-1")
    
    assert response.status_code == 200  # Make sure the request was successful
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.data, 'html.parser')
   
    form = soup.form
    
    assert form is not None, "No form found in the HTML"
    
    ele_list = form.select("[name='value']")
    
    assert ele_list, "No element with name='value' found in the form"
    
    ele = ele_list[0]
    
    assert ele is not None, "Selected element is None"
    
    print(ele)
    # for easier debugging run pytest with the -rP flags
    assert ele.get("value") == "tcval"
