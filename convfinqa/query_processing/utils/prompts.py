def questions_prompt(
    question: str, summary: str, amt_table: str, filtered_chunks: str
) -> str:
    return f"""
    You know all the financial terms and definitions and have a keen eye for detail.

    Your task is to help answer a question about a financial document by asking follow-up questions to encourage the right train of thought.

    Your follow-up questions should be accurate, unambiguous and answerable with a number or calculation i.e. how much? what what the fee / number?

    Your follow-up questions should lead to the answer to the first question. You should generate as few follow-up questions as you can. 

    You will be given a brief summary of the document, a table of figures, and some context from the document.

    ######################
    -Examples-
    ######################
    Example 1:
    Question: what is the growth rate in net revenue from 2010 to 2011?
    Summary: Entergy Louisiana's net income increased by $242.5 million in 2011 due to an IRS settlement, despite a $199 million regulatory charge. Net revenue analysis for 2011 reflects operating revenues after various expenses.
    Table: <table class='wikitable'><tr><td>1</td><td></td><td>amount ( in millions )</td></tr><tr><td>2</td><td>2010 net revenue</td><td>$ 1043.7</td></tr><tr><td>3</td><td>mark-to-market tax settlement sharing</td><td>-195.9 ( 195.9 )</td></tr><tr><td>4</td><td>retail electric price</td><td>32.5</td></tr><tr><td>5</td><td>volume/weather</td><td>11.6</td></tr><tr><td>6</td><td>other</td><td>-5.7 ( 5.7 )</td></tr><tr><td>7</td><td>2011 net revenue</td><td>$ 886.2</td></tr></table>
    Context: 
    The company reported a notable decrease in net revenue from 2010 to 2011. In 2010, the net revenue was $1,043.7 million, which declined to $886.2 million in 2011. This drop in revenue can be attributed to several key factors outlined below.
    The factors listed above, including the mark-to-market tax settlement sharing and changes in retail electric pricing, significantly contributed to the overall decrease in net revenue from 2010 to 2011.

    Output: 
    1. what was the change in the net revenue from 2010 to 2011?
    2. and how much does this change represent in relation to the net revenue in 2010?
    ######################
    Example 2: 
    Question: assuming the revolver is undrawn , what would the annual fee for the revolver be?
    Summary: The company's revolving credit facility was extended to October 2018, increased to $900 million, and includes various loan facilities with specific margins and amortization requirements.
    Table: <table class='wikitable'><tr><td>1</td><td></td><td>net deferred financing costs ( in $ millions )</td></tr><tr><td>2</td><td>as of december 31 2011</td><td>28</td></tr><tr><td>3</td><td>financing costs deferred ( 1 )</td><td>8</td></tr><tr><td>4</td><td>accelerated amortization due to refinancing activity ( 2 )</td><td>-1 ( 1 )</td></tr><tr><td>5</td><td>amortization</td><td>-5 ( 5 )</td></tr><tr><td>6</td><td>as of december 31 2012</td><td>30</td></tr><tr><td>7</td><td>financing costs deferred ( 3 )</td><td>2</td></tr><tr><td>8</td><td>accelerated amortization due to refinancing activity</td><td>2014</td></tr><tr><td>9</td><td>amortization</td><td>-5 ( 5 )</td></tr><tr><td>10</td><td>as of december 31 2013</td><td>27</td></tr><tr><td>11</td><td>financing costs deferred ( 4 )</td><td>10</td></tr><tr><td>12</td><td>accelerated amortization due to refinancing activity ( 5 )</td><td>-5 ( 5 )</td></tr><tr><td>13</td><td>amortization</td><td>-5 ( 5 )</td></tr><tr><td>14</td><td>as of december 31 2014</td><td>27</td></tr></table>
    Context: 
    The table below outlines the net deferred financing costs from 2011 to 2014. These figures include the impact of deferred financing costs, accelerated amortization due to refinancing activities, and regular amortization. The analysis highlights the changes in financing costs at the end of each year as well as the adjustments made throughout this period.
    The net deferred financing costs remained relatively stable over the period from 2011 to 2014, fluctuating slightly due to deferred financing costs and amortization adjustments. The key drivers behind these changes were refinancing activities, which led to both deferred financing costs and accelerated amortization in several instances. The final value as of December 31, 2014, stands at $27 million, highlighting the overall minimal net change during this period.
    
    Output:
    1. what was the quarterly commitment fee on the unused portion of the revolving credit facility?
    2. and converted to the millions?
    ######################
    Example 3: 
    Question: what was the three year average interest rate for 2007-2009?
    Summary: Royal Caribbean has multiple stock-based compensation plans, including options and restricted stock units, with total expenses of $16.8 million in 2009, up from $5.7 million in 2008. The company uses the Black-Scholes model for option valuation and adjusts forfeiture estimates based on historical data.
    Table: <table class='wikitable'><tr><td>1</td><td></td><td>2009</td><td>2008</td><td>2007</td></tr><tr><td>2</td><td>dividend yield</td><td>0.0% ( 0.0 % )</td><td>1.9% ( 1.9 % )</td><td>1.3% ( 1.3 % )</td></tr><tr><td>3</td><td>expected stock price volatility</td><td>55.0% ( 55.0 % )</td><td>31.4% ( 31.4 % )</td><td>28.0% ( 28.0 % )</td></tr><tr><td>4</td><td>risk-free interest rate</td><td>1.8% ( 1.8 % )</td><td>2.8% ( 2.8 % )</td><td>4.8% ( 4.8 % )</td></tr><tr><td>5</td><td>expected option life</td><td>5 years</td><td>5 years</td><td>5 years</td></tr></table>
    Context: 
    The table below presents key financial metrics, including dividend yield, stock price volatility, risk-free interest rates, and expected option life for the years 2007, 2008, and 2009. These metrics are critical for understanding the company’s financial performance and its associated risks during this period.
    The data reveals a significant decrease in dividend yield over the years, with 2009 showing no yield compared to 1.9% in 2008 and 1.3% in 2007. Stock price volatility increased substantially in 2009, indicating higher market uncertainty, while the risk-free interest rate dropped steadily. Despite these variations, the expected option life remained constant at 5 years across all three periods.

    Output:
    1. combined, what was the risk-free interest rate in 2008 and 2009?
    2. and in 2007?
    3. what was the total for all three years?
    4. so what was the average value during this time?
    ######################
    -Real Data-
    ######################
    Question: {question}
    Summary: {summary}
    Table: {amt_table}
    Context: 
    {filtered_chunks}

    Output:"""


