# Lab 2: Pandas and Data Manipulation

In this lab, we will explore essential Pandas functions and their usage in data manipulation and analysis.

> **Note**: You don't have to remove/delete any `q{n}.check()` or `q{n}.hint()` or any variables/code from the notebook anymore. You only need to add some code to the code block.
>
> **IMPORTANT: Your code must run without errors before submission to ensure proper evaluation.**
>
> *Other notes are stated in the notebook. Please read them carefully.*
>
> *For this lab, we highly recommend you use local machine to work on the exercises for the simplicity of dataset setup.*

## Overview

When you're reading this, you've probably accepted the assignment. This is your repository for the first assignment with Github Classroom.

You will only have to edit the notebook [`exercises.ipynb`](exercises.ipynb) and submit it. The notebook contains a series of exercises that will test your understanding of the Pandas library. You will need to complete the exercises and can check with the provided tool.

## Using this notebook

The notebook is structured as a series of code blocks, each containing a function definition with a `raise NotImplementedError` statement. You need to replace this statement with your code to answer the question.

```python
## Q1: Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}

def question_1(data):
    return pd.DataFrame(data)  # return a DataFrame created from the dictionary

q1_sol = question_1(data)  # Example test case
q1.check()  # Check the solution
```

Attempt all questions to get grade evaluated. You can check your answers by running the check function provided in each question.

> **DO NOT ALTER THE VARIABLE NAMES. YOU CAN CHANGE THE INPUTS TO THE FUNCTION CALLS.**

To check your solution, run the following command:

```python
q1.check()
```

> **Note**: The `q1` variable is a test case object and the `check` method will run a series of test cases to validate your solution.

You can also use the `q1.hint()` function to get a hint if you're stuck.

```python
q1.hint()
```

## Submission

After completing the notebook, you need to submit your [`exercises.ipynb`](exercises.ipynb) file. You have various way of doing this.

1. You can go directly to your repository and use the ![upload-file](https://github.com/user-attachments/assets/17bb42af-20f2-40de-9e64-0e64295d1d31) button to update the file.
2. If you're using Github Codespaces or any other IDE *(code editor)*, you can commit the changes and push to the repository.
    - First you need to clone the repository to your local machine. *(this step is skipped if you're using Codespaces)*
    - Open the terminal and run the following command to clone the repository.

    ```bash
    git clone <repository-url>
    ```

    - After cloning, navigate into the repository directory:

    ```bash
    cd <repository-name>
    ```

    - Make changes to the `exercises.ipynb` file and save.
    - Commit and push your changes following the steps below:

    ```bash
    git add exercises.ipynb
    git commit -m "Completed exercises"
    git push origin main
    ```

    ![git-basic-workflow](./assets/git-basic-workflow.png)

    > *Checkout [this documentation](https://docs.github.com/en/get-started/start-your-journey/git-and-github-learning-resources) to learn more about Git and Github.*

3. You can view your score by going to the Actions tab in the repository and selecting the latest workflow run. You can see the results of the autograding process.
    ![ghaction-grade](assets/autograding-github-action.png)

    Or you can checkout the Pull Requests tab to see your grading results.
    ![action-bot](assets/github-action-bot.png)

## Content

In this lab, you will work through several tasks that involve:

- **Creating and Manipulating Arrays**: Learn how to create Numpy arrays, examine their properties, and manipulate them using reshaping and slicing.
- **Performing Mathematical Operations**: Apply arithmetic operations and explore Numpy's vectorized functions for efficient computation.
- **Indexing and Slicing**: Practice accessing and modifying parts of arrays using advanced indexing techniques.
- **Leveraging Numpy Functions**: Utilize built-in functions to perform tasks such as aggregation, sorting, and conditional selection.

**Helpful Tips:**

- **Always Copy DataFrames Before Modifying**: Prevent unintended side-effects across different exercises by using df.copy() at the start of your function.
- **Refer to Documentation**: When in doubt, the [Pandas documentation](https://pandas.pydata.org/docs/) is an excellent resource for examples and detailed explanations.
- **Incremental Testing**: Test your code in small sections to catch errors early and ensure that each part works as expected.
- **Embrace Vectorization**: Where possible, use vectorized operations instead of loops to write more efficient and concise code.
- **Code Readability**: Keep your code organized and well-commented. This will not only help you debug but also make your work easier to understand later.
- **Debugging Strategy**: If you encounter an error, use print statements or interactive debugging to inspect variables and understand the issue.
