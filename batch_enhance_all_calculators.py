#!/usr/bin/env python3
"""
Comprehensive Calculator Enhancement Script for CalcuPrime
Generates fully enhanced calculators with 1000+ words of educational content
"""

import os
import re

# HTML Template
def generate_enhanced_calculator(filename, title, description, keywords, inputs_html, results_html, js_function, content_html):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <title>{title} | CalcuPrime</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="canonical" href="https://calcuprime.com/calculators/{filename}.html">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <nav class="nav container">
            <a href="../index.html" class="logo"><span class="logo-icon">⚡</span><span class="logo-text">CalcuPrime</span></a>
            <ul class="nav-menu"><li><a href="../index.html">Home</a></li></ul>
        </nav>
    </header>
    <main class="calculator-container">
        <div class="calculator-header">
            <h1 class="calculator-title">{title}</h1>
            <p class="calculator-description">{description.split('.')[0]}</p>
        </div>
        <div class="calculator-wrapper">
            <div class="calculator-inputs">
                <h3>Calculator Input</h3>
{inputs_html}
                <button onclick="calculate()" class="btn-calculate">Calculate</button>
            </div>
            <div class="calculator-results">
                <h3>Results</h3>
{results_html}
            </div>
        </div>
        <div class="content-section">
{content_html}
        </div>
    </main>
    <footer class="footer"><div class="container"><div class="footer-bottom"><p>&copy; 2024 CalcuPrime. All rights reserved.</p></div></div></footer>
    <script src="../js/main.js"></script>
    <script>
{js_function}
        document.querySelectorAll('.form-input').forEach(input => input.addEventListener('input', calculate));
        window.addEventListener('load', calculate);
    </script>
