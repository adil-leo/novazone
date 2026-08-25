import json
from pytrends.request import TrendReq

AFFILIATE_TAG = "fastbuyzone-20"

def get_google_trends():
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        kw_list = ["tech gadgets", "home essentials"]
        pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d')
        print("Google Trends connection active.")
    except Exception as e:
        print(f"Trends fallback activated: {e}")

# 40 High-Converting Verified Amazon Products (10 per category)
PRODUCTS_CATALOG = [
    # ⚡ TECH & GADGETS (10)
    {"title": "Logitech MX Master 3S Wireless Mouse", "price": "$99.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61ni3t1ryQL._AC_SL1500_.jpg", "asin": "B09HM94VDS"},
    {"title": "Apple AirTag 4 Pack Item Tracker", "price": "$79.00", "category": "tech", "image": "https://m.media-amazon.com/images/I/7138w4eT3AL._AC_SL1500_.jpg", "asin": "B0932QJ2JZ"},
    {"title": "Anker Soundcore Life Q20 Headphones", "price": "$59.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61SUj2aKoEL._AC_SL1500_.jpg", "asin": "B08HMWZBXC"},
    {"title": "Blink Mini Compact Indoor Smart Camera", "price": "$34.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/51SU6G3YFfL._AC_SL1000_.jpg", "asin": "B07X6C9RMF"},
    {"title": "Anker Magnetic Wireless Power Bank 10k", "price": "$42.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61M5QjS3C4L._AC_SL1500_.jpg", "asin": "B099F558UC"},
    {"title": "Fire TV Stick 4K Streaming Device", "price": "$49.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/71m4-Z4vU0L._AC_SL1500_.jpg", "asin": "B0BP9SNVH9"},
    {"title": "Echo Dot 5th Gen Smart Speaker", "price": "$49.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61MbLLagiVL._AC_SL1000_.jpg", "asin": "B09B8V1LZ3"},
    {"title": "SanDisk 128GB Ultra microSDXC Card", "price": "$15.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/61jB442U1cL._AC_SL1200_.jpg", "asin": "B073JYC4XM"},
    {"title": "TP-Link Kasa Smart Plug Power Strip", "price": "$29.99", "category": "tech", "image": "https://m.media-amazon.com/images/I/513yvC-q8eL._AC_SL1000_.jpg", "asin": "B07B8W2KHZ"},
    {"title": "JBL GO 3 Portable Bluetooth Speaker", "price": "$39.95", "category": "tech", "image": "https://m.media-amazon.com/images/I/61bK2f9A13L._AC_SL1200_.jpg", "asin": "B08339798S"},

    # 🏠 HOME & KITCHEN (10)
    {"title": "Keurig K-Mini Single Serve Coffee Maker", "price": "$59.99", "category": "home", "image": "https://m.media-amazon.com/images/I/71L-QThU3LL._AC_SL1500_.jpg", "asin": "B0748J593C"},
    {"title": "Fullstar Vegetable Chopper & Slicer 4-in-1", "price": "$29.99", "category": "home", "image": "https://m.media-amazon.com/images/I/81x1C63g6tL._AC_SL1500_.jpg", "asin": "B0764HS49D"},
    {"title": "BISSELL Little Green Carpet Cleaner", "price": "$123.59", "category": "home", "image": "https://m.media-amazon.com/images/I/71R3yL2qj1L._AC_SL1500_.jpg", "asin": "B0016HF5GK"},
    {"title": "Ninja Air Fryer 4-Quart Capacity", "price": "$89.99", "category": "home", "image": "https://m.media-amazon.com/images/I/71L9I8A2uYL._AC_SL1500_.jpg", "asin": "B07FDJMC99"},
    {"title": "Stanley Quencher H2.0 FlowState Tumbler", "price": "$45.00", "category": "home", "image": "https://m.media-amazon.com/images/I/61N8Z35JcDL._AC_SL1500_.jpg", "asin": "B0BN3G3J5Z"},
    {"title": "COSORI Air Fryer 5-Quart Compact", "price": "$99.99", "category": "home", "image": "https://m.media-amazon.com/images/I/71c6q3c4fTL._AC_SL1500_.jpg", "asin": "B07GJBBGHG"},
    {"title": "Rubbermaid Brilliance Food Containers 10-Pc", "price": "$22.99", "category": "home", "image": "https://m.media-amazon.com/images/I/81I233W8JFL._AC_SL1500_.jpg", "asin": "B01JCNEJVQ"},
    {"title": "Dash Mini Waffle Maker Machine", "price": "$12.99", "category": "home", "image": "https://m.media-amazon.com/images/I/81y8mX1KmgL._AC_SL1500_.jpg", "asin": "B011M4JFFI"},
    {"title": "Instant Pot Duo 7-in-1 Pressure Cooker", "price": "$79.99", "category": "home", "image": "https://m.media-amazon.com/images/I/71x4zJ8eE5L._AC_SL1500_.jpg", "asin": "B00FLYWNYQ"},
    {"title": "KitchenAid Silicone Oven Mitts Pair", "price": "$18.99", "category": "home", "image": "https://m.media-amazon.com/images/I/81m2c536mBL._AC_SL1500_.jpg", "asin": "B00G33L7E2"},

    # 💄 BEAUTY & CARE (10)
    {"title": "COSRX Snail Mucin 96% Repairing Essence", "price": "$14.99", "category": "beauty", "image": "https://m.media-amazon.com/images/I/51A1b2Vp-LL._AC_SL1500_.jpg", "asin": "B00PBX3L7K"},
    {"title": "CeraVe Hydrating Facial Cleanser 16oz", "price": "$15.49", "category": "beauty", "image": "https://m.media-amazon.com/images/I/7123A8c2PcL._AC_SL1500_.jpg", "asin": "B01MSSDEPK"},
    {"title": "LANEIGE Lip Sleeping Mask Treatment", "price": "$24.00", "category": "beauty", "image": "https://m.media-amazon.com/images/I/61m8uSTh3eL._AC_SL1500_.jpg", "asin": "B07XXPHC33"},
    {"title": "Paula's Choice 2% BHA Liquid Exfoliant", "price": "$35.00", "category": "beauty", "image": "https://m.media-amazon.com/images/I/61k2Yc4-fPL._AC_SL1500_.jpg", "asin": "B00949CTQQ"},
    {"title": "Revlon One-Step Volumizer Hair Dryer", "price": "$39.99", "category": "beauty", "image": "https://m.media-amazon.com/images/I/71S9bVn5sGL._AC_SL1500_.jpg", "asin": "B01LSUQSB0"},
    {"title": "Mighty Patch Original Hydrocolloid Patches", "price": "$11.99", "category": "beauty", "image": "https://m.media-amazon.com/images/I/61kC8bB020L._AC_SL1500_.jpg", "asin": "B074PVTPBW"},
    {"title": "PanOxyl Acne Foaming Wash 10% Benzoyl", "price": "$9.79", "category": "beauty", "image": "https://m.media-amazon.com/images/I/61wL3zC2CqL._AC_SL1500_.jpg", "asin": "B081KL25J8"},
    {"title": "Aquaphor Healing Ointment Skin Protectant", "price": "$13.74", "category": "beauty", "image": "https://m.media-amazon.com/images/I/71fL67O2JdL._AC_SL1500_.jpg", "asin": "B006IB5T4W"},
    {"title": "Neutrogena Hydro Boost Water Gel Cream", "price": "$16.59", "category": "beauty", "image": "https://m.media-amazon.com/images/I/71D0Yn8qR3L._AC_SL1500_.jpg", "asin": "B00NR1YQK4"},
    {"title": "CeraVe AM Facial Moisturizing Lotion SPF 30", "price": "$15.99", "category": "beauty", "image": "https://m.media-amazon.com/images/I/71a2M3u4-3L._AC_SL1500_.jpg", "asin": "B00F97FHAW"},

    # 👕 FASHION (10)
    {"title": "Carhartt Men's Knit Cuffed Beanie Hat", "price": "$19.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/81P8s+wz4BL._AC_SX679_.jpg", "asin": "B002G9UDYG"},
    {"title": "Crocs Unisex Classic Clogs Slip-On", "price": "$39.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/71rMv3YmUML._AC_UX695_.jpg", "asin": "B0014C5S7S"},
    {"title": "Champion Men's Powerblend Fleece Hoodie", "price": "$35.00", "category": "fashion", "image": "https://m.media-amazon.com/images/I/71qJ2x3YUAL._AC_UX679_.jpg", "asin": "B01HI2T070"},
    {"title": "Hanes Men's EcoSmart Fleece Sweatshirt", "price": "$14.00", "category": "fashion", "image": "https://m.media-amazon.com/images/I/81K090iRffL._AC_UX679_.jpg", "asin": "B00JUM2W2O"},
    {"title": "Fruit of the Loom Men's Coolzone Boxers 5-Pk", "price": "$19.98", "category": "fashion", "image": "https://m.media-amazon.com/images/I/81s6aB6bVBL._AC_UX679_.jpg", "asin": "B07C64HQV8"},
    {"title": "Gildan Adult Ultra Cotton T-Shirt 2-Pack", "price": "$12.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/71C7N-M4f2L._AC_UX679_.jpg", "asin": "B0002FHJTG"},
    {"title": "Timberland Men's Passcase Leather Wallet", "price": "$16.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/91r6iF-nFLL._AC_UY695_.jpg", "asin": "B004SME50A"},
    {"title": "Under Armour Men's Tech 2.0 Short-Sleeve", "price": "$19.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/514B3Z-0Z5L._AC_UX679_.jpg", "asin": "B077ZJNZF9"},
    {"title": "Dickies Men's Original 874 Work Pant", "price": "$29.99", "category": "fashion", "image": "https://m.media-amazon.com/images/I/61N-Ue3Q8GL._AC_UY695_.jpg", "asin": "B0001YWLYU"},
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
    print("deals.json updated successfully with 40 products.")

if __name__ == "__main__":
    generate_deals()