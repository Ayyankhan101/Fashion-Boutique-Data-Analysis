# Fashion Boutique Data Analysis

This project analyzes the Fashion Boutique dataset to gain insights into sales, product performance, and customer behavior.

## Dataset

The dataset `fashion_boutique_dataset.csv` contains information about products, including:
- `product_id`: Unique identifier for each product.
- `category`: Category of the product (e.g., Outerwear, Tops, Shoes).
- `brand`: Brand of the product.
- `season`: Season for which the product is intended.
- `size`: Size of the product.
- `color`: Color of the product.
- `original_price`: Original price of the product.
- `markdown_percentage`: Discount percentage.
- `current_price`: Current price of the product after the discount.
- `purchase_date`: Date of purchase.
- `stock_quantity`: Quantity of the product in stock.
- `customer_rating`: Rating given by the customer.
- `is_returned`: Boolean indicating if the product was returned.
- `return_reason`: Reason for the return.

## Analysis

The analysis is performed in the `fashion_boutique_analysis.ipynb` Jupyter Notebook. The key steps in the analysis include:

1.  **Data Loading and Cleaning:** Loading the dataset and handling missing values.
2.  **Exploratory Data Analysis (EDA):** Analyzing the data to understand the distributions of variables and the relationships between them.
3.  **Data Visualization:** Creating various plots to visualize the data and insights.
4.  **Return Analysis:** Analyzing the return rates and reasons for returns.

## Streamlit Dashboard

A Streamlit dashboard is created in `streamlit_app.py` to interactively visualize the key findings of the analysis.

### Running the Dashboard

To run the dashboard, you need to have Streamlit installed:

```bash
pip install streamlit
```

Then, run the following command in your terminal:

```bash
streamlit run streamlit_app.py
```