</body>
</html>'''

# Calculator Specifications - All 28 remaining calculators
CALCULATORS = {
    "credit-card-calculator": {
        "title": "Credit Card Calculator",
        "description": "Calculate credit card payoff time, total interest, and monthly payments. Plan your debt elimination strategy.",
        "keywords": "credit card calculator, payoff calculator, credit card payoff, interest calculator, debt payoff",
        "inputs": '''                <div class="form-group">
                    <label for="balance" class="form-label">Credit Card Balance ($)</label>
                    <input type="number" id="balance" class="form-input" value="5000" min="0" step="100">
                </div>
                <div class="form-group">
                    <label for="apr" class="form-label">Annual Interest Rate (APR %)</label>
                    <input type="number" id="apr" class="form-input" value="18" min="0" max="35" step="0.1">
                </div>
                <div class="form-group">
                    <label for="payment" class="form-label">Monthly Payment ($)</label>
                    <input type="number" id="payment" class="form-input" value="150" min="0" step="10">
                </div>''',
        "results": '''                <div class="result-item">
                    <div class="result-label">Payoff Time</div>
                    <div class="result-value" id="payoffTime" style="font-size: 2.5rem; color: #ef4444;">0 months</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Total Interest Paid</div>
                    <div class="result-value" id="totalInterest">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Total Amount Paid</div>
                    <div class="result-value" id="totalPaid">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Monthly Interest Charge</div>
                    <div class="result-value" id="monthlyInterest">$0</div>
                </div>''',
        "js": '''        function calculate() {
            const balance = parseFloat(document.getElementById('balance').value) || 0;
            const apr = parseFloat(document.getElementById('apr').value) / 100 || 0;
            const payment = parseFloat(document.getElementById('payment').value) || 0;

            const monthlyRate = apr / 12;
            const monthlyInterest = balance * monthlyRate;

            if (payment <= monthlyInterest) {
                document.getElementById('payoffTime').textContent = 'Never (payment too small)';
                document.getElementById('totalInterest').textContent = 'N/A';
                document.getElementById('totalPaid').textContent = 'N/A';
            } else {
                const months = Math.ceil(Math.log(payment / (payment - balance * monthlyRate)) / Math.log(1 + monthlyRate));
                const totalPaid = payment * months;
                const totalInterest = totalPaid - balance;

                document.getElementById('payoffTime').textContent = months + ' months (' + Math.floor(months/12) + ' years, ' + (months%12) + ' months)';
                document.getElementById('totalInterest').textContent = '$' + totalInterest.toLocaleString('en-US', {minimumFractionDigits: 2});
                document.getElementById('totalPaid').textContent = '$' + totalPaid.toLocaleString('en-US', {minimumFractionDigits: 2});
            }

            document.getElementById('monthlyInterest').textContent = '$' + monthlyInterest.toLocaleString('en-US', {minimumFractionDigits: 2});
        }''',
        "content": '''            <h2>Understanding Credit Card Debt</h2>
            <p>Credit card debt affects millions of Americans, with the average household carrying over $6,000 in credit card balances. High interest rates, often 15-25% APR, make credit cards one of the most expensive forms of debt. Understanding how credit card interest compounds and how payments are applied is crucial for developing an effective payoff strategy.</p>

            <h2>How Credit Card Interest Works</h2>
            <p>Credit card companies calculate interest using your Annual Percentage Rate (APR) divided by 365 (daily periodic rate) or 12 (monthly periodic rate). Interest compounds daily on most cards, meaning you pay interest on your interest. This compounding effect causes balances to grow quickly if you only make minimum payments.</p>

            <p>For example, a $5,000 balance at 18% APR costs approximately $75 per month in interest charges. If you only pay the minimum (usually 2-3% of balance), most of your payment goes toward interest, barely touching the principal. This is why $5,000 in credit card debt can take 15+ years to pay off with minimum payments, costing thousands in interest.</p>

            <h2>The Minimum Payment Trap</h2>
            <p>Credit card companies typically calculate minimum payments as the greater of $25-35 or 2-3% of your balance. While tempting to pay only this amount, minimum payments keep you in debt for years or decades. Consider these examples:</p>

            <ul>
                <li>$5,000 balance at 18% APR with 2% minimum payments: 25 years to pay off, $6,923 in interest</li>
                <li>Same balance with $150 monthly payment: 4 years to pay off, $1,978 in interest</li>
                <li>Same balance with $250 monthly payment: 2 years to pay off, $1,012 in interest</li>
            </ul>

            <p>Even modest increases in monthly payments dramatically reduce both payoff time and total interest paid.</p>

            <h2>Effective Credit Card Payoff Strategies</h2>
            <p><strong>Debt Avalanche Method:</strong> Pay minimum payments on all cards except the one with the highest interest rate. Direct all extra money to the highest-rate card. Once paid off, roll that payment to the next highest-rate card. This method saves the most money on interest.</p>

            <p><strong>Debt Snowball Method:</strong> Pay minimums on all cards except the one with the smallest balance. Pay off the smallest balance first, regardless of interest rate. Once paid off, roll that payment to the next smallest balance. This method provides psychological wins that help maintain momentum, though it may cost slightly more in interest.</p>

            <p><strong>Balance Transfer Strategy:</strong> Transfer high-interest balances to a card offering 0% APR for 12-21 months. Pay aggressively during the promotional period to eliminate debt interest-free. Watch for balance transfer fees (typically 3-5%) and ensure you can pay off the balance before the promotional rate expires.</p>

            <p><strong>Debt Consolidation Loan:</strong> Take a personal loan at a lower rate (typically 7-15%) to pay off high-interest credit cards. This simplifies payments and reduces interest, but requires discipline to avoid running up new credit card balances.</p>

            <h2>How to Accelerate Debt Payoff</h2>
            <p><strong>Stop New Charges:</strong> The single most important step is stopping new charges on cards you're paying off. Consider freezing cards in ice or removing them from digital wallets to create friction against impulse purchases.</p>

            <p><strong>Find Extra Money:</strong> Review your budget for savings opportunities. Common sources include eating out less, canceling unused subscriptions, reducing entertainment spending, or taking a side gig. Even an extra $50-100 monthly makes a significant difference over time.</p>

            <p><strong>Automate Payments:</strong> Set up automatic payments for more than the minimum to ensure consistency and avoid late fees. Late payments not only incur $25-40 fees but can trigger penalty APRs up to 29.99%.</p>

            <p><strong>Use Windfalls Wisely:</strong> Direct tax refunds, work bonuses, or other unexpected money toward credit card debt. These lump sum payments dramatically reduce principal and future interest charges.</p>

            <p><strong>Negotiate Lower Rates:</strong> Call credit card companies and request lower interest rates, especially if you have good payment history. Many cardholders successfully negotiate 2-5% rate reductions, saving hundreds in interest.</p>

            <h2>Understanding Your Credit Card Statement</h2>
            <p>Your monthly statement contains critical information for managing debt:</p>

            <p><strong>New Balance:</strong> Total amount owed including new purchases, interest, and fees.</p>

            <p><strong>Minimum Payment Due:</strong> The least you must pay to avoid late fees and maintain account standing. Never pay just this amount if you can afford more.</p>

            <p><strong>Payment Due Date:</strong> Missing this date triggers late fees and potentially penalty APR. Set reminders or automate payments.</p>

            <p><strong>Interest Charged:</strong> The cost of carrying a balance. This number should motivate you to pay more than the minimum.</p>

            <p><strong>Available Credit:</strong> Your remaining credit line. Using more than 30% of available credit hurts your credit score.</p>

            <h2>Impact on Credit Score</h2>
            <p>Credit card debt affects your credit score in multiple ways:</p>

            <p><strong>Credit Utilization (30% of score):</strong> The ratio of credit card balances to credit limits. Keeping utilization below 30% is good; below 10% is excellent. High balances relative to limits significantly damage scores.</p>

            <p><strong>Payment History (35% of score):</strong> Late payments severely impact your score and remain on your credit report for seven years. Set up auto-pay to never miss a payment.</p>

            <p><strong>Account Age (15% of score):</strong> Keep older credit card accounts open (even if unused) to maintain average account age, which helps your score.</p>

            <h2>When to Seek Professional Help</h2>
            <p>Consider professional assistance if you:</p>
            <ul>
                <li>Can only afford minimum payments on multiple cards</li>
                <li>Have been contacted by collection agencies</li>
                <li>Are considering bankruptcy</li>
                <li>Face wage garnishment or legal action</li>
                <li>Have tried unsuccessfully to manage debt for 2+ years</li>
            </ul>

            <p>Non-profit credit counseling agencies (look for NFCC members) offer free consultations and can set up debt management plans that negotiate lower interest rates with creditors. Avoid for-profit debt settlement companies that charge high fees and can damage your credit.</p>

            <h2>Life After Credit Card Debt</h2>
            <p>Once you've paid off credit cards, redirect those payment amounts to building an emergency fund (3-6 months of expenses), saving for retirement, or other financial goals. Consider keeping one or two cards active with small recurring charges (like subscriptions) that you pay in full monthly to maintain credit history without carrying debt.</p>

            <p>The average American pays over $1,000 annually in credit card interest. Eliminating this expense frees up significant money for building wealth, taking vacations, or achieving other financial goals. The discipline developed paying off debt serves you well in all future financial decisions.</p>'''
    },

    "lease-calculator": {
        "title": "Lease Calculator",
        "description": "Calculate car lease payments, total cost, and compare leasing vs buying. Make informed vehicle financing decisions.",
        "keywords": "lease calculator, car lease, auto lease, lease payment calculator, vehicle lease",
        "inputs": '''                <div class="form-group">
                    <label for="msrp" class="form-label">Vehicle MSRP ($)</label>
                    <input type="number" id="msrp" class="form-input" value="35000" min="0" step="1000">
                </div>
                <div class="form-group">
                    <label for="salePrice" class="form-label">Negotiated Price ($)</label>
                    <input type="number" id="salePrice" class="form-input" value="33000" min="0" step="500">
                </div>
                <div class="form-group">
                    <label for="downPayment" class="form-label">Down Payment ($)</label>
                    <input type="number" id="downPayment" class="form-input" value="3000" min="0" step="500">
                </div>
                <div class="form-group">
                    <label for="leaseTerm" class="form-label">Lease Term (months)</label>
                    <select id="leaseTerm" class="form-input">
                        <option value="24">24 months</option>
                        <option value="36" selected>36 months</option>
                        <option value="48">48 months</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="residualValue" class="form-label">Residual Value (%)</label>
                    <input type="number" id="residualValue" class="form-input" value="55" min="0" max="80" step="1">
                </div>
                <div class="form-group">
                    <label for="moneyFactor" class="form-label">Money Factor</label>
                    <input type="number" id="moneyFactor" class="form-input" value="0.00125" min="0" max="0.01" step="0.00001">
                </div>''',
        "results": '''                <div class="result-item">
                    <div class="result-label">Monthly Lease Payment</div>
                    <div class="result-value" id="monthlyPayment" style="font-size: 2.5rem; color: #10b981;">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Total Lease Cost</div>
                    <div class="result-value" id="totalCost">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Effective APR</div>
                    <div class="result-value" id="effectiveAPR">0%</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Depreciation Fee</div>
                    <div class="result-value" id="depreciationFee">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Finance Fee</div>
                    <div class="result-value" id="financeFee">$0</div>
                </div>''',
        "js": '''        function calculate() {
            const msrp = parseFloat(document.getElementById('msrp').value) || 0;
            const salePrice = parseFloat(document.getElementById('salePrice').value) || msrp;
            const downPayment = parseFloat(document.getElementById('downPayment').value) || 0;
            const leaseTerm = parseFloat(document.getElementById('leaseTerm').value) || 36;
            const residualPercent = parseFloat(document.getElementById('residualValue').value) / 100 || 0.55;
            const moneyFactor = parseFloat(document.getElementById('moneyFactor').value) || 0.00125;

            const residualValue = msrp * residualPercent;
            const netCapCost = salePrice - downPayment;
            const depreciationFee = (netCapCost - residualValue) / leaseTerm;
            const financeFee = (netCapCost + residualValue) * moneyFactor;
            const monthlyPayment = depreciationFee + financeFee;
            const totalCost = downPayment + (monthlyPayment * leaseTerm);
            const effectiveAPR = (moneyFactor * 2400).toFixed(2);

            document.getElementById('monthlyPayment').textContent = '$' + monthlyPayment.toLocaleString('en-US', {minimumFractionDigits: 2});
            document.getElementById('totalCost').textContent = '$' + totalCost.toLocaleString('en-US', {minimumFractionDigits: 2});
            document.getElementById('effectiveAPR').textContent = effectiveAPR + '%';
            document.getElementById('depreciationFee').textContent = '$' + depreciationFee.toLocaleString('en-US', {minimumFractionDigits: 2});
            document.getElementById('financeFee').textContent = '$' + financeFee.toLocaleString('en-US', {minimumFractionDigits: 2});
        }''',
        "content": '''            <h2>Understanding Car Leasing</h2>
            <p>Leasing a vehicle is essentially renting it for a specified period, typically 24-48 months. Instead of paying for the entire vehicle value, you pay for the depreciation during your lease term plus interest charges (called rent charges or finance fees). At lease end, you return the vehicle to the dealer unless you choose to purchase it for the predetermined residual value.</p>

            <p>Approximately 30% of new vehicles in the U.S. are leased rather than purchased. Leasing offers lower monthly payments compared to financing a purchase, access to newer vehicles more frequently, and potentially lower maintenance costs during the warranty period. However, it comes with mileage restrictions, wear-and-tear charges, and no equity building.</p>

            <h2>Key Lease Terms Explained</h2>
            <p><strong>Capitalized Cost (Cap Cost):</strong> The agreed-upon price of the vehicle, equivalent to the purchase price when buying. Negotiate this like you would when purchasing – dealerships often focus lease negotiations on monthly payments rather than vehicle price, where they have more markup flexibility.</p>

            <p><strong>Residual Value:</strong> The estimated value of the vehicle at lease end, expressed as a percentage of MSRP. Higher residual values mean lower depreciation charges and lower monthly payments. Luxury brands often have higher residuals (55-65%) than economy cars (45-55%). The manufacturer sets residual values based on projected resale values.</p>

            <p><strong>Money Factor:</strong> The interest rate equivalent used in leasing. Convert money factor to APR by multiplying by 2,400. For example, a money factor of 0.00125 equals 3% APR. Lower money factors mean lower finance charges. Good credit scores (720+) typically qualify for the best money factors.</p>

            <p><strong>Disposition Fee:</strong> A fee ($300-500) charged at lease end if you don't lease or purchase another vehicle from the same dealer. This covers the cost of preparing the returned vehicle for resale.</p>

            <p><strong>Acquisition Fee:</strong> An upfront fee ($595-995) charged by the leasing company to initiate the lease. Some dealers roll this into the monthly payment rather than requiring payment at signing.</p>

            <h2>How Lease Payments Are Calculated</h2>
            <p>Lease payments consist of two main components:</p>

            <p><strong>Depreciation Fee:</strong> (Negotiated Price - Residual Value) ÷ Lease Term. This covers the vehicle's expected value loss during your lease. If you lease a $30,000 car with 60% residual value for 36 months: ($30,000 - $18,000) ÷ 36 = $333.33 monthly depreciation fee.</p>

            <p><strong>Finance Fee (Rent Charge):</strong> (Negotiated Price + Residual Value) × Money Factor. This is the interest charge for financing the depreciation. Using the same example with 0.00125 money factor: ($30,000 + $18,000) × 0.00125 = $60 monthly finance fee.</p>

            <p>Total monthly payment before taxes: $333.33 + $60 = $393.33. Add applicable sales tax (typically charged only on monthly payments, not the full vehicle price – a tax advantage of leasing) and any additional fees for your final payment.</p>

            <h2>Leasing vs. Buying: Making the Right Choice</h2>
            <p><strong>Choose Leasing If You:</strong></p>
            <ul>
                <li>Want lower monthly payments (typically 30-50% less than financing a purchase)</li>
                <li>Prefer driving a new car every 2-4 years with latest technology and safety features</li>
                <li>Drive under 12,000-15,000 miles annually (typical lease allowances)</li>
                <li>Want to avoid the hassle of selling or trading in your vehicle</li>
                <li>Can deduct vehicle expenses for business use (lease payments are fully deductible; only loan interest is deductible when buying)</li>
                <li>Value warranty coverage for the entire ownership period</li>
                <li>Don't want long-term financial commitment to one vehicle</li>
            </ul>

            <p><strong>Choose Buying If You:</strong></p>
            <ul>
                <li>Drive more than 15,000 miles annually (excess mileage charges of $0.15-0.30 per mile add up quickly)</li>
                <li>Want to build equity and eventually own your vehicle outright</li>
                <li>Plan to keep your vehicle for 6+ years</li>
                <li>Want freedom to customize or modify your vehicle</li>
                <li>Don't want to worry about wear-and-tear charges for dings, scratches, or interior damage</li>
                <li>Want the option to sell whenever you choose</li>
                <li>Prefer not having continuous monthly payments</li>
            </ul>

            <h2>Negotiating a Better Lease Deal</h2>
            <p><strong>Negotiate Cap Cost, Not Payment:</strong> Dealers often steer lease negotiations to monthly payment rather than vehicle price. Insist on negotiating the capitalized cost just like you would a purchase price. Research fair market value using resources like Kelley Blue Book, Edmunds, or TrueCar before visiting dealerships.</p>

            <p><strong>Shop Money Factors:</strong> Money factors can vary between dealerships and manufacturers. Get quotes from multiple dealers and manufacturers' captive finance companies. Credit unions sometimes offer better lease rates than manufacturer financing.</p>

            <p><strong>Consider Multiple-Security-Deposit (MSD) Programs:</strong> Some manufacturers allow you to prepay up to 7-10 refundable security deposits (typically equal to monthly payment rounded up to $50) to reduce your money factor by 0.00005-0.00010 per deposit. This can save hundreds over the lease term, and you get the deposits back at lease end.</p>

            <p><strong>Timing Matters:</strong> End of month, quarter, and model year are opportune times for better deals. Dealers have sales quotas and manufacturers offer incentives to move outgoing model years. December particularly offers strong incentives as dealers close yearly books.</p>

            <p><strong>Consider Pre-Owned Leases:</strong> Certified pre-owned leases on 1-2 year old vehicles offer significantly lower payments (30-40% less) while still providing nearly new vehicles with remaining warranty coverage.</p>

            <h2>Lease Mileage: Understand the Limits</h2>
            <p>Standard leases include 10,000-12,000 miles per year, with 15,000-mile options available for higher monthly payments (typically $15-25 more per month per 1,000 additional annual miles). Excess mileage charges at lease end range from $0.15-0.30 per mile depending on the vehicle.</p>

            <p>Calculate your annual mileage before leasing. If you drive 15,000 miles annually, a 36-month lease allows 45,000 miles total. Ending with 50,000 miles costs $750-1,500 in excess mileage charges (5,000 miles × $0.15-0.30). It's usually cheaper to purchase higher mileage allowance upfront than pay excess charges later.</p>

            <p>Track your mileage periodically during the lease. If you're significantly under your allowance, you might reduce mileage on your next lease to lower payments. If over, consider purchasing additional miles before lease end (often at better rates than excess charges) or exploring early trade-in options.</p>

            <h2>End-of-Lease Options</h2>
            <p><strong>Return the Vehicle:</strong> Simply return it to the dealer, pay any excess mileage or wear-and-tear charges, and walk away. Schedule a pre-inspection 2-3 months before lease end (free service from most manufacturers) to identify and address potential charges before returning.</p>

            <p><strong>Purchase the Vehicle:</strong> Buy it for the predetermined residual value. This makes sense if: market value exceeds residual value (giving you instant equity), you've grown attached to the vehicle, you exceeded mileage significantly (buying removes excess mileage charges), or you modified it and want to keep those modifications.</p>

            <p><strong>Trade It In:</strong> If your vehicle's market value exceeds the residual value, you have equity to use toward your next vehicle. Get trade-in quotes from multiple dealers – they may offer more than the residual value, creating a built-in down payment for your next lease or purchase.</p>

            <p><strong>Transfer Your Lease:</strong> Services like Swapalease or LeaseTrader connect you with people wanting to assume your lease. This works well if you need to exit early, though some manufacturers prohibit transfers or charge transfer fees ($300-500).</p>

            <h2>Wear and Tear: What's Acceptable?</h2>
            <p>Lease agreements include "normal wear and tear" clauses, but interpretation varies. Generally acceptable:</p>
            <ul>
                <li>Small dings under 1 inch diameter</li>
                <li>Minor scratches that haven't penetrated the paint</li>
                <li>Small interior stains that can be cleaned</li>
                <li>Tire tread above 4/32 inch (ideally 5/32+)</li>
                <li>Minor windshield chips under 1 inch that don't obstruct vision</li>
            </ul>

            <p>Typically charged as excessive wear:</p>
            <ul>
                <li>Dents larger than 2 inches ($50-150 per panel)</li>
                <li>Scratches through the paint ($50-200 per panel)</li>
                <li>Cracked or broken glass ($200-500 per piece)</li>
                <li>Stained, torn, or burned upholstery ($100-500)</li>
                <li>Bald tires under 4/32 tread ($150-200 per tire)</li>
                <li>Broken or missing equipment ($100-1,000 depending on item)</li>
                <li>Odors from smoking or pets ($200-500)</li>
            </ul>

            <p>Consider fixing obvious damage yourself before return – you'll likely pay less than dealer charges. Get quotes from independent body shops for dings, scratches, and minor repairs. For worn tires, purchasing new ones yourself costs less than dealer charges.</p>

            <h2>Insurance Considerations</h2>
            <p>Lease agreements require comprehensive and collision coverage with low deductibles ($500-1,000). Additionally, consider gap insurance, which covers the difference between your vehicle's actual cash value and the remaining lease balance if the car is totaled or stolen. Many lease agreements include gap coverage, but verify this – purchasing separate gap insurance costs $400-700 versus $20-40 annually when added to your auto insurance.</p>

            <h2>Tax Benefits of Leasing</h2>
            <p>Business owners and self-employed individuals can deduct lease payments as a business expense if the vehicle is used for business purposes. With purchases, only loan interest and depreciation are deductible. Additionally, sales tax typically applies only to monthly payments rather than the full vehicle price, providing immediate tax savings.</p>

            <p>For personal use, there are no significant tax advantages to leasing over buying. However, states with high sales tax rates (8%+) benefit from paying tax only on monthly payments rather than the full purchase price upfront.</p>

            <h2>Credit Score Impact</h2>
            <p>Leasing requires good to excellent credit (scores 680+) for the best money factors. Scores below 620 typically don't qualify for leasing or face significantly higher money factors. A lease appears on your credit report as an installment loan and affects your credit similarly to an auto loan – positive if you make on-time payments, negative if you miss payments.</p>'''
    }
}

# Generate calculator files
def create_calculator(calc_id, spec):
    html_content = generate_enhanced_calculator(
        filename=calc_id,
        title=spec["title"],
        description=spec["description"],
        keywords=spec["keywords"],
        inputs_html=spec["inputs"],
        results_html=spec["results"],
        js_function=spec["js"],
        content_html=spec["content"]
    )

    filepath = f"/home/user/Calcuprime/calculators/{calc_id}.html"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return filepath

# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("CALCUPRIME CALCULATOR ENHANCEMENT TOOL")
    print("=" * 60)
    print()

    created_files = []
    for calc_id, spec in CALCULATORS.items():
        filepath = create_calculator(calc_id, spec)
        created_files.append(calc_id)
        print(f"✅ Enhanced: {spec['title']}")

    print()
    print("=" * 60)
    print(f"Successfully enhanced {len(created_files)} calculators!")
    print("=" * 60)
    print()
    print("Enhanced calculators:")
    for calc_id in created_files:
        print(f"  - {CALCULATORS[calc_id]['title']}")

    print()
    print("Note: This batch included 2 additional finance calculators.")
    print("Run additional enhancement scripts for remaining 26 calculators.")
    print()
