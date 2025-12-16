# Crime Spillover Analysis Using Hawkes Processes

This repository contains an analysis of crime spillover effects across Boston neighborhoods using Hawkes process modeling. The project focuses on understanding how crime events in one neighborhood influence subsequent crime intensity in the same or neighboring areas over time.

Most of the development and experimentation for this project was conducted in **Google Colab** and uploaded here.

---

## Repository Structure

The repository is organized around two main components:  
(1) shared preprocessing and exploratory analysis, and  
(2) neighborhood-specific spillover modeling.

### Core Preprocessing & Data Exploration

- **`O2Odata.ipynb`**  
  This notebook contains **preprocessing and exploratory data analysis**, including:
  - Data loading and cleaning
  - Timestamp parsing and event sequencing
  - Filtering and organizing crime events by neighborhood
  - Construction of event-time arrays used as input to Hawkes process models
  - Initial exploratory visualizations and summary statistics

  All subsequent analyses build on the outputs and assumptions established in this notebook.

### Figures

The figures folder contains code that was used to create some of our key visuals. 

---

### Neighborhood-Specific Spillover Analyses

The remaining notebooks analyze **individual neighborhood crime dynamics** and spillover behavior by crime type. Each notebook focuses on one district and applies Hawkes process modeling to estimate self-excitation and spillover effects on individual crime types. It measures the spillover between Roxbury and the following adjacent districts:

- **`B3.ipynb = Mattapan`**
- **`C6.ipynb = South Boston`**
- **`C11.ipynb = Dorchester`**
- **`D4.ipynb = South End`**
- **`E13.ipynb = Jamaica Plain`**
- **`South_end_all_crimes.ipynb`**

Each of these notebooks generally includes:
- Data cleaning (consistent with what's done in O2Odata)
- Model setup and parameter estimation
- Output to CSV and sort by strength of spillover 

While the structure is similar across notebooks, each one examines a **distinct local patterns**.

**Note:** Spillover analyses between neighborhoods using **all crime types** were also conducted. Two demo versions are included called **demo_JP** and **demo_Mattapan** (spillover between Roxbury and Jamaica Plain/Mattapan) to show what these files looked like. That analysis is maintained in a separate repository (https://github.com/younesszs/O2O) and the other districts are not included here. 

---