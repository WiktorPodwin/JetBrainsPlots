# Step: Visualize

## Theory
In this step, we will focus on visualizing the transformed data using a bar plot. Visualization is crucial in data analysis as it helps convey insights and patterns in a clear and intuitive manner. Here’s how we will accomplish this:

1 - `Creating the Bar Plot`: We will use the matplotlib library to create a bar plot that displays the distribution of game genres across various gaming platforms. The BarPlot class encapsulates the logic for generating the plot.

Key points to remember:

* Ensure that the DataFrame provided to the plot is not empty; otherwise, it will raise an error.
* Use the pivot() function to reshape the DataFrame so that platforms become the index, genres become the columns, and the count of games is represented as the values.
* Handle color mapping for the bars to visually differentiate between genres.
* Setting Up Plot Attributes: We will customize the plot’s title, axis labels, ticks, and legends to enhance readability and provide context. This is important for effectively communicating the information represented in the plot.

Important considerations:

* Use set_title(), set_xlabel(), and set_ylabel() to add descriptive titles and labels.
* Customize ticks and legends to ensure they are informative and easy to understand.

2 - `Saving the Plot`: After creating the plot, we will save it as an image file to a specified path using the savefig() function from matplotlib. This allows us to share or present the visualization later.

Key functions in Matplotlib:

* plt.savefig() is used to save the created plot to a file.
* Always ensure the file path is correct to avoid file saving errors.

The entire plotting process is encapsulated in the BarPlot class, which includes two primary methods:
* `create_plot(df)`: Generates a bar plot from the provided DataFrame.
* `save_image(plot_path)`: Saves the generated plot to the specified path.

## Task
Your task is to implement a script that utilizes the BarPlot class defined in the reference solution. Follow these steps to complete the task:

1. Instantiate the BarPlot Class:
* Create an instance of the BarPlot class.

2. Create the Plot:
* Call the create_plot() method which creates bar chart with the transformed DataFrame obtained from the previous step.

3. Save the Plot:
* Use the save_image() method to save the created plot to a specified file path.