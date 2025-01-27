# AI Health Data Visualization

This project is focused on visualizing health data using Python libraries such as `pandas`, `seaborn`, and `matplotlib`.

## Setup Instructions

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your machine.

### Steps to Set Up the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/zestybean/ai_health_data_visualization
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

    Ensure you have the necessary data files in place and then run your main script:

    ```bash
    python main.py
    ```

### Troubleshooting

If you encounter a `ModuleNotFoundError`, ensure that you have activated the correct Conda environment and installed all dependencies.

```bash
conda activate ai_health_env
pip install -r requirements.txt