# Navigator for the Habitable Worlds Observatory (HWO)

This project is developed as part of the [NASA Space Apps Challenge 2024](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/navigator-for-the-habitable-worlds-observatory-hwo-mapping-the-characterizable-exoplanets-in-our-galaxy/) hackathon. The aim is to create a tool that identifies and visualizes exoplanets in our galaxy, focusing on those with potential for habitability and sufficient data for characterization, using metrics like Signal-to-Noise Ratio (SNR) and planetary/star distance.

## Challenge Overview
The challenge involves working with existing datasets, such as the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/), to identify exoplanets that can be characterized based on their distance from their stars, size, and the ability of future telescopes (like the HWO) to detect features in their atmospheres&#8203;:contentReference[oaicite:2]{index=2}.

## Features
- **Exoplanet Data Querying**: Fetch data from NASA’s Exoplanet Archive.
- **Visualization**: Create charts and graphs that display exoplanet characteristics (e.g., distance from the star, size, and SNR).
- **Habitability Scoring**: Rank planets based on their potential for habitability.

## Installation

Clone this repository and install the required libraries:

### Dependencies
- `pandas` for data manipulation.
- `numpy` for numerical computations.
- `requests` for making API calls to NASA’s Exoplanet Archive.
- `plotly` for interactive data visualizations.

You can install these dependencies using:

```bash
pip install pandas numpy requests plotly
