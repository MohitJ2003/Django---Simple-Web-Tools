import openpyxl
from django.shortcuts import render

def passbook_payment_history(request):
    # Path to your Excel file (adjust path as needed)
    excel_file_path = 'D:\\mohit johri\\Monthly_billsAndStatements\\paymentsCopy.xlsx'  # Update with correct path

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
    return render(request, 'viewPaymentRecords.html', context)