def check_question_prompt(question: str, generated_questions: str) -> str:
    return f"""
    You know all the financial terms and definitions and have a keen eye for detail.

    Your task is to review a set of questions that are aimed at helping someone answer the QUESTION.

    The questions should be accurate, unambiguous and answerable with a number or calculation i.e. how much? what what the fee / number?

    If a question is inaccurate, you should replace it with an accurate question.

    Return the questions, and only the questions.

    ######################
    -Examples-
    ######################
    Example 1:
    QUESTION: what is the growth rate in the fair value of retained interests in 2018 compared to 2017?

    Set of questions:
    1. What is the principal amount of the senior unsecured notes issued in December 2016?
    2. What is the interest rate on these senior unsecured notes?
    3. How often is the interest paid on these notes?
    4. What is the total interest payment per year?
    5. How many years will the interest be paid from the issuance date to the maturity date?
    6. What is the total interest paid over the life of the notes?
    7. What is the total payment (principal + total interest) they will receive on December 2021?

    Output:
    1. what was the principal amount by the interest rate for unsecured notes issued in 2016?
    2. what was the principal amount?
    3. what is the prior product plus the principal value?
    ######################
    -Real Data-
    ######################
    QUESTION: {question}

    Set of questions:
    {generated_questions}

    Output:
    """


