# 🛒 Smart Shopping Bill Generator

A lightweight, clean, and interactive console-based billing tool written in Python. This script collects item names, quantities, and prices for three products, dynamically calculates the grand total, and outputs a formatted retail-style receipt.

---

## ✨ Features

- 🧾 **Interactive Prompts:** Effortlessly input names, prices, and quantities for items.
- 🧮 **Instant Calculation:** Computes the grand total automatically with zero fuss.
- 📐 **Clean Receipt Formatting:** Neatly formatted tabular output with aligned columns, dividing borders, and a friendly checkout banner.
- ⚡ **Zero Dependencies:** Runs on pure, standard Python 3 without any external packages.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed on your machine:
```bash
python --version
```
*(Python 3.6 or higher is recommended)*

### Installation & Run

1. **Clone or download** this repository to your local machine.
2. **Open** the project in VS Code.
3. **Execute** the script:
   ```bash
   level_3.16.py
   ```

---

## 🛠️ How It Works

1. **Input Phase:** Takes user inputs via standard console prompts for three separate items.
2. **Computation Phase:** Multiplies each item's unit price by its respective quantity and sums the sub-totals:
   $$\text{Total} = (P_1 \times Q_1) + (P_2 \times Q_2) + (P_3 \times Q_3)$$
3. **Display Phase:** Uses Python's formatted f-strings with alignment specifiers (`<`, `>`, `^`) to render a neat receipt grid.

---

## 💡 Future Enhancements

- [ ] Support dynamic item counts using loops rather than a fixed set of 3 products.
- [ ] Add tax/GST calculation and discount percentages.
- [ ] Implement input validation to gracefully handle non-numeric inputs.
- [ ] Export the generated receipt to a `.txt` or `.pdf` file.

---

## 👤 Author

**Heer K.**  
*Crafted with care and Python ✨*
