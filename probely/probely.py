"""

Exercise #1
--------------

Generic risk finding score calculus:
    1 low severity = 1
    1 medium severity = 10
    1 high severity = 40


Only not fixed values count towards this score.

API: https://api.probely.com/targets/ GET

Scan Target: https://api.probely.com/targets/<target-id>/scan_now/ POST # Starts the scan. (<target-id> = RzXFSNHH3qUY)

Scan completed with: https://api.probely.com/targets/RzXFSNHH3qUY/scans/2yvCKSRn4mZx/

"""

import requests


def calc_risk_score(target_id):
    url = 'https://api.probely.com/targets/{}/findings/'.format(target_id)
    headers = (
            {
                'Content-Type': 'application/json',
                'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnQiOiJwcm9iZWx5IiwidXNlcm5hbWUiOiJZVWt3WjhHZFhpUmkiLCJqdGkiOiJRRDdoWUFvdjdTYnIifQ.O53R154sjyE0I5iv_ykFkboz7i5qeQwRRk-Kve9hjIs'
            })

    r = requests.get(url, headers=headers)
    page_total = r.json()['page_total']
    print(page_total)
    risk_sum = 0
    if page_total > 1:
        for x in range(2, page_total+1):
            url = 'https://api.probely.com/targets/RzXFSNHH3qUY/findings/?page={}'.format(str(x))
            page = requests.get(url, headers=headers)
            results = page.json()['results']
            print(url)
            for result in results:
                print(result['severity'])
                risk_sum += result['severity']
            
    else:
        page_total = r.text
        
        #print(page_total)
    print(risk_sum)

calc_risk_score('RzXFSNHH3qUY')

'''
def compareIssues(url):
    r = requests.get(url, headers=headers)
    results = r.json()['results']
    for result in results:
        if '2yvCKSRn4mZx' in result['scans']:
            print(result['state'])


if page_total > 1:
    for x in range(1, page_total+1):
        url = 'https://api.probely.com/targets/RzXFSNHH3qUY/findings/?page={}'.format(str(x))
        print(url)
        compareIssues(url)
else:
    compareIssues(url)
'''