def calculations_prompt(
    question: str, generated_questions: str, filtered_chunks: str, amt_table: str
) -> str:
    return f"""
    Your task is to answer the QUESTION where the answer can be found in a table and some document context.

    Your answer should be the python calculation you would do to get to the answer in the format <answer>calculation</answer>.

    Answering the follow-up questions will help with your thought process on how to arrive at the answer to the QUESTION.

    Discard the follow-up questions if they do not help you reach the correct answer.

    Please give the calculation and only the calculation, do not hallucinate.

    Remember, answer the QUESTION, and if you are unsure about your calculation, reply with <answer>None</answer>.

    ######################
    -Examples-
    ######################
    Example 1:
    QUESTION: what is the growth rate in net revenue from 2010 to 2011?

    Table: <table class='wikitable'>
    <tr><td>1</td><td></td><td>amount (in millions)</td></tr>
    <tr><td>2</td><td>mark-to-market tax settlement sharing</td><td>-195.9</td></tr>
    <tr><td>3</td><td>retail electric price</td><td>32.5</td></tr>
    <tr><td>4</td><td>volume/weather</td><td>11.6</td></tr>
    <tr><td>5</td><td>other</td><td>-5.7</td></tr>
    </table>

    Context: 
    The company reported a notable decrease in net revenue from 2010 to 2011. In 2010, the net revenue was $1,043.7 million, which declined to $886.2 million in 2011. This drop in revenue can be attributed to several key factors outlined below.
    The factors listed above, including the mark-to-market tax settlement sharing and changes in retail electric pricing, significantly contributed to the overall decrease in net revenue from 2010 to 2011.

    Follow-up questions:
    1. what was the change in the net revenue from 2010 to 2011? 
    2. and how much does this change represent in relation to the net revenue in 2010?

    Answers to follow-up questions:
    A_0: 886.2 - 1043.7
    A_1: A_0 / 1043.7

    Answer to QUESTION:
    <answer>(886.2 - 1043.7) / 1043.7</answer>
    ######################
    Example 2:
    QUESTION: assuming the revolver is undrawn , what would the annual fee for the revolver be?
    
    Table: <table class='wikitable'><tr><td>1</td><td></td><td>net deferred financing costs ( in $ millions )</td></tr><tr><td>2</td><td>as of december 31 2011</td><td>28</td></tr><tr><td>3</td><td>financing costs deferred ( 1 )</td><td>8</td></tr><tr><td>4</td><td>accelerated amortization due to refinancing activity ( 2 )</td><td>-1 ( 1 )</td></tr><tr><td>5</td><td>amortization</td><td>-5 ( 5 )</td></tr><tr><td>6</td><td>as of december 31 2012</td><td>30</td></tr><tr><td>7</td><td>financing costs deferred ( 3 )</td><td>2</td></tr><tr><td>8</td><td>accelerated amortization due to refinancing activity</td><td>2014</td></tr><tr><td>9</td><td>amortization</td><td>-5 ( 5 )</td></tr><tr><td>10</td><td>as of december 31 2013</td><td>27</td></tr><tr><td>11</td><td>financing costs deferred ( 4 )</td><td>10</td></tr><tr><td>12</td><td>accelerated amortization due to refinancing activity ( 5 )</td><td>-5 ( 5 )</td></tr><tr><td>13</td><td>amortization</td><td>-5 ( 5 )</td></tr><tr><td>14</td><td>as of december 31 2014</td><td>27</td></tr></table>
    
    Context: 
    The table below outlines the net deferred financing costs from 2011 to 2014. These figures include the impact of deferred financing costs, accelerated amortization due to refinancing activities, and regular amortization. The analysis highlights the changes in financing costs at the end of each year as well as the adjustments made throughout this period.
    The net deferred financing costs remained relatively stable over the period from 2011 to 2014, fluctuating slightly due to deferred financing costs and amortization adjustments. The key drivers behind these changes were refinancing activities, which led to both deferred financing costs and accelerated amortization in several instances. The final value as of December 31, 2014, stands at $27 million, highlighting the overall minimal net change during this period.
    
    Follow-up questions:
    1. what was the quarterly commitment fee on the unused portion of the revolving credit facility?
    2. and converted to the millions?

    Answers to follow-up questions:
    A_0: 900 * 0.0025
    A_1: A_0 * 1000000

    Answer to QUESTION:
    <answer>(900 * 0.0025) * 1000000</answer>
    ######################
    Example 3:
    QUESTION: what was the three year average interest rate for 2007-2009?
    
    Table: <table class='wikitable'><tr><td>1</td><td></td><td>2009</td><td>2008</td><td>2007</td></tr><tr><td>2</td><td>dividend yield</td><td>0.0% ( 0.0 % )</td><td>1.9% ( 1.9 % )</td><td>1.3% ( 1.3 % )</td></tr><tr><td>3</td><td>expected stock price volatility</td><td>55.0% ( 55.0 % )</td><td>31.4% ( 31.4 % )</td><td>28.0% ( 28.0 % )</td></tr><tr><td>4</td><td>risk-free interest rate</td><td>1.8% ( 1.8 % )</td><td>2.8% ( 2.8 % )</td><td>4.8% ( 4.8 % )</td></tr><tr><td>5</td><td>expected option life</td><td>5 years</td><td>5 years</td><td>5 years</td></tr></table>
    
    Context:
    The table below presents key financial metrics, including dividend yield, stock price volatility, risk-free interest rates, and expected option life for the years 2007, 2008, and 2009. These metrics are critical for understanding the company’s financial performance and its associated risks during this period.
    The data reveals a significant decrease in dividend yield over the years, with 2009 showing no yield compared to 1.9% in 2008 and 1.3% in 2007. Stock price volatility increased substantially in 2009, indicating higher market uncertainty, while the risk-free interest rate dropped steadily. Despite these variations, the expected option life remained constant at 5 years across all three periods.

    Follow-up questions:
    1. combined, what was the risk-free interest rate in 2008 and 2009?
    2. and in 2007?
    3. what was the total for all three years?
    4. so what was the average value during this time?

    Answers to follow-up questions:
    A_0: 1.8 + 2.8
    A_1: 4.8
    A_2: A_0 + 4.8
    A_3: A_2 / 3 
    
    Answer to QUESTION:
    <answer>((1.8 + 2.8) + 4.8) / 3</answer>
    ######################
    -Real Data-
    ######################
    QUESTION: {question}

    Table: {amt_table}

    Context: {filtered_chunks}

    Follow-up questions:
    {generated_questions}
    """
