import json
import requests
from bs4 import BeautifulSoup

AFFILIATE_TAG = "fastbuyzone-20"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Targeted high-converting Amazon products across categories
PRODUCTS_DATA = [
    # Tech
    {"title": "Anker Magnetic Wireless Power Bank", "price": "$39.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61m3J4m0ZEL._AC_SL1500_.jpg", "asin": "B099F558UC"},
    {"title": "Logitech MX Master 3S Wireless Mouse", "price": "$99.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61ni3t1ryQL._AC_SL1500_.jpg", "asin": "B09HM94VDS"},
    {"title": "Blink Mini 2 Smart Security Camera", "price": "$39.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/51Ie1Oa-ZpL._AC_SL1000_.jpg", "asin": "B0BGH8F13Z"},
    
    # Home
    {"title": "Keurig K-Express Coffee Maker", "price": "$69.99", "category": "home", "image": "https://m.media-amazon.com/images/I/61KxGThUeeL._AC_SL1500_.jpg", "asin": "B0934S587L"},
    {"title": "COSRX Snail Mucin 96% Power Essence", "price": "$14.99", "category": "beauty", "image": "https://m.media-amazon.com/images/I/51A1b2Vp-LL._AC_SL1500_.jpg", "asin": "B00PBX3L7K"},
    {"title": "Fullstar Vegetable Chopper & Slicer", "price": "$29.99", "category": "home", "image": "https://m.media-amazon.com/images/I/81x1C63g6tL._AC_SL1500_.jpg", "asin": "B089KXC91G"},

    # Beauty
    {"title": "Laneige Lip Sleeping Mask", "price": "$24.00", "category": "beauty", "image": "https://m.media-amazon.com/images/I/61m8uSTh3eL._AC_SL1500_.jpg", "asin": "B07XXPHC33"},
    {"title": "CeraVe Hydrating Facial Cleanser", "price": "$15.49", "category": "beauty", "image": "https://m.media-amazon.com/images/I/71R3yL2qj1L._AC_SL1500_.jpg", "asin": "B01MSSDEPK"},

    # Fashion
    {"title": "Carhartt Men's Knit Cuffed Beanie", "price": "$19.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/81P8s+wz4BL._AC_SX679_.jpg", "asin": "B002G9UDYG"},
    {"title": "JW PEI Women's Gabbi Shoulder Bag", "price": "$79.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/61J2xL40IHL._AC_UY695_.jpg", "asin": "B08728F9LL"}
]

def generate_deals():
    deals = []
    for item in PRODUCTS_DATA:
        # Build clean affiliate link
        affiliate_url = f"https://www.amazon.com/dp/{item['asin']}?tag={AFFILIATE_TAG}"
        deals.append({
            "title": item["title"],
            "price": item["price"],
            "category": item["category"],
            "image": item["image"],
            "link": affiliate_url
        })
    
    with open("deals.json", "w") as f:
        json.dump(deals, f, indent=2)
    print("deals.json updated successfully with tag: " + AFFILIATE_TAG)

if __name__ == "__main__":
    generate_deals()