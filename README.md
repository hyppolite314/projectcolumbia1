# *Loan Portfolio Analyzer*
Welcome to my repository of FinTech projects. This specific project is an analyzer for loan portfolios. With this tool, investors can:
<p>
**quickly sift through a portfolio of loans**
<br>
**extract key indicators of the portfolio**
<br>
**decide whether it fits their investment strategy**</p>

---

## Technologies

Required programs, libraries, systems, and overall dependencies:

Python (version 3.0 or later)
<br>
`Pathlib`
<br>
`csv`

---

## Installation Guide

`pip install Pathlib`

---

## Usage

Determine number of loans in the portfolio

```python

number_of_loans = len(loan_costs)
print(f'The number of loans in this portfolio is {number_of_loans}')           
```

Determine the present value of a loan product

```python
annual_discount_rate = 0.20
present_value = (future_val) / (1 + annual_discount_rate/12) ** remaining_months
print(f'The FAIR VALUE for this loan is {present_value:.3f}')
```

Determine the present value of a loan product

```python
csvpath = Path("ENTER FILEPATH HERE")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())
```

## Updates Since Last *Push*
<p>
**Updated coding for finding sum of loans**
<br>
**Improved `csv coding to save csv file**
<br>
**Added coding to limit float outputs to 3 decimal places for a cleaner look**</p>

---

## Contributors

Reginald Hyppolite
https://www.linkedin.com/in/reginald-hyppolite-nyc/

A big THANK YOU to all the great TAs and Professor Vinicio DeSola

---

## Licenses

N/A -- Free open.ware