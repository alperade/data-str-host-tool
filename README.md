<a name="readme-top"></a>

<!-- PROJECT TITLE -->
<br />
<div align="center">
  <h3 align="center">Short Term Rental Host Tool</h3>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#deployment-resources">Deployment Resources</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

Python project analyzing bookings data from Airbnb listings in Upstate, NY. Airbnb and OpenWeather external APIs are used to pull data on reservation calendar and weather.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Python
* DuckDB
* Pandas
* BeautifulSoup
* Numpy
* Requests
* Selenium


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

* Create a virtual environment
  ```sh
  python -m .venv venv
  ```
* Install pip requirements
  ```sh
  pip install -r requirements.txt
  ```
* Activate virtual environment
  ```sh
  source venv/bin/activate
  ```
* Run code
  ```sh
  python main.py
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/alperade/data-str-host-tool.git
   ```
2. Create an account on OpenWeather and get an API key.

3. Create an `keys.py` file
   ```py
   OPEN_WEATHER_API_KEY = 'ENTER OPEN WEATHER API KEY HERE'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- DEPLOYMENT RESOURCES -->
## Deployment Resources

* https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?tabs=azure-cli&pivots=container-linux
* Specify --platform=linux/amd64 each time you need to build or run an amd64 image/container.
* https://stackoverflow.com/questions/60163440/docker-fails-to-pull-the-image-from-within-azure-app-service

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Build project on gcloud, scheule it to run daily.
- [ ] Update Readme Roadmap

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

alperademoglu@gmail.com - [Linkedin](https://www.linkedin.com/in/alper-ademoglu/)

Project Link: [https://github.com/alperade/data-str-host-tool/](https://github.com/alperade/data-str-host-tool/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: /screenshot.png
