from pyscript import when, display, document
import js

@when("click", "#my_button")
def click_handler(event):
    js.alert("Button clicked")
    
