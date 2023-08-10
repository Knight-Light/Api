import requests, urllib3, time
from datetime import datetime
from pytz import timezone
from Collected_data import courts
urllib3.disable_warnings()
from Alchemy import session, Casedata

def fetch_status():
        for court in courts:
            try:
                link = court.get('court_link')
                res = requests.get(link, verify=False, allow_redirects=True)
                message = ''
                curr_time = datetime.now(timezone('Asia/Kolkata'))
                if res.status_code // 100 == 2:
                    court['response_status_code'] = res.status_code
                    court['site_status'] = 'Up'
                    court['date_and_time'] = curr_time
                    court['error'] = None
                    print(res.status_code)

                else:
                    court['response_status_code'] = res.status_code
                    court['site_status'] = 'Down'
                    court['date_and_time'] = curr_time
                    court['error'] = None
                    print(res.status_code)
            except Exception as e:
                court['response_status_code'] = res.status_code
                court['site_status'] = 'Down'
                court['date_and_time'] = curr_time
                court['error'] = f"{e}"
                print(res.status_code)




fetch_status()
for court in courts:
    keto = Casedata(**court)
    session.add(keto)
    session.commit()
    session.close()