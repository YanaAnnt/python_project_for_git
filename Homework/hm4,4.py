from selenium import webdriver

def test_ycombinator_title():
    try:
        driver = webdriver.Chrome()

        #Navigates to the Y Combinator website
        driver.get("https://www.ycombinator.com/")

        #Gets the title of the webpage
        title = driver.title

        #Checks if the title is "Y Combinator"
        if title == "Y Combinator":
            print("Title is 'Y Combinator'. Test passed!")
        else:
            print(f"Title is '{title}'. Test failed.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

test_ycombinator_title()
