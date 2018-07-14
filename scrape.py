import requests

for summary_id in range(1, 11386):
    xml = requests.get('https://www.guideline.gov/summaries/downloadcontent/ngc-{}?contentType=xml'.format(summary_id))
    if xml.status_code == 200:
        print('Saving summary {}/11385'.format(summary_id))
        file = open('summaries/ngc-{}.xml'.format(summary_id), "w+")
        file.write(xml.text)
        file.close()
