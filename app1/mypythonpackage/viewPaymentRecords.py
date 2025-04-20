import openpyxl
from django.shortcuts import render
import os
import django
from datetime import datetime
import pandas as pd
from app1.models import Transaction
from decimal import Decimal, InvalidOperation



def passbook_payment_history(request):
    # Path to your Excel file (adjust path as needed)
    excel_file_path = 'D://mohit johri//Monthly_billsAndStatements//paymentsCopy.xlsx'  # Update with correct path

    wb = openpyxl.load_workbook(excel_file_path, data_only=True)

    if "Passbook Payment History" in wb.sheetnames:
        sheet = wb["Passbook Payment History"]
    else:
        return render(request, 'error.html', {"message": "Sheet not found."})

    data = []
    headers = []

    for i, row in enumerate(sheet.iter_rows(values_only=True)):
        if i == 0:
            headers = row
        else:
            if any(row):
                record = dict(zip(headers, row))
                data.append(record)

    # ➡️ ADD this for months and years
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    years = ["2023", "2024", "2025", "2026"]

    context = {
        'records': data,
        'months': months,
        'years': years,
    }

    import_transactions_from_excel(excel_file_path)

    return render(request, 'viewPaymentRecords.html', context)


# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()


def import_transactions_from_excel(file_path):
    print(f"Importing transactions from {file_path}...")
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Convert empty strings to None
    df = df.where(pd.notnull(df), None)
    
    for index, row in df.iterrows():
        try:
            # Parse date and time
            date_str = row['Date']
            time_str = row['Time']
            
            # Handle date
            day, month, year = map(int, date_str.split('/'))
            date_obj = datetime(year, month, day).date()
            
            # Handle time
            if isinstance(time_str, str) and ':' in time_str:
                time_obj = datetime.strptime(time_str, '%H:%M:%S').time()
            else:
                time_obj = datetime.strptime('00:00:00', '%H:%M:%S').time()
            
            # Clean amount field
            raw_amount = str(row['Amount']).replace(',', '').replace('“', '').replace('”', '').strip()
            try:
                amount = Decimal(raw_amount)
            except InvalidOperation:
                print(f"Skipping row {index}: invalid amount '{row['Amount']}'")
                continue  # Skip this row if amount can't be converted

            # Create the transaction
            Transaction.objects.create(
                date=date_obj,
                time=time_obj,
                transaction_details=row['Transaction Details'],
                your_account=row['Your Account'],
                amount=amount,
                upi_ref_no=row['UPI Ref No.'],
                order_id=row['Order ID'],
                remarks=row['Remarks'],
                tags=row['Tags'],
                comment=row['Comment']
            )
        except Exception as e:
            print(f"Error processing row {index}: {e}")
    
    print(f"Successfully imported {len(df)} transactions.")

if __name__ == '__main__':
    excel_file_path = 'D:/mohit johri/Monthly_billsAndStatements/paymentsCopy.xlsx'  # Update path if needed
    import_transactions_from_excel(excel_file_path)
