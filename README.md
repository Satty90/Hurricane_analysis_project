# Hurricane Analysis Project

This Python project analyzes historical hurricane data to extract meaningful insights about hurricane patterns, damage, and mortality.

---

## Project Description

The Hurricane Analysis project processes and analyzes data from multiple hurricanes, providing various insights such as:

- Damage caused by hurricanes (converted to numerical values)
- Organization of hurricane data by year
- Areas most affected by hurricanes
- Deadliest hurricanes
- Classification of hurricanes by mortality rate and damage scale

---

## Features

- **Data Conversion**: Converts string damage values (with "M" for millions and "B" for billions) to numerical values  
- **Hurricane Dictionary Creation**: Creates a comprehensive dictionary of hurricane data  
- **Year-based Organization**: Groups hurricanes by the year they occurred  
- **Area Impact Analysis**: Counts and identifies the most frequently affected areas  
- **Mortality Analysis**: Identifies the deadliest hurricanes and categorizes them by mortality scale  
- **Damage Analysis**: Finds the hurricane that caused maximum damage and categorizes hurricanes by damage scale

---

## Project Structure

- `data.py`: Contains all the hurricane datasets (names, dates, wind speeds, areas affected, damages, deaths)  
- `hurricanes.py`: Contains all the analysis functions and logic

---

## Usage

To run the analysis, simply execute the main Python file:
`python hurricanes.py`

This will display various analysis results:

- Complete hurricane dictionary  
- Hurricanes organized by year  
- Count of affected areas  
- Most affected area  
- Deadliest hurricane information  
- Hurricanes grouped by mortality rating  
- Hurricane with maximum recorded damage  
- Hurricanes grouped by damage rating

---

## Data Sources

The project analyzes data for 34 hurricanes, including:

- Names, months, and years of occurrence  
- Maximum sustained wind speeds  
- Areas affected by each hurricane  
- Damages in USD (converted from string format to numerical values)  
- Number of deaths caused

---

## Requirements

- Python 3.x  
- No external libraries required

---

## Future Enhancements

Potential improvements for this project could include:

- Visualization of hurricane data using libraries like Matplotlib or Seaborn  
- Adding more recent hurricane data  
- Statistical analysis of hurricane trends over time  
- Map-based visualization of affected areas
