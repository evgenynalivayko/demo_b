from selene.support.shared import browser
from selene import by, be, have



def test_auth_with_valid_password():
    # browser.config.window_width = 500
    # browser.config.window_height = 500
    # browser.open("https://bumbleby.ru")
    # browser.element("input[type='text']").type("nalivayko.ev@gmail.com")
    # browser.element("input[type='password']").type("Aa123456")
    # browser.element("//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
    # browser.element(".scrollmenu").hover()
    # browser.element(".avatar_link").click()
    # text_name = browser.element(".name").text
    # text_name_splitted = text_name.split(" ")
    # assert text_name_splitted[0] == "Наливайко"
    # browser.element(".scrollmenu").hover()
    # browser.element(".logout_name").click()

    import psycopg2
    conn = psycopg2.connect(dbname="demo", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books;")
    res = cur.fetchall()
    print(res)
    cur.close()
    conn.close()

def test_auth_with_valid_password2():
    pass
