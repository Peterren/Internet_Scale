**Continuous Integration with Selenium and Travis**

We used Selenium with the Chrome webdriver module to test the page source of our rendered front-end templates. The integration and unit tests are run on Travis CI. The mysql containers are setup in docker-compose beforehand. Travis builds up each of the containers in order specified.

We created tests for the front-end of our app. These included our core functions, including signing in our app, updating information, the iewing products. We also tested how the modules are integrated together by testing the if we can successfully access other pages through our buttons. The tests used the Selenium package to scrape the page source of the rendered pages from our fron end layer, and compare them to the desired html output. The tests are designed for the Chrome browser and we used the Chrome webdriver in Selenium for this purpose. The tests are run in a Selenium container in docker. 

we linked our github repository to Travis CI and create .travis.yml file to let it build online and run unit tests.
