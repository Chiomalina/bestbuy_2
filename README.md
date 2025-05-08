# 🎉 Best Buy Store Project

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A **command-line** inventory management and shopping system built with ❤️ in Python. This project demonstrates object-oriented design, error handling, and best coding practices.

---

## 🚀 Features

* **🛍️ Product Management**

  * Create products with validation for name, price, and quantity.
  * Automatically activate/deactivate based on stock levels.
* **🏬 Store Composition**

  * Manage a collection of products: add, remove, view active inventory.
  * Place multi-item orders with real-time stock updates.
* **💻 Interactive UI**

  * Intuitive console menu to list products, view totals, make purchases, and exit.
  * Handles edge cases gracefully (invalid input, insufficient stock).
* **✅ Testing & Quality**

  * **Pytest** suite for functionality coverage.
  * **PEP8** style checks via pycodestyle (max line length 79).

---

## 📁 Project Structure

```text
BestBuy/
├── products.py            Product class implementation
├── store.py               Store class implementation
├── main.py                Command-line user interface
├── tests/                 Automated tests
│   ├── test_best_buy.py    Unit tests for Product & Store
│   └── test_style.py       PEP8 style compliance tests
└── README.md              Project documentation
```

---

## ⚡ Quick Start

1. **Clone** the repo:

   ```bash
   git clone https://github.com/your-username/best-buy.git
   cd best-buy
   ```

2. **(Optional)** Create & activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\\Scripts\\activate
   ```

3. **Install** dependencies:

   ```bash
   pip install pytest pycodestyle
   ```

4. **Run** the store interface:

   ```bash
   python main.py
   ```

---

## 🎯 Usage

1. **List Products**: Shows all active items with price and quantity.
2. **Show Total**: Displays total number of items in inventory.
3. **Make Order**: Select items by number, specify quantity, and complete purchase.
4. **Quit**: Exit the application.

*Example:* 🛒

```text
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

---

## 🧪 Running Tests

Run all tests with:

```bash
pytest
```

* **Unit Tests**: Verify `Product` & `Store` behaviors.
* **Style Tests**: Ensure PEP8 compliance.

---

## 📜 License

MIT License.

---

## 👏 Acknowledgments

Developed by **Lina Chioma Anaso** ([chiomalinaanaso@gmail.com](mailto:your.email@example.com)) 🎓

*Happy coding!* \:rocket:
