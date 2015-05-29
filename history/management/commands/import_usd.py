from django.core.management.base import BaseCommand, CommandError
import xlrd
import datetime
import numpy
from decimal import *
from history.models import USDExchangeRate

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print "Importing USD from excel file .."
        book = xlrd.open_workbook("history/files/usd.xls")
        sheet = book.sheet_by_index(0)

        # values controlling depth
        current_row = 5
        num_rows = 11040

        checking_month = 0
        checking_year = 0
        rates = []

        def write_values(rates, month, year):
            if rates:
                avg = Decimal(numpy.mean(rates)).quantize(Decimal('1.00'))
                high = max(rates)
                low = min(rates)
                USDExchangeRate.objects.create(
                    month = month,
                    year = year,
                    average = avg,
                    high = high,
                    low = low,
                )
                # print "{}/{}   AVG: ${}   HIGH: ${}   LOW: ${}  (using {} values for this month)".format(month, year, avg, high, low, len(rates))

        while current_row <= num_rows:

            row = sheet.row(current_row)
            date = xlrd.xldate_as_tuple(row[0].value, book.datemode)
            rate = row[3].value
            if rate:
                rate = Decimal("{}".format(rate)).quantize(Decimal('1.00'))

            year = date[0]
            month = date[1]
            day = date[2]

            if checking_month != month:
                write_values(rates, checking_month, checking_year)
                # clear out rates array, start checking for this month, and push first rate into array
                rates = []
                checking_month = month
                checking_year = year
                if rate:
                    rates.append(rate)
            else:
                if rate:
                    rates.append(rate)

                if current_row == num_rows:
                    write_values(rates, checking_month, checking_year)
            current_row += 1
