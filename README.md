# ExoMapper

A 3D application that interactively showcases the potential of the Habitable World Observatory (HWO) to find possible habitable planets in our galaxy. By using physical characteristics of existing exoplanets, we combined this information with the expected design of the HWO(like mirror radius, frequency band observation and orbital distance). Thus, scientists, politicians, and the general public can clearly understand the progress of scientific advancements.

# Project Demo
[Video Presentation](https://drive.google.com/file/d/1sXnv5yVxffHoo5NAmxHZYCpBK5xh0rPW/view?usp=sharing)

[Final Project](https://github.com/jojogab/navigator-nasa-hacks)

## Documentation

[Slide Documentation](https://www.canva.com/design/DAGS0QFDLT8/7pJ7KuIO5oVcK9qgxQrwCA/view?utm_content=DAGS0QFDLT8&utm_campaign=designshare&utm_medium=link&utm_source=editor)

## Project Details
Our project has two distinct parts: backend development and frontend development.
For the backend development, after requesting data from NASA's API, we processed it to produce an observability score. We directly used three simple parameters for the analysis: 1) The Radius of the Exoplanet: the larger the radius of the exoplanet, the more likely it is to be detected, as both transit and radial velocity methods favor planets with a larger radius. However, the radius should be less than 3.5 times that of Earth to preserve habitable characteristics. 2) The Mass of the Exoplanet: More massive planets tend to influence the center of gravity of their system, making them easier to detect. 3) Distance from Earth: The farther away an object is from Earth, the more difficult it becomes to observe it, especially exoplanets.
With this score, we considered the design characteristics of the HWO, which, as an observatory, should prioritize these parameters to enhance observation. Additionally, it uses physical parameters related to habitability criteria to determine if a candidate planet could potentially support life.
For the frontend development, we created a 3D application that organizes planets based on their observability potential, represented by a score from 0 to 100%, displayed in colors, with warmer colors indicating higher observability. From this, we can identify the characteristics that enhance a potentially habitable exoplanet's chances of being observed by our observatory.
## Programing Languages

**Python:** Used for data manipulation and making requests to NASA's API.

**JavaScript:** Used for interaction logic on the frontend and updating charts.

**HTML:** Used to structure the web page.

**CSS:** Used to style the web page.

## Libraries and Frameworks
**Pandas:** Used in Python for data manipulation and analysis.

**NumPy:** Used in Python for numerical calculations and array manipulation.

**Requests:** Used in Python to make HTTP requests to NASA's API.

**Plotly.js:** Used in JavaScript for data visualization and creating interactive charts.

**Flask:** A framework is being used to host the backend (not mentioned, but common).

## APIs
**NASA Exoplanet Archive:** API used to obtain data about exoplanets.

## Development Tools
**Postman:** Used for testing APIs.
**GitHub:** Used for code versioning and collaboration (not explicitly mentioned, but common practice).

## Version Control and Collaboration
**NASA Exoplanet Archive:** API used to obtain data about exoplanets.

## Data Structures and Models
**DataFrame:** Used in Pandas for manipulating tabular data.

## Referência

- [Nasa API](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html)
- [Nasa Exoplanets API](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html)
- [ESA Exoplanets](hhttps://www.esa.int/Science_Exploration/Space_Science/Exoplanets)
- [Nasa Habitable Worlds](https://astrobiology.nasa.gov/research/astrobiology-at-nasa/habitable-worlds/)
- [Open AI](https://chatgpt.com/)
- [Capcut](https://www.capcut.com/pt-br/)
- [Copilot](https://copilot.microsoft.com/)




![Logo] (https://drive.google.com/file/d/1fwV5UVx3lnA7683KJzT6O6kLrp9vMOz6/view?usp=drive_link)


## Screenshots

![App Screenshot](https://drive.google.com/file/d/1yd1vYzxmRnp-MxyBTsC-wJ96PjW5Pf1_/view?usp=drive_link)
![App Screenshot](https://drive.google.com/file/d/1NnCsdDx_tV9z0uagydtvR0yjOSj2dwIa/view?usp=drive_link)


## Autores

- [@kritgarb](https://www.github.com/kritgarb)
- [@fdoargolo] (https://github.com/fdoargolo)
- [@jojogab] (https://github.com/jojogab)
- [@ziulalb] (https://github.com/ziulalb)
- [@viferreira-p] (https://github.com/viferreira-p)

## Documentação de cores

| Cor               | Hexadecimal or RGB                                               |
| ----------------- | ---------------------------------------------------------------  |
| Gradient Start      | ![#000428](https://via.placeholder.com/10/000428?text=+) #000428 |
| Gradient End     | ![#004e92](https://via.placeholder.com/10/004e92?text=+) #004e92 |
| Main Text       | ![#e0e0e0](https://via.placeholder.com/10/e0e0e0?text=+) #e0e0e0 |
| Header and Footer      | ![rgba(0, 0, 0, 0.8)](https://via.placeholder.com/10/rgba(0,0,0,0.8)?text=+) rgba(0, 0, 0, 0.8) |
| Header/Footer Shadow     | ![rgba(255, 255, 255, 0.2)](https://via.placeholder.com/10/rgba(255,255,255,0.2)?text=+) rgba(255, 255, 255, 0.2) |
| Title Shadow    | ![rgba(0, 0, 0, 0.7)](https://via.placeholder.com/10/rgba(0,0,0,0.7)?text=+) rgba(0, 0, 0, 0.7) |
| Footer Border     | ![rgba(255, 255, 255, 0.2)](https://via.placeholder.com/10/rgba(255,255,255,0.2)?text=+) rgba(255, 255, 255, 0.2) |

