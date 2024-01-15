![Dashboard](Dashboard.png)

# Analysis of Brazil's Development Indicators

The present project had as objectives both the study of Streamlit and understanding the temporal evolution of Brazil's development indicators during the last decade, in this work the author has wrangled a dataset from The World Bank's DataBank and also developed a dashboard for better visualization of the results found.

In order for one to run this project, follow these steps:

1. Clone this repository;

2. Create a virtual environment named Analysis_BrWDIvenv, on Linux run the following code on the cloned repository folder:  
    python3 -m venv Analysis_BrWDIvenv

3. Activate the virtual environment, on Linux run the following code on the cloned repository folder:  
    source Analysis_BrWDIvenv/bin/activate

4. Install all necessary packages using the command:  
    cat requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | xargs -n 1 python -m pip install

5. Run the Homepage file and enter the command provided on the terminal.

The database utilized in this work was downloaded from:     
https://databank.worldbank.org/reports.aspx?source=2&country=BRA.