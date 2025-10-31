# Quick Calculations Guide 💡

The Advanced Python Calculator includes **Quick Calculation Templates** for common real-world calculations. These templates simplify everyday math tasks with easy-to-use commands.

## 🎯 Available Quick Calculations

### 1. Percentage Calculator (`pct`)

Calculate what percentage one number is of another.

**Usage:**
```
➤ Enter operation: pct
Enter value: 200
Enter percentage: 15
✅ 15% of 200 = 30.0
```

**Examples:**
- **Sales tax**: 15% of $50 = $7.50
- **Grade**: 85% of 100 points = 85 points
- **Discount preview**: 25% of $80 = $20 off

---

### 2. Tip Calculator (`tip`)

Calculate tip amount and split the bill between multiple people.

**Usage:**
```
➤ Enter operation: tip
Enter bill amount: 85.50
Enter tip percentage (e.g., 15, 20): 18
Split between how many people? (press Enter for 1): 3

💰 Tip Calculation:
   Bill Amount: $85.50
   Tip (18%): $15.39
   Total: $100.89
   Per Person (÷3): $33.63
```

**Common Tip Percentages:**
- 🌟 Excellent service: 20-25%
- 😊 Good service: 15-20%
- 👍 Standard service: 10-15%

**Features:**
- Automatic tip calculation
- Bill splitting among any number of people
- Clear breakdown of all amounts

---

### 3. Discount Calculator (`disc`)

Calculate final price after applying a discount percentage.

**Usage:**
```
➤ Enter operation: disc
Enter original price: 120
Enter discount percentage: 30

🏷️ Discount Calculation:
   Original Price: $120.00
   Discount (30%): -$36.00
   Final Price: $84.00
   You Save: $36.00
```

**Shopping Examples:**
- **Black Friday**: 50% off $200 = $100 final price
- **Clearance**: 75% off $80 = $20 final price
- **Member discount**: 10% off $150 = $135 final price

---

### 4. Compound Interest Calculator (`ci`)

Calculate investment growth with compound interest.

**Usage:**
```
➤ Enter operation: ci
Enter principal amount: 5000
Enter annual interest rate (%): 5
Enter time period (years): 10
Compounds per year (press Enter for 1): 12

📈 Compound Interest Calculation:
   Principal: $5000.00
   Rate: 5% per year
   Time: 10 years
   Compounds: 12 times/year
   Final Amount: $8235.05
   Interest Earned: $3235.05
```

**Compounding Frequencies:**
- **Annually**: 1 time per year
- **Semi-annually**: 2 times per year
- **Quarterly**: 4 times per year
- **Monthly**: 12 times per year
- **Daily**: 365 times per year

**Investment Examples:**
- **Savings account**: $1000 @ 2% for 5 years
- **Certificate of deposit**: $10000 @ 4% for 3 years
- **Retirement fund**: $50000 @ 7% for 20 years

**Formula Used:**
```
A = P(1 + r/n)^(nt)

Where:
A = Final amount
P = Principal (initial amount)
r = Annual interest rate (as decimal)
n = Number of times interest compounds per year
t = Time in years
```

---

### 5. BMI Calculator (`bmi`)

Calculate Body Mass Index and health category.

**Usage:**
```
➤ Enter operation: bmi
Enter weight (kg): 70
Enter height (meters): 1.75

⚕️ BMI Calculation:
   Weight: 70 kg
   Height: 1.75 m
   BMI: 22.86
   Category: Normal weight
```

**BMI Categories (WHO Standards):**
| BMI Range | Category |
|-----------|----------|
| < 18.5 | Underweight |
| 18.5 - 24.9 | Normal weight |
| 25.0 - 29.9 | Overweight |
| ≥ 30.0 | Obese |

**Conversion Tips:**
- **Pounds to kg**: Divide by 2.205
  - Example: 154 lbs ÷ 2.205 = 70 kg
