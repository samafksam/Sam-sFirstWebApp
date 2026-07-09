import streamlit as st

# Set page layout to wide
st.set_page_config(page_title="Thread & Trend", layout="wide")

# Initialize session state for the shopping cart if it doesn't exist
if "cart" not in st.session_state:
    st.session_state.cart = []

# Sample data for the clothing store
CLOTHES_CATALOG = [
    {
        "id": 1,
        "name": "Classic Denim Jacket",
        "category": "Outerwear",
        "price": 59.99,
        "image": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=500",
        "description": "Timeless denim jacket with a relaxed fit and durable stitching."
    },
    {
        "id": 2,
        "name": "Oversized Cotton Hoodie",
        "category": "Hoodies",
        "price": 45.00,
        "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500",
        "description": "Ultra-soft premium cotton hoodie perfect for everyday lounging."
    },
    {
        "id": 3,
        "name": "Pleated Midi Skirt",
        "category": "Bottoms",
        "price": 39.99,
        "image": "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=500",
        "description": "Elegant flowing pleated skirt with an elastic waistband."
    },
    {
        "id": 4,
        "name": "Minimalist White Sneakers",
        "category": "Shoes",
        "price": 75.00,
        "image": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=500",
        "description": "Clean, crisp leather sneakers that pair perfectly with any outfit."
    }
]

# --- SIDEBAR: Filters & Cart Summary ---
st.sidebar.title("🛒 Shopping Summary")

# Cart calculations
if st.session_state.cart:
    st.sidebar.write(f"**Items in Cart:** {len(st.session_state.cart)}")
    total_price = sum(item['price'] for item in st.session_state.cart)
    st.sidebar.write(f"**Total Price:** ${total_price:.2f}")
    if st.sidebar.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()
else:
    st.sidebar.write("Your cart is empty.")

st.sidebar.markdown("---")
st.sidebar.title("🔍 Filter Catalog")

# Dynamic category filter
categories = ["All"] + list(set(item["category"] for item in CLOTHES_CATALOG))
selected_category = st.sidebar.selectbox("Choose Category", categories)

# --- MAIN CONTENT ---
st.title("🧵 THREAD & TREND")
st.subheader("Fresh Autumn Arrivals — Upgrade your wardrobe with our latest curated collection.")
st.markdown("---")

# Filter the catalog based on sidebar selection
filtered_catalog = CLOTHES_CATALOG
if selected_category != "All":
    filtered_catalog = [item for item in CLOTHES_CATALOG if item["category"] == selected_category]

# Display items in a responsive grid layout using columns
# 4 items max per row
columns_per_row = 4
for i in range(0, len(filtered_catalog), columns_per_row):
    row_items = filtered_catalog[i:i + columns_per_row]
    cols = st.columns(columns_per_row)
    
    for idx, item in enumerate(row_items):
        with cols[idx]:
            # Product card design
            st.image(item["image"], use_container_width=True)
            st.caption(item["category"].upper())
            st.subheader(item["name"])
            st.write(item["description"])
            st.write(f"**${item['price']:.2f}**")
            
            # Interactive add-to-cart button
            if st.button(f"Add to Cart", key=f"btn_{item['id']}"):
                st.session_state.cart.append(item)
                st.toast(f"Added {item['name']} to cart! 🎉")
                st.rerun()
