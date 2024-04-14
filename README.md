# GeoElevation

## Project Description
GeoElevation is a tool for downloading terrain elevation data, including building overlays, from the geoportal.gov.pl service. This tool specifically targets geographical data from Poland.

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- Python 3.10
- pip (Python package installer)
- Git

## Installation

### Step 1: Clone the Repository
Start by cloning the repository to your local machine. Open your terminal and execute:
`git clone https://github.com/Swietonp/geo-elevation.git`

### Step 2: Create and Activate a Python Virtual Environment
1. `cd <project-directory-name>`
2. `python -m venv venv`
3. `venv\Scripts\activate`

### Step 3: Install Required Dependencies
1. `pip install -r requirements.txt`

## Running script
Once the setup is complete, you can run the application using the following command in your terminal. You need to provide two coordinates as arguments to the command. You can specify these either as Cartesian coordinates (`--x` and `--y`) or as latitude and longitude (`--lat` and `--long`).

### Using Cartesian Coordinates EPSG:2180 (CS92)
`python main.py --x 641412.648697 --y 488156.603191`

### Using Using Geographic CoordinatesEPSG:4326 (WGS 84)
`python main.py --lat 52.21 --long 20.99`
