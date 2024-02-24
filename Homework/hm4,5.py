from selenium import webdriver

def test_title():
    try:
        driver = webdriver.Chrome()

        #Navigates to the website
        driver.get("https://hub.docker.com")

        #Gets the title of the webpage
        title = driver.title

        #Checks if the title is "Docker Hub Container Image Library | App Containerization"
        if title == "Docker Hub Container Image Library | App Containerization":
            print("Test passed!")
        else:
            print(f"Title is '{title}'. Test failed.")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

test_title()