- **Feet/inches to meters**: 
  - Example: 5'9" = 69 inches × 0.0254 = 1.75 m

**Example Calculations:**
```
Weight: 65 kg, Height: 1.70 m → BMI: 22.5 (Normal)
Weight: 90 kg, Height: 1.80 m → BMI: 27.8 (Overweight)
Weight: 55 kg, Height: 1.65 m → BMI: 20.2 (Normal)
```

---

## 📊 Practical Use Cases

### Shopping Trip
```
1. Calculate discount: disc
   - Original: $150, Discount: 40%
   - Pay: $90

2. Calculate sales tax: pct
   - Subtotal: $90, Tax: 8.5%
   - Tax amount: $7.65
   
3. Final total: $90 + $7.65 = $97.65
```

### Restaurant Bill
```
1. Calculate tip: tip
   - Bill: $67.50
   - Tip: 18%
   - Split: 3 people
   - Each person pays: $26.55
```

### Investment Planning
```
1. Calculate compound interest: ci
   - Principal: $10,000
   - Rate: 6% annually
   - Time: 5 years
   - Compounds: 12 (monthly)
   - Final: $13,488.50
```

### Health Tracking
```
1. Calculate BMI: bmi
   - Weight: 75 kg
   - Height: 1.80 m
   - BMI: 23.15 (Normal weight)
```

---

## 💡 Tips for Quick Calculations

### Percentage Tips
- **Double check**: 10% is easy to calculate mentally (move decimal left once)
- **Combine**: 15% = 10% + 5%
- **Round**: For tips, rounding up is generous!

### Discount Shopping
- **Stack discounts**: Apply multiple discounts sequentially
  - Example: 20% off, then additional 10% off the sale price
- **Compare**: Use calculator to compare different discount offers

### Investment Strategy
- **Rule of 72**: Years to double = 72 ÷ interest rate
  - Example: At 6%, money doubles in ~12 years
- **Compare compounding**: Monthly vs. annual compounds
- **Long-term**: Small differences compound significantly over time

### BMI Considerations
- **Note**: BMI doesn't account for muscle mass
- **Athletes**: May have high BMI but low body fat
- **Trends**: Track changes over time, not just one measurement
- **Consult**: Always consult healthcare professionals for health advice

---

## 🔄 History Tracking

All quick calculations are automatically saved to history:

```
➤ Enter operation: hist

📜 Calculation History:
------------------------------------------------------------
1. [2025-10-31 16:00:00] 15% of 200 = 30.0
2. [2025-10-31 16:01:15] Tip: $85.5 + 18% = 100.89
3. [2025-10-31 16:02:30] Discount: $120.0 - 30% = 84.0
4. [2025-10-31 16:03:45] CI: $5000.0 @ 5% for 10y = 8235.05
5. [2025-10-31 16:05:00] BMI: 70kg / 1.75m = 22.86
------------------------------------------------------------
```

---

## 🎓 Educational Value

These quick calculations help users learn:

1. **Financial Literacy**
   - Understanding interest and compound growth
   - Smart shopping with discount calculations
   - Fair tipping practices

2. **Health Awareness**
   - Understanding BMI and health metrics
   - Setting fitness goals

3. **Practical Math**
   - Real-world applications of percentages
   - Understanding ratios and proportions

---

## 🚀 Pro Tips

### Combine with Memory Functions
```
1. Calculate discount: disc → $84
2. Store in memory: ms → 84
3. Calculate tax on discounted price: pct
4. Recall memory: mr → Use for next calculation
```

### Use with Expression Mode
```
After a quick calculation, use expr mode for follow-up:
1. Tip calculator gives: $100.89 total
2. expr mode: 100.89*30  (if buying for 30 people)
```

### Export History
Save your shopping trip or financial calculations:
```
➤ Enter operation: export
✅ History exported to calculator_history.json
```

---

**Make everyday calculations easier! 💪**
