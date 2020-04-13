import csv
import json
import requests

stores_urls = [
    # put links to stores in quotes separated by commas here
]

def scrape_store(store_urls):
    filename = "shopify_store_products.csv"
    print (filename)
    create_file(filename)
    for url in store_urls:
        base_url = url
        incomplete_url = base_url + 'products.json?page='
        n = 1 
        while True:
            page_url = incomplete_url + str(n)
            try:
                write_values_from_url(page_url, filename,base_url)
                n += 1
            except:
                print ("Done")
                break


def create_file(filename):
    f = open( filename, "w")
    f.write ("vendor *&^ title *&^ link *&^ Description *&^ Price*&^ images")
    f.close
    return filename
    
def write_values_from_url(url,file,base_url):

    resp = requests.get(url)
    json = resp.json()
    products =json['products']
    if len(products) ==0:
        raise

    f = open("shopify_store_products.csv", "a")
    for product in products:
        line = ''
        line= line +  (product['vendor'] )
        line= line + ("*&^")
        line= line +  (product['title'] )
        line= line + ("*&^")
        line= line +  base_url+ '/products/' + (product['handle'])
        line= line + ("*&^")
        line= line +  (product['body_html']).replace('\n','')
        line= line + ("*&^")
        line= line +  (product['variants'][0]['price'])
        line= line + ("*&^")
        for image in product['images']:
            line= line +  (image['src'])
            line= line + ("*&^")
        f.write('\n')
        f.write(line)
        line = ''
    f.close()

scrape_store(stores_urls)





