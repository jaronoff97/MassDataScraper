import requests

url = "http://masslandrecords.com/suffolk/default.aspx"

payload = "ScriptManager1=DocList1%24UpdatePanel%7CDocList1%24GridView_Document%24ctl09%24ButtonRow_Doc.%20%23_7&ScriptManager1_HiddenField=%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3Aeffe2a26%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3A475a4ef5%3A5546a2b%3A497ef277%3Aa43b07eb%3Ad2e10b12%3A37e2e5c9%3A5a682656%3A1d3ed089%3Af9029856%3Ad1a1d569%3B%3B%3BAjaxControlToolkit%2C%20Version%3D3.5.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Aen-US%3A1547e793-5b7e-48fe-8490-03a375b13a33%3A3ac3e789&__VIEWSTATE=&Navigator1%24SearchOptions1%24DocImagesCheck=on&SearchFormEx1%24ACSTextBox_DateFrom=11%2F1%2F2019&SearchFormEx1%24ACSTextBox_DateTo=12%2F31%2F2019&SearchFormEx1%24ACSDropDownList_DocumentType=100017&SearchFormEx1%24ACSDropDownList_Towns=100001&ImageViewer1%24ScrollPos=&ImageViewer1%24ScrollPosChange=&ImageViewer1%24_imgContainerWidth=0&ImageViewer1%24_imgContainerHeight=0&ImageViewer1%24isImageViewerVisible=true&ImageViewer1%24hdnWidgetSize=&ImageViewer1%24DragResizeExtender_ClientState=&CertificateViewer1%24ScrollPos=&CertificateViewer1%24ScrollPosChange=&CertificateViewer1%24_imgContainerWidth=0&CertificateViewer1%24_imgContainerHeight=0&CertificateViewer1%24isImageViewerVisible=true&CertificateViewer1%24hdnWidgetSize=&CertificateViewer1%24DragResizeExtender_ClientState=&DocList1%24ctl03=&DocList1%24ctl05=0&DocDetails1%24PageSize=&DocDetails1%24PageIndex=&DocDetails1%24SortExpression=&BasketCtrl1%24ctl01=&BasketCtrl1%24ctl03=&__EVENTTARGET=DocList1%24GridView_Document%24ctl09%24ButtonRow_Doc.%20%23_7&__EVENTARGUMENT=&__LASTFOCUS=&__ASYNCPOST=true&"
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'X-Requested-With': 'XMLHttpRequest',
  'X-MicrosoftAjax': 'Delta=true',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
  'Accept': '*/*',
  'Origin': 'http://masslandrecords.com',
  'Referer': 'http://masslandrecords.com/suffolk/',
  'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
  'Cookie': 'visid_incap_2183455=x6LfP9tZSJqATKZv4GUuH77BmV4AAAAAQUIPAAAAAAAiPMDcl3GzRd/L6m2Kk1NK; incap_ses_530_2183455=D0b7YK+h4zoOeh6xs/FaB77BmV4AAAAA7ox7V/X7spj8Ux/Rocx91w==; ASP.NET_SessionId=b1vouymswnaxjw55ng05qh45; incap_ses_703_2183455=cLClLy7H7Fz576kNHpvBCSLCmV4AAAAAoTCIv4LAUPL4YIn4LeQI3A==; incap_ses_148_2183455=tbY6UweKUzZIDtW1WtENAuuhnF4AAAAAGgeRG9PQr20DVaaXtIkJ1A==; incap_ses_531_2183455=SMQYJJYmExleTtX9PX9eByyinF4AAAAAyfdAu2x6jKYD05hBrQM3hg==; TS015e6998=01651f8bb53123de81428a103b3065d1fab351345eb7513f7f72a11c6bb6e17cf0e49c59a8e43152dec598ae1271c3d5487eea5b4e90ee4d28e3db1e2158231db56d2b97f4',
  'Content-Type': 'text/plain',
  'Cookie': 'TS015e6998=01651f8bb5e83a32459058ae0f5bbff49672e5b0d9fad678b23debd206dec82d91f14607608315d5c66ae2e9cad2b222b08717afa105928685d2f0e14be3f51583059b1ad9'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
