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

        # TODO: We need to check at what part of the data is new. We then split the data arr and then we can write the rest of it.
        worksheet.update("A2", data)

        return True
        
    except:

        print("FAILED TO WRITE TO EXCEL SHEET")
    # print(sheet.worksheets())

