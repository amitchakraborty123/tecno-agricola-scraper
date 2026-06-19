# 🌾 Tecno Agricola Products Data Scraper

A Python web scraper that extracts product data from [tecnoagricolamodena.it](https://www.tecnoagricolamodena.it/) — built for fast, reliable, and repeatable data collection into clean CSV files.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📋 Overview

This script scrapes product listings — either from **all categories** or a **single category** of your choice — and exports the results to a structured CSV file. It's built with session reuse, automatic retries, and clean logging so it runs reliably even on large catalogs.

## 📦 What You Get

Every run produces a CSV file with the following data points:

| Field | Description |
|---|---|
| `Link` | Direct URL to the product page |
| `Name` | Product title |
| `Price` | Listed price |
| `Image` | Product image URL |
| `Availability` | Stock status (Available / Not available) |

## 🛠️ Tech Stack

- **Language:** Python ≥ 3.10
- **Core libraries:** `requests`, `beautifulsoup4`, `lxml`, `pandas`
- **Dev tools:** `pytest` (testing), `ruff` + `black` (linting & formatting)

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/amitchakraborty123/tecno-agricola-scraper.git
cd tecno-agricola-scraper
```

**2. Install dependencies**
```bash
pip install .
```
Or,
```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the scraper from the `src` folder:

```bash
cd src
python scraper.py
```

You'll be prompted to choose a scraping mode:

```
What do you want to scrape?
  1. All Categories
  2. Single Category
```

- Enter **`1`** to scrape every category on the site automatically.
- Enter **`2`** to scrape a single category — you'll be asked to paste its URL.

The script then walks through every page of results and saves all collected data to `output/products.csv`.

## 📸 Screenshots

| Step | Preview |
|---|---|
| Library installation | `screenshots/installation-libraries.png` |
| Target website | `screenshots/tecno-agricola-website.png` |
| Scraping all categories | `screenshots/all-categories-scrape.png` |
| Scraping a single category | `screenshots/single-category-scrape.png` |

> Add your actual screenshots to the `screenshots/` folder using these filenames, and they'll render automatically here.

## 📁 Project Structure

```
tecno-agricola-scraper/
│
├── src/
│   ├── scraper.py
│   ├── config.py
│   └── utils.py
│
├── tests/
│   ├── test_scraper.py
│   └── fixtures/
│       └── sample_product.html
│
├── screenshots/
│   ├── installation-libraries.png
│   ├── tecno-agricola-website.png
│   ├── all-categories-scrape.png
│   └── single-category-scrape.png
│
├── sample_output/
│   └── Products_Data.csv
│
├── output/
│   └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── .env.example
└── LICENSE
```

## ⚠️ Disclaimer

This tool is intended for educational and personal data-analysis purposes. Always review a website's `robots.txt` and Terms of Service before scraping, and use reasonable request delays to avoid overloading the target server.

## 📄 License

Distributed under the [MIT License](https://choosealicense.com/licenses/mit/).

## 👤 About Me

I'm a Data Analyst passionate about turning raw web data into clean, usable datasets.

📧 **Email:** me.amitchakravarti@gmail.com
💻 **GitHub:** [@amitchakraborty123](https://github.com/amitchakraborty123)
🔗 **LinkedIn:** [Amit Chakravarti](https://www.linkedin.com/in/mr-amit-chakraborty/)

---

⭐ If you found this project useful, consider giving it a star!
