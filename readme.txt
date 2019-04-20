This is a Weather App Website.
The API key is hard coded in the program and it is not allowed to use for commercial purpose.
The code is wroten in Python3.
To use the program, user must first install flask and requests using commands "pip install flask" and "pip install requests".
To run the program, use command "py -3 server.py" in Windows PowerShell and then open "http://127.0.0.1:5000/" in the browser.
After that, user can type the city name and click the search button.
If the input name is invalid, the website will be directed to a page with error message.
If the input name is valid, the website will display city name, current weather, current temperature, maximum and minimum temperature of the day, pressure and humidity.
Additionally, the website will display hourly forecast for the next 24 hours and hourly forecast for the next 96 hours using charts and all these temperatures are displayed in Celsius.
Clicking the return button redirects website to the home page.