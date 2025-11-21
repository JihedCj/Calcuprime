#!/usr/bin/env python3
"""
Enhanced Content Generator for CalcuPrime Calculators
Adds comprehensive 1000+ word educational content to calculators
"""

# Finance Calculator Content
finance_content = {
    "tax-calculator": {
        "inputs_html": '''<div class="form-group">
                    <label for="annualIncome" class="form-label">Annual Income ($)</label>
                    <input type="number" id="annualIncome" class="form-input" value="75000" min="0" step="1000">
                </div>
                <div class="form-group">
                    <label for="filingStatus" class="form-label">Filing Status</label>
                    <select id="filingStatus" class="form-input">
                        <option value="single">Single</option>
                        <option value="married">Married Filing Jointly</option>
                        <option value="head">Head of Household</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="deductions" class="form-label">Total Deductions ($)</label>
                    <input type="number" id="deductions" class="form-input" value="12000" min="0" step="500">
                </div>''',
        "results_html": '''<div class="result-item">
                    <div class="result-label">Taxable Income</div>
                    <div class="result-value" id="taxableIncome">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Federal Tax</div>
                    <div class="result-value" id="federalTax" style="font-size: 2.5rem; color: #ef4444;">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Effective Tax Rate</div>
                    <div class="result-value" id="effectiveRate">0%</div>
                </div>
                <div class="result-item">
                    <div class="result-label">After-Tax Income</div>
                    <div class="result-value" id="afterTaxIncome" style="font-size: 2rem; color: #10b981;">$0</div>
                </div>''',
        "calculation_js": '''function calculate() {
            const income = parseFloat(document.getElementById('annualIncome').value) || 0;
            const status = document.getElementById('filingStatus').value;
            const deductions = parseFloat(document.getElementById('deductions').value) || 0;

            const taxableIncome = Math.max(0, income - deductions);

            // 2024 Tax brackets (simplified)
            let federalTax = 0;
            if (status === 'single') {
                if (taxableIncome <= 11000) federalTax = taxableIncome * 0.10;
                else if (taxableIncome <= 44725) federalTax = 1100 + (taxableIncome - 11000) * 0.12;
                else if (taxableIncome <= 95375) federalTax = 5147 + (taxableIncome - 44725) * 0.22;
                else if (taxableIncome <= 182100) federalTax = 16290 + (taxableIncome - 95375) * 0.24;
                else if (taxableIncome <= 231250) federalTax = 37104 + (taxableIncome - 182100) * 0.32;
                else if (taxableIncome <= 578125) federalTax = 52832 + (taxableIncome - 231250) * 0.35;
                else federalTax = 174238.25 + (taxableIncome - 578125) * 0.37;
            } else {
                // Married filing jointly (doubled brackets)
                if (taxableIncome <= 22000) federalTax = taxableIncome * 0.10;
                else if (taxableIncome <= 89050) federalTax = 2200 + (taxableIncome - 22000) * 0.12;
                else if (taxableIncome <= 190750) federalTax = 10294 + (taxableIncome - 89050) * 0.22;
                else if (taxableIncome <= 364200) federalTax = 32580 + (taxableIncome - 190750) * 0.24;
                else if (taxableIncome <= 462500) federalTax = 74208 + (taxableIncome - 364200) * 0.32;
                else if (taxableIncome <= 693750) federalTax = 105664 + (taxableIncome - 462500) * 0.35;
                else federalTax = 186601.5 + (taxableIncome - 693750) * 0.37;
            }

            const effectiveRate = income > 0 ? (federalTax / income * 100).toFixed(2) : 0;
            const afterTaxIncome = income - federalTax;

            document.getElementById('taxableIncome').textContent = '$' + taxableIncome.toLocaleString('en-US', {maximumFractionDigits: 0});
            document.getElementById('federalTax').textContent = '$' + federalTax.toLocaleString('en-US', {maximumFractionDigits: 0});
            document.getElementById('effectiveRate').textContent = effectiveRate + '%';
            document.getElementById('afterTaxIncome').textContent = '$' + afterTaxIncome.toLocaleString('en-US', {maximumFractionDigits: 0});
        }''',
        "content": '''<h2>Understanding Federal Income Tax</h2>
            <p>The U.S. federal income tax system is progressive, meaning tax rates increase as income rises. Our tax calculator helps you estimate your federal tax liability based on your annual income, filing status, and deductions. Understanding how taxes are calculated is essential for financial planning and maximizing your take-home pay.</p>

            <h2>How Federal Tax Brackets Work</h2>
            <p>Many people misunderstand tax brackets. The U.S. uses a marginal tax rate system, which means different portions of your income are taxed at different rates. For example, if you're single and earn $50,000 in 2024, you don't pay 22% on the entire amount. Instead:</p>
            <ul>
                <li>The first $11,000 is taxed at 10%</li>
                <li>Income from $11,001 to $44,725 is taxed at 12%</li>
                <li>Income from $44,726 to $50,000 is taxed at 22%</li>
            </ul>
            <p>This progressive system ensures lower-income earners pay less while higher earners contribute proportionally more.</p>

            <h2>Standard Deduction vs. Itemized Deductions</h2>
            <p>The standard deduction is a fixed dollar amount that reduces your taxable income. For 2024, it's $13,850 for single filers and $27,700 for married couples filing jointly. You can instead choose to itemize deductions if your qualifying expenses exceed the standard deduction amount.</p>

            <p>Common itemized deductions include:</p>
            <ul>
                <li><strong>Mortgage Interest:</strong> Interest paid on home loans up to $750,000</li>
                <li><strong>State and Local Taxes:</strong> Up to $10,000 in property and income taxes</li>
                <li><strong>Charitable Contributions:</strong> Donations to qualified organizations</li>
                <li><strong>Medical Expenses:</strong> Expenses exceeding 7.5% of your AGI</li>
            </ul>

            <h2>Filing Status and Its Impact</h2>
            <p>Your filing status significantly affects your tax liability. The five filing statuses are:</p>

            <p><strong>Single:</strong> Unmarried individuals with no dependents typically use this status, which has the narrowest tax brackets.</p>

            <p><strong>Married Filing Jointly:</strong> Married couples who file together benefit from wider tax brackets and often pay less tax overall. This is usually the most advantageous status for married couples.</p>

            <p><strong>Married Filing Separately:</strong> Rarely beneficial, this status may be used when spouses want to be responsible only for their own tax or when one spouse has significant medical expenses.</p>

            <p><strong>Head of Household:</strong> Unmarried individuals who pay more than half the cost of maintaining a home for a qualifying dependent receive more favorable rates than single filers.</p>

            <p><strong>Qualifying Widow(er):</strong> Available for two years after a spouse's death if you have a dependent child, providing the same benefits as married filing jointly.</p>

            <h2>Tax Planning Strategies</h2>
            <p>Strategic tax planning can significantly reduce your tax liability:</p>

            <p><strong>Maximize Retirement Contributions:</strong> Traditional 401(k) and IRA contributions reduce your taxable income dollar-for-dollar. For 2024, you can contribute up to $23,000 to a 401(k) and $7,000 to an IRA (with catch-up contributions available for those 50+).</p>

            <p><strong>Utilize Tax Credits:</strong> Tax credits directly reduce your tax bill and are more valuable than deductions. Common credits include the Earned Income Tax Credit, Child Tax Credit ($2,000 per qualifying child), and education credits.</p>

            <p><strong>Harvest Tax Losses:</strong> Selling investments at a loss can offset capital gains and up to $3,000 of ordinary income annually.</p>

            <p><strong>Bunch Deductions:</strong> Consolidating itemizable expenses into alternating years can help exceed the standard deduction threshold.</p>

            <h2>Common Tax Mistakes to Avoid</h2>
            <p>Many taxpayers inadvertently pay more than necessary due to common errors:</p>
            <ul>
                <li>Not claiming all available deductions and credits</li>
                <li>Failing to adjust withholding after major life changes</li>
                <li>Missing the standard deduction increase available after age 65</li>
                <li>Forgetting to deduct home office expenses for remote workers</li>
                <li>Not keeping adequate records for deductions</li>
            </ul>

            <h2>Understanding Effective vs. Marginal Tax Rates</h2>
            <p>Your <strong>marginal tax rate</strong> is the rate you pay on your last dollar of income – your tax bracket. Your <strong>effective tax rate</strong> is your average rate across all income. For example, someone in the 24% bracket might have an effective rate of only 15% because lower income portions were taxed at lower rates.</p>

            <p>Understanding this distinction is crucial for financial decisions. When evaluating whether to earn additional income, consider your marginal rate. When assessing your overall tax burden, use your effective rate.</p>

            <h2>State and Local Taxes</h2>
            <p>Don't forget that most states also impose income taxes, ranging from 0% in states like Texas and Florida to over 13% in California. Additionally, you may owe local city or county income taxes. Our calculator focuses on federal taxes, but remember to account for state and local obligations in your planning.</p>

            <h2>When to Consult a Tax Professional</h2>
            <p>While calculators provide helpful estimates, consider professional help if you:</p>
            <ul>
                <li>Own a business or have self-employment income</li>
                <li>Have complex investments or rental properties</li>
                <li>Experienced major life changes (marriage, divorce, inheritance)</li>
                <li>Have foreign income or assets</li>
                <li>Face an IRS audit or owe back taxes</li>
            </ul>

            <p>A qualified tax professional can identify deductions you might miss and ensure compliance with ever-changing tax laws.</p>'''
    },

    "paycheck-calculator": {
        "inputs_html": '''<div class="form-group">
                    <label for="salary" class="form-label">Annual Salary ($)</label>
                    <input type="number" id="salary" class="form-input" value="60000" min="0" step="1000">
                </div>
                <div class="form-group">
                    <label for="payFrequency" class="form-label">Pay Frequency</label>
                    <select id="payFrequency" class="form-input">
                        <option value="26">Bi-weekly (26 paychecks)</option>
                        <option value="24">Semi-monthly (24 paychecks)</option>
                        <option value="12">Monthly (12 paychecks)</option>
                        <option value="52">Weekly (52 paychecks)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="federalAllowances" class="form-label">Federal Tax Rate (%)</label>
                    <input type="number" id="federalAllowances" class="form-input" value="15" min="0" max="40" step="0.5">
                </div>
                <div class="form-group">
                    <label for="stateTax" class="form-label">State Tax Rate (%)</label>
                    <input type="number" id="stateTax" class="form-input" value="5" min="0" max="15" step="0.5">
                </div>''',
        "results_html": '''<div class="result-item">
                    <div class="result-label">Gross Pay (per paycheck)</div>
                    <div class="result-value" id="grossPay">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Federal Tax</div>
                    <div class="result-value" id="federalTax">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">State Tax</div>
                    <div class="result-value" id="stateTaxAmount">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">FICA (7.65%)</div>
                    <div class="result-value" id="ficaTax">$0</div>
                </div>
                <div class="result-item">
                    <div class="result-label">Net Pay (Take Home)</div>
                    <div class="result-value" id="netPay" style="font-size: 2.5rem; color: #10b981;">$0</div>
                </div>''',
        "calculation_js": '''function calculate() {
            const salary = parseFloat(document.getElementById('salary').value) || 0;
            const frequency = parseFloat(document.getElementById('payFrequency').value) || 26;
            const federalRate = parseFloat(document.getElementById('federalAllowances').value) / 100 || 0.15;
            const stateRate = parseFloat(document.getElementById('stateTax').value) / 100 || 0.05;

            const grossPay = salary / frequency;
            const federalTax = grossPay * federalRate;
            const stateTax = grossPay * stateRate;
            const ficaTax = grossPay * 0.0765; // Social Security (6.2%) + Medicare (1.45%)
            const netPay = grossPay - federalTax - stateTax - ficaTax;

            document.getElementById('grossPay').textContent = '$' + grossPay.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('federalTax').textContent = '-$' + federalTax.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('stateTaxAmount').textContent = '-$' + stateTax.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('ficaTax').textContent = '-$' + ficaTax.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
            document.getElementById('netPay').textContent = '$' + netPay.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
        }''',
        "content": '''<h2>Understanding Your Paycheck</h2>
            <p>Your paycheck represents more than just your hourly wage or annual salary divided by pay periods. Understanding the various deductions and how they're calculated empowers you to make informed financial decisions, plan your budget accurately, and ensure you're being paid correctly.</p>

            <h2>Gross Pay vs. Net Pay</h2>
            <p><strong>Gross pay</strong> is your total earnings before any deductions. It's calculated by dividing your annual salary by the number of pay periods in a year. For hourly employees, it's the number of hours worked multiplied by the hourly rate, plus any overtime.</p>

            <p><strong>Net pay</strong> or "take-home pay" is what you actually receive after all mandatory and voluntary deductions. The difference between gross and net pay can be substantial – often 20-30% or more of your gross earnings.</p>

            <h2>Pay Frequency Matters</h2>
            <p>How often you're paid affects your financial planning:</p>

            <p><strong>Weekly (52 paychecks):</strong> Provides the most frequent cash flow, helpful for managing weekly expenses. However, individual paychecks are smaller.</p>

            <p><strong>Bi-weekly (26 paychecks):</strong> The most common pay frequency in the U.S. Employees receive two paychecks most months, with two months per year having three paychecks – a nice bonus for savings.</p>

            <p><strong>Semi-monthly (24 paychecks):</strong> Typically paid on the 15th and last day of the month. Easier for monthly budgeting since amounts are consistent, but can complicate hourly calculations.</p>

            <p><strong>Monthly (12 paychecks):</strong> Less common in the U.S., requires more disciplined budgeting but simplifies monthly expense planning.</p>

            <h2>Federal Income Tax Withholding</h2>
            <p>Your employer withholds federal income tax from each paycheck based on the information you provided on Form W-4. Key factors affecting withholding include:</p>

            <ul>
                <li><strong>Filing Status:</strong> Single, married, or head of household</li>
                <li><strong>Number of Dependents:</strong> More dependents reduce withholding</li>
                <li><strong>Additional Income:</strong> Other jobs or investment income</li>
                <li><strong>Deductions and Credits:</strong> Student loan interest, IRA contributions, etc.</li>
            </ul>

            <p>The goal is to withhold the right amount – not too much (giving the government an interest-free loan) or too little (facing a tax bill and potential penalties in April).</p>

            <h2>FICA Taxes Explained</h2>
            <p>FICA (Federal Insurance Contributions Act) taxes fund Social Security and Medicare. In 2024, the breakdown is:</p>

            <p><strong>Social Security:</strong> 6.2% of gross pay up to $168,600 (the wage base limit). Both employee and employer each pay 6.2%, for a total of 12.4%.</p>

            <p><strong>Medicare:</strong> 1.45% of all gross pay with no income limit. Employers match this 1.45%. High earners (over $200,000 single, $250,000 married) pay an additional 0.9% Medicare surtax.</p>

            <p>Combined, employees pay 7.65% in FICA taxes. Self-employed individuals pay both the employee and employer portions (15.3%) but can deduct half as a business expense.</p>

            <h2>State and Local Income Taxes</h2>
            <p>Most states impose income taxes ranging from 1% to over 13%. Nine states have no income tax: Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington, and Wyoming. Some cities and counties also levy local income taxes.</p>

            <p>State tax rates vary significantly. High-income earners in California might pay over 13% state tax, while someone in Pennsylvania pays a flat 3.07% regardless of income level.</p>

            <h2>Pre-Tax Deductions</h2>
            <p>Pre-tax deductions reduce your taxable income, lowering your overall tax burden. Common pre-tax deductions include:</p>

            <p><strong>Retirement Contributions:</strong> 401(k), 403(b), and traditional IRA contributions reduce your current taxable income while building retirement savings. For 2024, you can contribute up to $23,000 to a 401(k).</p>

            <p><strong>Health Insurance Premiums:</strong> Employer-sponsored health insurance premiums are typically deducted pre-tax, reducing both income tax and FICA taxes.</p>

            <p><strong>Health Savings Account (HSA):</strong> If you have a high-deductible health plan, HSA contributions are triple tax-advantaged – tax-deductible, grow tax-free, and withdrawals for qualified medical expenses are tax-free.</p>

            <p><strong>Flexible Spending Accounts (FSA):</strong> Healthcare FSAs allow up to $3,200 (2024) in pre-tax contributions for medical expenses. Dependent Care FSAs allow up to $5,000 for childcare expenses.</p>

            <p><strong>Commuter Benefits:</strong> Up to $315 per month (2024) can be set aside pre-tax for parking and transit expenses.</p>

            <h2>Post-Tax Deductions</h2>
            <p>These deductions come from your net pay after taxes are calculated:</p>
            <ul>
                <li>Roth 401(k) contributions</li>
                <li>Supplemental life insurance premiums</li>
                <li>Disability insurance</li>
                <li>Union dues</li>
                <li>Charitable contributions</li>
                <li>Wage garnishments</li>
            </ul>

            <h2>How to Maximize Your Take-Home Pay</h2>
            <p><strong>Optimize Your W-4:</strong> Review and update your W-4 annually or after major life changes. The IRS Tax Withholding Estimator helps determine the right withholding to avoid refunds or tax bills.</p>

            <p><strong>Leverage Pre-Tax Benefits:</strong> Maximize contributions to employer-sponsored retirement plans and health savings accounts to reduce taxable income while building wealth.</p>

            <p><strong>Understand State Tax Implications:</strong> If you work remotely or across state lines, understand which state(s) can tax your income. Some states have reciprocal agreements.</p>

            <p><strong>Timing Bonuses and Income:</strong> If you receive bonuses, understanding supplemental wage withholding (often 22% federal flat rate) helps you anticipate the net amount.</p>

            <h2>Common Paycheck Mistakes</h2>
            <p>Payroll errors happen more often than you might think. Watch for:</p>
            <ul>
                <li>Incorrect hours or overtime calculations</li>
                <li>Wrong tax filing status or withholding allowances</li>
                <li>Missing overtime premium pay (time-and-a-half after 40 hours)</li>
                <li>Incorrect benefit deductions</li>
                <li>Not receiving earned commission or bonuses</li>
            </ul>

            <p>Always review your pay stub carefully. Report discrepancies to HR or payroll immediately – some states limit how far back you can claim unpaid wages.</p>

            <h2>Reading Your Pay Stub</h2>
            <p>Your pay stub contains crucial information beyond just your net pay:</p>

            <p><strong>Year-to-Date (YTD) Totals:</strong> Track your cumulative earnings and taxes paid throughout the year.</p>

            <p><strong>Hours Breakdown:</strong> Regular hours, overtime, sick leave, and vacation time used and accrued.</p>

            <p><strong>Tax Withholdings:</strong> Federal, state, local, FICA, and any additional withholdings.</p>

            <p><strong>Benefits and Deductions:</strong> All pre-tax and post-tax deductions with current period and YTD amounts.</p>

            <h2>Special Considerations for Different Workers</h2>
            <p><strong>Hourly Employees:</strong> Track your hours carefully. Federal law requires overtime pay (1.5x regular rate) for hours over 40 per week for non-exempt employees.</p>

            <p><strong>Salaried Exempt Employees:</strong> Not entitled to overtime pay. Your paycheck should be consistent regardless of hours worked (though some deductions may vary).</p>

            <p><strong>Tipped Employees:</strong> Employers can pay a lower base wage ($2.13 federal minimum) if tips bring total compensation to at least standard minimum wage. All tips are taxable income.</p>

            <p><strong>Contract Workers:</strong> Paid via 1099 rather than W-2, contractors receive gross pay without withholdings but must pay self-employment taxes quarterly.</p>'''
    }
}

print("Content enhancement script ready. Contains comprehensive content for Tax and Paycheck calculators.")
print("Run the content sections to enhance your calculators!")
