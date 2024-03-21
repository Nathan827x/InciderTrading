from GoogleSheets.GoogleSheets import writeToInciderSheet
from scraper import fixDatesForList, getTradesByPublishedDate

# THIS IS JUST FOR TESTING
basic = getTradesByPublishedDate()
print("Basic: ", basic[0])
writeToInciderSheet(basic)

# MOCK_DATA = [['Kevin Hern\nRepublicanHouseOK', 'Texas Instruments Inc\nTXN:US', '2024\n13 Mar', '2024\n13 Feb', 'days\n28', 'Spouse', 'BUY', '1K–15K', '156.85', ''], ['Rick Scott\nRepublicanSenateFL', 'PORT AUTHORITY OF NEW YORK AND NEW JERSEY\nN/A', 'Yesterday\n16:15', '2024\n5 Mar', 'days\n10', 'Self', 'SELL', '500K–1M', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'NEW YORK STATE URBAN DEVELOPMENT CORP\nN/A', 'Yesterday\n16:15', '2024\n5 Mar', 'days\n10', 'Self', 'SELL', '500K–1M', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'EL PASO COUNTY TEXAS\nN/A', 'Yesterday\n16:15', '2024\n4 Mar', 'days\n11', 'Self', 'BUY', '100K–250K', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'EL PASO COUNTY TEXAS\nN/A', 'Yesterday\n16:15', '2024\n4 Mar', 'days\n11', 'Spouse', 'BUY', '500K–1M', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'EL PASO COUNTY TEXAS\nN/A', 'Yesterday\n16:15', '2024\n4 Mar', 'days\n11', 'Self', 'BUY', '500K–1M', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'EL PASO COUNTY TEXAS\nN/A', 'Yesterday\n16:15', '2024\n4 Mar', 'days\n11', 'Spouse', 'BUY', '250K–500K', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'WASHINGTON KING COUNTY\nN/A', 'Yesterday\n16:15', '2024\n15 Feb', 'days\n29', 'Self', 'SELL', '100K–250K', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'PORT AUTHORITY OF NEW YORK AND NEW JERSEY\nN/A', 'Yesterday\n16:15', '2024\n15 Feb', 'days\n29', 'Self', 'SELL', '100K–250K', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'PORT AUTHORITY OF NEW YORK AND NEW JERSEY\nN/A', 'Yesterday\n16:15', '2024\n15 Feb', 'days\n29', 'Spouse', 'SELL', '250K–500K', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'YSLETA INDEPENDENT SCHOOL DISTRICT EL PASO COUNTY TEXAS\nN/A', 'Yesterday\n16:15', '2024\n15 Feb', 'days\n29', 'Spouse', 'SELL', '250K–500K', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'YSLETA INDEPENDENT SCHOOL DISTRICT EL PASO COUNTY TEXAS\nN/A', 'Yesterday\n16:15', '2024\n15 Feb', 'days\n29', 'Self', 'SELL', '500K–1M', 'N/A', ''], ['Rick Scott\nRepublicanSenateFL', 'PORT AUTHORITY OF NEW YORK AND NEW JERSEY\nN/A', 'Yesterday\n16:15', '2024\n15 Feb', 'days\n29', 'Spouse', 'SELL', '250K–500K', 'N/A', '']]

# print("TESING: ", fixDatesForList(MOCK_DATA))

# temp = fixDatesForList(MOCK_DATA)
# for each in range(5):
    
#     print (temp[each])