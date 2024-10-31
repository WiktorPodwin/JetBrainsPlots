# Game Genre Bar Chart Project

## WHAT WILL YOU LEARN TODAY?
This lesson is about how to create a single bar chart to show the genres of games for four gaming platforms (PS4, XOne, PC, and WiiU). This project uses Python and the Matplotlib library for data visualization.

## REQUIREMENTS
* Python 3.9.20
* pip 
* Git

## PROJECT SETUP
* Clone the git repository
```bash
git clone https://github.com/WiktorPodwin/VisualizePipeline.git
```

* Install required packages
```bash
pip install -r requirements.txt
```

## PROJECT WORKFLOW
Each of steps should be completed by the following order:

1. Data Ingesting 
* Goal: Download data using HTTP request, save the data into specified file, ingest data as Dataframe
* Directory: 'lessons/extract/'
* Files: 'Task.md'- task and theory, 'load_data.py' - reference solution, 'test_load_data.py' - unit tests, 'your_extract_solution.py' - file where to solve the task

2. Data Transforming 
* Goal: Clean and prepare the data to the final form
* Directory: 'lessons/transform/'
* Files: 'Task.md'- task and theory, 'transform_data.py' - reference solution, 'test_transform_data.py' - unit tests, 'your_transform_solution.py' - file where to solve the task

3. Data Visualization 
* Goal: Create a bar chart to display the data and save the image to specified file
* Directory: 'lessons/visualize/'
* Files: 'Task.md'- task and theory, 'visualization.py' - reference solution, 'test_visualization.py' - unit tests, 'your_visualization_solution.py' - file where to solve the task


### For each step:
* Read the theory 
* Introduce yourself with tasks
* Use tests to verify your solution (you need to run this command in step directory)
``` bash
python3 -m unittest
```

## PROJECT EXECUTION:
The file `main.py` combines all operations and executes them. In the general directory, run:
``` bash
python3 main.py
```