# AI Health Data Visualization

This project is focused on visualizing health data using Python libraries such as `pandas`, `seaborn`, and `plotly`.

## Setup Instructions

### Prerequisites
- [Jupyter Notebook](https://jupyter.org/install) installed on your machine.
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your machine.


### Steps to Set Up the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/ai_health_data_visualization.git
    cd ai_health_data_visualization
    ```

2. **Create and activate a Conda environment:**

    ```bash
    conda create --name ai_health_env python=3.13.1
    conda activate ai_health_env
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the project:**
    Ensure you have the necessary data files in place and then open the project with VS Code:

    1. Open VS Code and install the Jupyter extension if you haven't already.

    2. Open the project folder in VS Code:

        ```bash
        code .
        ```

    3. Open the notebook file you want to run (e.g., `DataVisualizationAnalysis.ipynb`) and execute the cells.

### Troubleshooting

If you encounter a `ModuleNotFoundError`, ensure that you have activated the correct Conda environment and installed all dependencies.

```bash
conda activate ai_health_env
pip install -r requirements.txt