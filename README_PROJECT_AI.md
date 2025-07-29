# ![CI logo]

## Global AI Job Markets And Salary

Welcome,

This is the Code Institute student template for the Data Analytics capstone project. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo. Click the **Use this template** button, then click **Create a new repository**.

1. Copy the URL of your repository to your clipboard.

1. In VS Code, select **File** -> **Open Folder**.

1. Select your `vscode-projects` folder, then click the **Select Folder** button on Windows, or the **Open** button on Mac.

1. From the top menu in VS Code, select **Terminal** > **New Terminal** to open the terminal.

1. In the terminal, type `git clone` followed by the URL of your GitHub repository. Then hit **Enter**. This command will download all the files in your GitHub repository into your vscode-projects folder.

1. In VS Code, select **File** > **Open Folder** again.

1. This time, navigate to and select the folder for the project you just downloaded. Then, click **Select Folder**.

1. A virtual environment is necessary when working with Python projects to ensure each project's dependencies are kept separate from each other. You need to create your virtual environment, also called a venv, and then ensure that it is activated any time you return to your workspace.
   Click the gear icon in the lower left-hand corner of the screen to open the Manage menu and select **Command Palette** to open the VS Code command palette.

1. In the command palette, type: _create environment_ and select **Python: Create Environment…**

1. Choose **Venv** from the dropdown list.

1. Choose the Python version you installed earlier. Currently, we recommend Python 3.12.8

1. **DO NOT** click the box next to `requirements.txt`, as you need to do more steps before you can install your dependencies. Click **OK**.

1. You will see a `.venv` folder appear in the file explorer pane to show that the virtual environment has been created.

1. **Important**: Note that the `.venv` folder is in the `.gitignore` file so that Git won't track it.

1. Return to the terminal by clicking on the TERMINAL tab, or click on the **Terminal** menu and choose **New Terminal** if no terminal is currently open.

1. In the terminal, use the command below to install your dependencies. This may take several minutes.

```console
pip3 install -r requirements.txt
```

1. Open the `jupyter_notebooks` directory, and click on the notebook you want to open.

1. Click the **kernel** button and choose **Python Environments**.

Note that the kernel says `Python 3.12.8` as it inherits from the venv, so it will be Python-3.12.8 if that is what is installed on your PC. To confirm this, you can use the command below in a notebook code cell.

```console
! python --version
```

## Deployment Reminders

- Set the `.python-version` Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version that closest matches what you used in this project.
- The project can be deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the **Deploy** tab, select **GitHub** as the deployment method.
3. Select your repository name and click **Search**. Once it is found, click **Connect**.
4. Select the branch you want to deploy, then click **Deploy Branch**.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button **Open App** at the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the `.slugignore` file.

## AI Job Market Visualizations in Tableau – Key Insights

These Tableau visualizations reveal key trends in AI jobs, covering locations, in-demand skills, salaries, and benefits. They help job seekers and analysts understand the AI employment landscape.

### Story Flow

1. **Where** – AI job locations
2. **What Skills** – Top in-demand skills
3. **Market Trends** – Salary changes over time
4. **Geographic Pay** – Highest paying countries
5. **Experience Impact** – Salary by role level
6. **Company Size Effect** – Salaries in startups vs large firms
7. **Total Compensation** – Salary vs benefits relationship

### Chart Overview & Findings

- **Where the AI Jobs Are (Bubble Chart):** Germany leads with 814 jobs; most countries have 700–800 listings.
- **Top In-Demand Skills (Bar Chart):** Python is top skill (4,450 mentions), followed by SQL (3,407).
- **AI Salary Trends Over Time (Line Chart):** Salaries are stable year-round with no seasonal changes.
- **Country vs Avg Salary (Bar Chart):** Switzerland ($162K) and Denmark ($159K) pay the highest salaries.
- **Experience Pays: Salary by Role (Box Plot):** Executives earn the most (median $168K), followed by senior roles.
- **AI Salaries by Company Size and Experience (Area Chart):** Large companies pay more at all experience levels.
- **Benefits vs Salary (Scatter Plot):** Slight inverse relation; higher salary jobs tend to offer marginally fewer benefits.

Explore these **Tableau visualizations** to gain insights into the AI job market, from locations and skills to compensation.

## AI Skills Word Cloud – A Visual Insight into In-Demand Technologies

This project creates a word cloud to highlight the most in-demand skills in the AI job market. It uses a cleaned dataset of AI-related job listings, with skills like Python, SQL, TensorFlow, and AWS represented as one-hot encoded columns. The script calculates the frequency of each skill and visualizes them using Python’s WordCloud library. A dark background with the professional `cividis` colormap gives the output a clean and modern appearance. The final image, `skills_wordcloud.png`, offers a quick and engaging way to see which technologies are most valued in AI careers.
