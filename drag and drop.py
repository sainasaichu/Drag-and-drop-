from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver (you may need to specify the path to your chromedriver)
driver = webdriver.Chrome()

# Open the jQuery UI Droppable demo page
driver.get("https://jqueryui.com/droppable/")

# Switch to the frame that contains the drag and drop elements
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

# Locate the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Perform the drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Pause for a few seconds to observe the result
time.sleep(3)

# Close the browser
driver.quit()
