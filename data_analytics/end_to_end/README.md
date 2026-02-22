# A/B Test Analysis – Landing Page Conversion
## Project Overview

This project analyzes the impact of a new landing page on user conversion using an end-to-end A/B testing framework. The objective was to determine whether the new page improves conversion rates compared to the existing version and to provide a data-driven business recommendation.

The analysis includes data cleaning, experiment validation, statistical hypothesis testing, and an interactive dashboard for business stakeholders.

### Business Problem

A company introduced a new landing page and conducted an A/B experiment:

Control group → Old landing page

Treatment group → New landing page

The key question:

Does the new landing page increase the conversion rate?

Dataset

~294,000 user records

Fields:

user_id

timestamp

group (control / treatment)

landing_page (old_page / new_page)

converted (1 = converted, 0 = not converted)

### Project Workflow
1. Data Cleaning & Validation:

Removed duplicate users

Dropped mismatched records

Control users seeing new page

Treatment users seeing old page

Final dataset: ~290K users

Verified experiment balance between groups

2. Exploratory Analysis:

Overall conversion rate

Conversion rate by group

User distribution by group

Conversion trends over time

3. Hypothesis Testing

Null Hypothesis (H₀):
New page conversion ≤ Old page conversion

Alternative Hypothesis (H₁):
New page conversion > Old page conversion

### Statistical methods:

Two-proportion Z-test

95% Confidence Interval

Results

Control Conversion: 12.03%

Treatment Conversion: 11.87%

Lift: -1.30%

P-value: 0.195

Confidence Interval includes 0

Conclusion
The difference is not statistically significant.

### Business Recommendation

The new landing page does not improve conversion and slightly underperforms.
Recommendation: Retain the current (old) landing page.

### Dashboard (Power BI)

The interactive dashboard includes:

KPI Cards

Total Users

Overall Conversion Rate

Control vs Treatment Conversion

Lift %

Conversion rate trend over time

Conversion comparison by group

100% stacked Converted vs Not Converted

User distribution by group

Final business insight

![Alt text](dashboard.png)

### Tools & Technologies

Python

Pandas, NumPy

Matplotlib / Seaborn

SciPy (Z-test)

Jupyter Notebook

Power BI

### Key Skills Demonstrated

Data Cleaning & Validation

Experiment Integrity Checks

A/B Testing & Hypothesis Testing

Statistical Analysis (Z-test, Confidence Interval)

Data Visualization

Business Insight & Decision Making

Dashboard Development


### Key Insight

Despite a large sample size (~290K users), the new landing page did not produce a statistically significant improvement and resulted in a slight negative lift.

### Future Improvements

Segment analysis (device, time, user behavior)

Bayesian A/B testing approach

Statistical power analysis

Experiment duration optimization

### Author

Alive Peterson
Github:@Alive-Peterson
