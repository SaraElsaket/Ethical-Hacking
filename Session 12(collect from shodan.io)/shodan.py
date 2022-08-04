from shodan import Shodan
from shodan.cli.helpers import get_api_key
api = Shodan(get_api_key())
# Wrap the request in a try/ except block to catch errors
try:
    # Search Shodan
    results = api.search('google.com',1,3,facets="ports")
    # Show the results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        hostname=api.host(result['ip_str'])
        print('IP: {}'.format(result['ip_str']))
        # print(result['port'])
        print('port: {}'.format(result['port']))
        print('country_name: {}'.format(hostname['country_name']))
        print('city: {}'.format(hostname['city']))
        print('domain: {}'.format(result["domains"]))
except Exception as e:
    print (f'Error: {e}')
