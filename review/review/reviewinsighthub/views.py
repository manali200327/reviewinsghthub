

# from django.shortcuts import render
# from django.shortcuts import render
# import requests
# from bs4 import BeautifulSoup
# def index(request):
#     return render(request, 'index.html')


    
 
# def home(request):
#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         # Process the product name (e.g., perform sentiment analysis)
#         return render(request, 'review_summary.html', {'product_name': product_name})
#     return render(request, 'home.html')


# def generate_review_summary(product_name):
#     try:
#         ordinary_url_to_search_on_flipkart = "https://www.flipkart.com/search?q=" + product_name
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
#         first_response = requests.get(ordinary_url_to_search_on_flipkart, headers=headers).text
#         good_looking_first_response = BeautifulSoup(first_response, 'lxml')

#         found_links = good_looking_first_response.find_all('a', attrs={'class': 's1Q9rs'})
#         product_url = "https://www.flipkart.com" + found_links[0].get('href')

#         product_url_response = requests.get(product_url, headers=headers).text
#         good_looking_product_url_response = BeautifulSoup(product_url_response, 'lxml')
#         found_divs = good_looking_product_url_response.find('div', attrs={'class': '_3UZZGt'}).parent
#         review_url = "https://www.flipkart.com" + found_divs.get('href')

#         review_url_response = requests.get(review_url, headers=headers).text
#         good_looking_review_url_response = BeautifulSoup(review_url_response, 'lxml')

#         review_div = good_looking_review_url_response.find_all('div', {'class': '_27M-vq'})
#         total_reviews = []
#         for review in review_div:
#             total_reviews.append(review.select('div')[1].text)

#         review_summary = ' '.join(total_reviews[:3])  # Summarizing first 3 reviews
#         return review_summary
#     except Exception as e:
#         return "Error occurred while fetching reviews: " + str(e)
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'index.html')

def home(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        review_summary = generate_review_summary(product_name)
        return render(request, 'review_summary.html', {'product_name': product_name, 'review_summary': review_summary})
    return render(request, 'home.html')




# import requests
# from bs4 import BeautifulSoup
# import re

# def generate_review_summary(product_name):
#     # Fetch reviews and generate summary
#     review_url = get_review_url(product_name)
#     if review_url:
#         total_pages = get_total_pages(review_url)
#         if total_pages:
#             all_reviews = get_all_reviews(review_url, total_pages)
#             review_summary = "\n".join(all_reviews)  # Concatenate all reviews into a single string
#             return review_summary
#     return "No reviews found."

# def get_review_url(product_name):
#     ordinary_url_to_search_on_flipkart = f"https://www.flipkart.com/search?q={product_name}"
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) AppleWebKit/537.36 (KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
#     first_response = requests.post(ordinary_url_to_search_on_flipkart, headers=headers).text
#     good_looking_first_response = BeautifulSoup(first_response, 'lxml')
#     found_links = good_looking_first_response.find_all('a', attrs={'class': 'CGtC98'})
#     if found_links:
#         return "https://flipkart.com" + found_links[0].get('href')
#     return None

# def get_total_pages(review_url):
#     headers = {"x-user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.92 Safari/537.36 FKUA/website/41/website/Desktop"}
#     review_url_response = requests.get(review_url, headers=headers).text
#     good_looking_review_url_response = BeautifulSoup(review_url_response, 'lxml')
#     total_pages_div = good_looking_review_url_response.find_all('div', {'class': '_1G0WLw'})
#     if total_pages_div:
#         total_pages_span = total_pages_div[0].select('span')
#         if total_pages_span:
#             total_pages_span = total_pages_span[0]
#             total_pages_match = re.search(r'\b(\d+)\b$', total_pages_span.text)
#             if total_pages_match:
#                 total_pages = int(total_pages_match.group(1))
#                 return min(total_pages, 50)  # Limit total pages to 50
#     return None

# def get_all_reviews(review_url, total_pages):
#     all_reviews = []
#     for page in range(1, total_pages + 1):
#         new_url = f"{review_url}&page={page}"
#         headers = {"x-user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.92 Safari/537.36 FKUA/website/41/website/Desktop"}
#         response = requests.get(new_url, headers=headers).text
#         good_looking_response = BeautifulSoup(response, 'lxml')
#         review_divs = good_looking_response.find_all('div', {'class': 'ZmyHeo'})
#         for review_div in review_divs:
#             review_text = review_div.select('div')[1].text.strip()
#             all_reviews.append(review_text)
#     return all_reviews

# # This function is not called in the script but is provided for use in Django views
# def generate_review_summary_for_product(request):
#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         review_summary = generate_review_summary(product_name)
#         return render(request, 'review_summary.html', {'product_name': product_name, 'review_summary': review_summary})
#     return render(request, 'home.html')
import requests
from bs4 import BeautifulSoup
import re

def get_review_url(product_name):
    try:
        url = f"https://www.flipkart.com/search?q={product_name}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) AppleWebKit/537.36 (KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        link = soup.find('a', class_='s1Q9rs')
        if link:
            return "https://www.flipkart.com" + link.get('href')
        else:
            raise Exception("No product found on Flipkart")
    except Exception as e:
        print(f"Error in get_review_url: {e}")
        return None

def get_total_pages(review_url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(review_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        total_pages_span = soup.find('span', class_='_2KpZ6l')
        if total_pages_span:
            total_pages = int(re.search(r'Page 1 of (\d+)', total_pages_span.text).group(1))
            return min(total_pages, 50)  # Limit total pages to 50
    except Exception as e:
        print(f"Error in get_total_pages: {e}")
    return None

def get_all_reviews(review_url, total_pages):
    all_reviews = []
    try:
        for page in range(1, total_pages + 1):
            url = f"{review_url}&page={page}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            review_divs = soup.find_all('div', class_='_3LWZlK')
            for review_div in review_divs:
                review_text = review_div.find('div', class_='t-ZTKy').text.strip()
                all_reviews.append(review_text)
        return all_reviews
    except Exception as e:
        print(f"Error in get_all_reviews: {e}")
        return None

def generate_review_summary(product_name):
    try:
        review_url = get_review_url(product_name)
        if review_url:
            total_pages = get_total_pages(review_url)
            if total_pages:
                all_reviews = get_all_reviews(review_url, total_pages)
                if all_reviews:
                    review_summary = "\n".join(all_reviews)
                    return review_summary
    except Exception as e:
        print(f"Error in generate_review_summary: {e}")
    return "No reviews found."
