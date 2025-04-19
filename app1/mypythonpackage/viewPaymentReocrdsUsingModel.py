import openpyxl
from app1.models import PassbookPaymentHistory
from datetime import datetime


from django.shortcuts import render
from app1.models import PassbookPaymentHistory
from app1.forms import PaymentHistoryFilterForm

def view_payment_records(request):
    form = PaymentHistoryFilterForm(request.GET or None)
    records = PassbookPaymentHistory.objects.all()

    if form.is_valid():
        transaction_id = form.cleaned_data.get('transaction_id')
        account_name = form.cleaned_data.get('account_name')
        payment_mode = form.cleaned_data.get('payment_mode')
        from_date = form.cleaned_data.get('from_date')
        to_date = form.cleaned_data.get('to_date')

        if transaction_id:
            records = records.filter(transaction_id__icontains=transaction_id)
        if account_name:
            records = records.filter(account_name__icontains=account_name)
        if payment_mode:
            records = records.filter(payment_mode__icontains=payment_mode)
        if from_date:
            records = records.filter(date__gte=from_date)
        if to_date:
            records = records.filter(date__lte=to_date)

    context = {
        'form': form,
        'records': records,
    }
    return render(request, 'your_app/view_payment_records.html', context)


def import_payments_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active  # Or select by sheet name

    rows = list(ws.iter_rows(values_only=True))
    headers = [(h.strip() if h else '') for h in rows[0]]
    data_rows = rows[1:]  # data after headers
    for row in data_rows:
        row_dict = dict(zip(headers, row))

        # Handle date parsing
        date_value = row_dict.get('Date')
        if isinstance(date_value, str):
            try:
                date_obj = datetime.strptime(date_value, "%d/%m/%Y").date()
            except Exception:
                date_obj = None
        elif isinstance(date_value, datetime):
            date_obj = date_value.date()
        else:
            date_obj = None

        PassbookPaymentHistory.objects.create(
            date = date_obj,
            transaction_id = row_dict.get('Transaction ID', '') or '',
            account_name = row_dict.get('Account Name', '') or '',
            payment_mode = row_dict.get('Payment Mode', '') or '',
            amount = row_dict.get('Amount') or 0,
            remarks = row_dict.get('Remarks', '') or '',
        )

    print(f"✅ Successfully imported {len(data_rows)} records!")



# Example Usage:
import_payments_from_excel("D:\mohit johri\Monthly_billsAndStatements\paymentsCopy.xlsx")
