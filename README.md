# Computer Infrastructure

This repository contains my work for the Computer Infrastructure module, part of the Science in Computing (Data Analytics) course at [Atlantic Technological University (ATU)](https://www.atu.ie/).  

Author: [Elaine R. Cazetta](https://github.com/elainecazetta)   
Lecturer: [Ian McLoughlin](https://github.com/ianmcloughlin)   

## Module Overview

The Computer Infrastructure module covers:

- Using and configuring command-line / shell environments  
- Manipulating data, files, and code via the command line  
- Understanding software infrastructures, architectures, and tools  
- Evaluating and selecting infrastructure components for computational tasks 

The course materials, lectures, and assessments are maintained in the lecturer’s repository:  
[Computer Infrastructure (Ian McLoughlin)](https://github.com/ianmcloughlin/computer-infrastructure).

## About the Assessments & Problems

This repository includes a set of hands-on problems, provided by our lecturer, that help you learn how software infrastructure and automation work in practice. The original problem descriptions are [available here](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/problems.md).
Each task uses **Python** and **GitHub** to collect, process, visualize, and automate financial data for the five **FAANG** companies — Facebook, Apple, Amazon, Netflix, and Google.

Here’s a summary of the assessment problems:

| Problem | Summary |
|----------|----------|
| **Problem 1 – Data from yfinance** | Create a function `get_data()` that uses the **yfinance** Python library to download hourly stock data for the past 5 days for the five FAANG companies. Save the data as a timestamped CSV file inside a new `data/` folder. |
| **Problem 2 – Plotting Data** | Write a function `plot_data()` that opens the most recent data file, plots the **Close** prices for all five stocks on one chart, and includes axis labels, a legend, and the date as the title. Save the figure in a `plots/` folder using a similar timestamped filename. |
| **Problem 3 – Script** | Combine the previous two functions into a script named `faang.py` that can be run directly from the terminal. The script should automatically fetch the data and create the plot. |
| **Problem 4 – Automation** | Automate everything by creating a **GitHub Actions** workflow (`faang.yml`) inside `.github/workflows/`. The workflow should run the script automatically every **Saturday morning**. |

Each problem is implemented and explained in the **`problems.ipynb`** notebook, where outputs and reasoning are documented.

## Tools & Libraries Used

To complete these tasks, I used the following tools and libraries:

- **Python**: The programming language used for all tasks. Download it [here](https://www.python.org/downloads/).  
- **Jupyter Notebook**: A web-based environment for running Python code. Learn more [here](https://jupyter.org/).  
- **Pandas**: A library for data manipulation and analysis. Documentation [here](https://pandas.pydata.org/docs/).

## How to Run the Code  

Follow the steps below to set up and run this project:  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/elainecazetta/computer_infrastructure.git
   cd computer_infrastructure
   ```  

2. **Install dependencies**
Make sure you have Python 3 installed. Then, install the required libraries using:    
   ```bash
   pip install -r requirements.txt
   ```
(If you’re using GitHub Codespaces, dependencies are pre-installed automatically.)  

3. **Open the Jupyter Notebook**
- In GitHub Codespaces: Open `problems.ipynb` directly from the file explorer.  
- On your local machine: Start Jupyter Notebook by running:  
```bash
   jupyter notebook
```
Then open `problems.ipynb` from the Jupyter dashboard.  

4. **Run the notebook cells in order**  
Each problem (1–4) is clearly labeled. Running all cells sequentially will:  

- Download the FAANG stock data (Problem 1)  
- Generate and save plots (Problem 2)  
- Execute the combined script logic (Problem 3)  
- Trigger the GitHub Actions automation (Problem 4)  

## End
