from Models import TradeEntry
from Constants import ENV_PATH, GOOGLE_FILE_LOCATION, SHEET_FILE_NAME, SHEET_NAME
import gspread
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path(ENV_PATH)
load_dotenv(dotenv_path=dotenv_path)

gc = gspread.service_account(GOOGLE_FILE_LOCATION)

def writeToInciderSheet(trade_entries):
    print("Starting write to Sheets")

    try:
        sheet  = gc.open(os.environ[SHEET_FILE_NAME])

        worksheet = sheet.worksheet(os.environ[SHEET_NAME])

        data = [entry.format() for entry in trade_entries]

        total_rows = len(worksheet.col_values(1))
        data = eliminateRepeatedData(data, worksheet, total_rows)
        
        new_length = total_rows + 1
        worksheet.update("A" + str(new_length), data)

        return True
        
    except:

        print("FAILED TO WRITE TO EXCEL SHEET")

'''
    This is to find where we last left off so we don't have repeated data.
'''
def eliminateRepeatedData(data, worksheet, total_rows):
    print("Finding and fixing repeated data")
    last_element = worksheet.row_values(total_rows)

    index = 0
    while index < range(len(data)) + 1:
        entry = data[index]

        if entry == last_element:
            print("Erasing repeated data")
            return data[index + 1:]

        index += 1
    
    print("No data needed to be erased")
    return data