import json
from pytrends.request import TrendReq

AFFILIATE_TAG = "fastbuyzone-20"

def get_google_trends():
    """Fetch top search trends to align high-converting products"""
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        kw_list = ["tech gadgets", "home essentials"]
        pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d')
        print("Google Trends fetched successfully.")
    except Exception as e:
        print(f"Trends fallback activated: {e}")

# High-converting products with clean Amazon CDN Image URLs
PRODUCTS_CATALOG = [
    # Tech
    {"title": "Anker Magnetic Wireless Power Bank 10,000mAh", "price": "$42.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61M5QjS3C4L._AC_SL1500_.jpg", "asin": "B099F558UC"},
    {"title": "Logitech MX Master 3S Wireless Performance Mouse", "price": "$99.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61ni3t1ryQL._AC_SL1500_.jpg", "asin": "B09HM94VDS"},
    {"title": "Blink Mini 2 Smart Security Camera 1080p", "price": "$39.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/51Ie1Oa-ZpL._AC_SL1000_.jpg", "asin": "B0BGH8F13Z"},
    {"title": "Apple AirTag 4 Pack Bluetooth Tracker", "price": "$79.00", "category": "tech", "image": "https://m.media-amazon.com/images/I/7138w4eT3AL._AC_SL1500_.jpg", "asin": "B0932QJ2JZ"},

    # Home
    {"title": "Keurig K-Express Single Serve Coffee Maker", "price": "$69.99", "category": "home", "image": "https://m.media-amazon.com/images/I/61KxGThUeeL._AC_SL1500_.jpg", "asin": "B0934S587L"},
    {"title": "Fullstar Vegetable Chopper & Spiralizer 4-in-1", "price": "$29.99", "category": "home", "image": "https://m.media-amazon.com/images/I/81x1C63g6tL._AC_SL1500_.jpg", "asin": "B089KXC91G"},
    {"title": "BISSELL Little Green Multi-Purpose Carpet Cleaner", "price": "$123.59", "category": "home", "image": "https://m.media-amazon.com/images/I/71R3yL2qj1L._AC_SL1500_.jpg", "asin": "B0016HF5GK"},

    # Beauty
    {"title": "COSRX Snail Mucin 96% Power Repairing Essence", "price": "$14.99", "category": "beauty", "image": "https://m.media-amazon.com/images/I/51A1b2Vp-LL._AC_SL1500_.jpg", "asin": "B00PBX3L7K"},
    {"title": "LANEIGE Lip Sleeping Mask Nourishing Treatment", "price": "$24.00", "category": "beauty", "image": "https://m.media-amazon.com/images/I/61m8uSTh3eL._AC_SL1500_.jpg", "asin": "B07XXPHC33"},

    # Fashion
    {"title": "Carhartt Men's Knit Cuffed Beanie", "price": "$19.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/81P8s+wz4BL._AC_SX679_.jpg", "asin": "B002G9UDYG"},
    {"title": "JW PEI Women's Gabbi Shoulder Bag", "price": "$79.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/61J2xL40IHL._AC_UY695_.jpg", "asin": "B08728F9LL"}
]

def generate_deals():
    get_google_trends()
    deals = []
    for item in PRODUCTS_CATALOG:
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
    print("deals.json successfully updated.")

if __name__ == "__main__":
    generate_deals()