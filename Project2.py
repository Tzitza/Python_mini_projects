import pandas as pd
import matplotlib.pyplot as plt

# Φόρτωση δεδομένων από αρχείο CSV
def load_data(start_date=None, end_date=None):
    df = pd.read_csv('data.csv', parse_dates=['Ημερομηνία έκδοσης δαπάνης', 'Ημερομηνία εξόφλησης'], dayfirst=True)

    if start_date is not None and end_date is not None:
        mask = (df['Ημερομηνία έκδοσης δαπάνης'] >= start_date) & (df['Ημερομηνία έκδοσης δαπάνης'] <= end_date)
        df = df.loc[mask]

    return df

# Υπολογισμός στατιστικών στοιχείων
def calculate_statistics(df):
    statistics = {
        'Ελάχιστο': df['Ποσό'].min(),
        'Μέγιστο': df['Ποσό'].max(),
        'Μέσος Όρος': df['Ποσό'].mean(),
        'Τυπική Απόκλιση': df['Ποσό'].std(),
        'Διαφορά': df['Ποσό'].var()
    }
    return statistics

# Υπολογισμός οφειλών ανά πολυκατοικία
def calculate_debts_per_building(df):
    debts_per_building = df.groupby('id κτιρίου')['Ποσό'].sum()
    return debts_per_building

# Υπολογισμός οφειλών ανά μήνα/έτος
def calculate_debts_per_month(df):
    df['Μήνας'] = df['Ημερομηνία έκδοσης δαπάνης'].dt.to_period('M')
    debts_per_month = df.groupby('Μήνας')['Ποσό'].sum()
    return debts_per_month

# Απεικόνιση γραφήματος οφειλών ανά πολυκατοικία
def plot_debts_per_building(debts_per_building):
    plt.figure(figsize=(12, 6))
    debts_per_building.plot(kind='bar')
    plt.title('Σύνολο οφειλών ανά πολυκατοικία')
    plt.xlabel('id κτιρίου')
    plt.ylabel('Σύνολο οφειλών')
    plt.show()

# Απεικόνιση γραφήματος οφειλών ανά μήνα/έτος
def plot_debts_per_month(debts_per_month):
    plt.figure(figsize=(12, 6))
    debts_per_month.plot(kind='line')
    plt.title('Σύνολο οφειλών ανά μήνα/έτος')
    plt.xlabel('Μήνας/Έτος')
    plt.ylabel('Σύνολο οφειλών')
    plt.xticks(rotation=45)
    plt.show()

# Κύριο πρόγραμμα
start_date = input('Εισάγετε ημερομηνία έναρξης (dd/mm/yyyy) ή πατήστε Enter για να αγνοηθεί: ')
end_date = input('Εισάγετε ημερομηνία λήξης (dd/mm/yyyy) ή πατήστε Enter για να αγνοηθεί: ')

if start_date and end_date:
    start_date = pd.to_datetime(start_date, dayfirst=True)
    end_date = pd.to_datetime(end_date, dayfirst=True)

data = load_data(start_date, end_date)
statistics = calculate_statistics(data)
debts_per_building = calculate_debts_per_building(data)
debts_per_month = calculate_debts_per_month(data)

print('Στατιστικά στοιχεία:')
for key, value in statistics.items():
    print(f'{key}: {value}')

print('\nΣύνολο οφειλών ανά πολυκατοικία:')
print(debts_per_building)

print('\nΣύνολο οφειλών ανά μήνα/έτος:')
print(debts_per_month)

plot_debts_per_building(debts_per_building)
plot_debts_per_month(debts_per_month)
