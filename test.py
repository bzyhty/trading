import pdapi
con = pdblp.BCon(debug=True, port=8194)
con.start()
test = con.bdh('SPY US Equity', 'PX_LAST',
                '20150629', '20150630')
