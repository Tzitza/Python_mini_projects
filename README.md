# Python Mini Projects

Collection of Python applications including a restaurant ordering system and building expense analyzer with data visualization.

## Projects Overview

### 1. Restaurant Ordering System (`Project1.py`)
A command-line restaurant management application that handles menu items, order processing, and payment methods.

**Features:**
- Interactive menu with Greek food items
- Order management by table number
- Multiple payment methods (card/cash)
- Automatic change calculation for cash payments
- Order summary and total price calculation

**Menu Items:**
- Chicken Burger (€4.20)
- Ham Burger (€2.85)
- Green Burger (€4.20)
- Club Sandwich (€10.90)
- Caesar Salad (€6.90)
- Quinoa with Vegetables (€6.30)

### 2. Building Expense Analyzer (`Project2.py`)
A data analysis tool for managing and visualizing building expenses across multiple properties.

**Features:**
- CSV data loading with date filtering
- Statistical analysis (min, max, mean, standard deviation, variance)
- Expense aggregation by building ID
- Monthly/yearly expense trends
- Interactive matplotlib visualizations
- Greek language support

**Visualizations:**
- Bar chart: Total debts per building
- Line chart: Expense trends over time

## Requirements

```
pandas
matplotlib
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-mini-projects.git
cd python-mini-projects
```

2. Install required packages:
```bash
pip install pandas matplotlib
```

## Usage

### Restaurant Ordering System
```bash
python Project1.py
```
Follow the interactive prompts to:
1. Enter table number
2. Select quantities for each menu item
3. Choose payment method
4. Process payment and calculate change if needed

### Building Expense Analyzer
```bash
python Project2.py
```
1. Optionally enter date range for filtering
2. View statistical analysis
3. See expense breakdowns by building and time period
4. Interactive charts will display automatically

**Note:** Make sure `data_forProject2.csv` is in the same directory for the expense analyzer to work properly.

## Data Format

The expense analyzer expects CSV data with the following columns (Greek headers):
- `buildingID`: Building identifier
- `title`: Expense description
- `poso`: Amount (numeric)
- `plirothike`: Payment status (boolean)
- `date_created`: Transaction date

## Sample Data

The repository includes `data_forProject2.csv` with sample building expense data including:
- Utility bills (electricity, water)
- Maintenance services (cleaning, elevator)
- Administrative fees
- Bank charges
- Heating costs

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.


