import datetime
from src.models.user import Convert, FinanceNews, db, OnlineBankingInterface, SpecialPackage, MinimumBalance, Loan, CreditCard, Fees
from app import app

def add_online_banking_interface(bank_name, mobile_app_usability, bill_payments, e_wallet_integration, security_features):
    new_interface = OnlineBankingInterface(
        bank_name=bank_name,
        mobile_app_usability=mobile_app_usability,
        bill_payments=bill_payments,
        e_wallet_integration=e_wallet_integration,
        security_features=security_features,
        created_at=datetime.datetime.now()
    )
    db.session.add(new_interface)
    db.session.commit()
    return new_interface

def add_special_package(bank_name, package_name, account_maintenance_fees, perks_and_benefits, eligibility_requirements):
    new_package = SpecialPackage(
        bank_name=bank_name,
        package_name=package_name,
        account_maintenance_fees=account_maintenance_fees,
        perks_and_benefits=perks_and_benefits,
        eligibility_requirements=eligibility_requirements,
        created_at=datetime.datetime.now()
    )
    db.session.add(new_package)
    db.session.commit()
    return new_package

def add_minimum_balance(bank_name, minimum_balance_requirement, annual_interest_rate, additional_benefits):
    new_balance = MinimumBalance(
        bank_name=bank_name,
        minimum_balance_requirement=minimum_balance_requirement,
        annual_interest_rate=annual_interest_rate,
        additional_benefits=additional_benefits,
        created_at=datetime.datetime.now()
    )
    db.session.add(new_balance)
    db.session.commit()
    return new_balance

def add_loan(bank_name, loan_type, interest_rate, loan_term, eligibility_criteria, maximum_amount=None, approval_time=None, fees=None):
    new_loan = Loan(
        bank_name=bank_name,
        loan_type=loan_type,
        interest_rates=interest_rate,
        loan_terms=loan_term,
        maximum_amount=maximum_amount,
        approval_time=approval_time,
        fees=fees,
        created_at=datetime.datetime.now()
    )
    db.session.add(new_loan)
    db.session.commit()
    return new_loan

def add_credit_card(bank_name, annual_fees, cashback_rewards, credit_limits, interest_rates_on_unpaid_balances):
    new_card = CreditCard(
        bank_name=bank_name,
        annual_fees=annual_fees,
        cashback_rewards=cashback_rewards,
        credit_limits=credit_limits,
        interest_rates_on_unpaid_balances=interest_rates_on_unpaid_balances,
        created_at=datetime.datetime.now()
    )
    db.session.add(new_card)
    db.session.commit()
    return new_card

def add_fees(bank_name, account_maintenance_fees, atm_withdrawal_fees, international_transfer_fees, currency_exchange_fees):
    new_fees = Fees(
        bank_name=bank_name,
        account_maintenance_fees=account_maintenance_fees,
        atm_withdrawal_fees=atm_withdrawal_fees,
        international_transfer_fees=international_transfer_fees,
        currency_exchange_fees=currency_exchange_fees,
        created_at=datetime.datetime.now()
    )
    db.session.add(new_fees)
    db.session.commit()
    return new_fees
def add_news(title, content, source, link):
    new_news = FinanceNews(
        title=title,
        content=content,
        source=source,
        link=link,
        published_at=datetime.datetime.now()
    )
    db.session.add(new_news)
    db.session.commit()
    return new_news

def add_convert(to_currency, conversion_rate):
    new_convert = Convert(
        to_currency=to_currency,
        conversion_rate=conversion_rate,
        created_at=datetime.datetime.now()
    )
    db.session.add(new_convert)
    db.session.commit()
    return new_convert

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()

        online_banking_data = [
            {'bank_name': 'Société Tunisienne de Banque (STB)', 'online_banking_interface': 'User-friendly, intuitive', 'mobile_app_usability': 'Highly rated, easy navigation', 'bill_payments': 'Supports various bill payments', 'e_wallet_integration': 'Limited integration', 'security_features': 'Multi-Factor Authentication (MFA), SSL'},
            {'bank_name': 'Banque Nationale Agricole (BNA)', 'online_banking_interface': 'Modern design, responsive', 'mobile_app_usability': 'Good usability', 'bill_payments': 'Comprehensive bill payment options', 'e_wallet_integration': 'Limited integration', 'security_features': '3D Secure, encryption'},
            {'bank_name': 'Banque de l\'Habitat (BH)', 'online_banking_interface': 'Simple layout', 'mobile_app_usability': 'Functional, basic features', 'bill_payments': 'Supports utility and service bills', 'e_wallet_integration': 'No direct e-wallet integration', 'security_features': 'Strong encryption, transaction alerts'},
            {'bank_name': 'Banque de Financement des Petites et Moyennes Entreprises (BFPME)', 'online_banking_interface': 'Basic interface', 'mobile_app_usability': 'User-friendly', 'bill_payments': 'Limited to selected bills', 'e_wallet_integration': 'No e-wallet features', 'security_features': 'Basic security protocols'},
            {'bank_name': 'Banque Tunisienne de Solidarité (BTS)', 'online_banking_interface': 'Basic and functional', 'mobile_app_usability': 'Limited features', 'bill_payments': 'Limited bill payment options', 'e_wallet_integration': 'No e-wallet integration', 'security_features': 'Standard security measures'},
            {'bank_name': 'Tunisian Solidarity Bank (BS)', 'online_banking_interface': 'Simple and straightforward', 'mobile_app_usability': 'Basic usability', 'bill_payments': 'Supports some bill payments', 'e_wallet_integration': 'No e-wallet features', 'security_features': 'Standard security measures'},
            {'bank_name': 'Banque de Tunisie et des Emirats (BTE)', 'online_banking_interface': 'Modern and user-friendly', 'mobile_app_usability': 'Highly rated', 'bill_payments': 'Comprehensive bill payment options', 'e_wallet_integration': 'Limited integration', 'security_features': 'MFA, SSL encryption'},
            {'bank_name': 'Amen Bank', 'online_banking_interface': 'Intuitive interface', 'mobile_app_usability': 'Highly rated', 'bill_payments': 'Wide range of bill payments', 'e_wallet_integration': 'Integrated with local e-wallets', 'security_features': 'Advanced security features'},
            {'bank_name': 'Arab Tunisian Bank (ATB)', 'online_banking_interface': 'Clean and modern', 'mobile_app_usability': 'Good usability', 'bill_payments': 'Supports various bills', 'e_wallet_integration': 'Integrated with local e-wallets', 'security_features': '3D Secure, MFA'},
            {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'online_banking_interface': 'Comprehensive interface', 'mobile_app_usability': 'Highly rated', 'bill_payments': 'Full range of bill payments', 'e_wallet_integration': 'Integrated with local e-wallets', 'security_features': 'Strong encryption, transaction alerts'},
            {'bank_name': 'Banque Zitouna', 'online_banking_interface': 'Simple layout', 'mobile_app_usability': 'Basic usability', 'bill_payments': 'Limited bill payment options', 'e_wallet_integration': 'Islamic finance compliant e-wallets', 'security_features': 'Basic security measures'},
            {'bank_name': 'Citibank', 'online_banking_interface': 'Advanced online platform', 'mobile_app_usability': 'Highly rated', 'bill_payments': 'Supports international bill payments', 'e_wallet_integration': 'Global e-wallet integration', 'security_features': 'Advanced security protocols'},
            {'bank_name': 'Al Baraka Bank Tunisia', 'online_banking_interface': 'User-friendly', 'mobile_app_usability': 'Functional', 'bill_payments': 'Limited to selected bills', 'e_wallet_integration': 'Islamic finance compliant e-wallets', 'security_features': 'Standard security measures'},
            {'bank_name': 'Bank of Africa - Tunisia', 'online_banking_interface': 'Modern design', 'mobile_app_usability': 'Good usability', 'bill_payments': 'Comprehensive bill payment options', 'e_wallet_integration': 'Integrated with local e-wallets', 'security_features': 'Strong encryption, transaction alerts'},
            {'bank_name': 'Attijari Bank', 'online_banking_interface': 'Comprehensive interface', 'mobile_app_usability': 'Highly rated', 'bill_payments': 'Full range of bill payments', 'e_wallet_integration': 'Integrated with local e-wallets', 'security_features': 'MFA, SSL encryption'},
            {'bank_name': 'Qatar National Bank (QNB)', 'online_banking_interface': 'Advanced online platform', 'mobile_app_usability': 'Highly rated', 'bill_payments': 'Supports international bills', 'e_wallet_integration': 'Global e-wallet integration', 'security_features': 'Advanced security protocols'},
            {'bank_name': 'Zitouna Bank', 'online_banking_interface': 'Simple layout', 'mobile_app_usability': 'Basic usability', 'bill_payments': 'Limited bill payment options', 'e_wallet_integration': 'Islamic finance compliant e-wallets', 'security_features': 'Basic security measures'},
            {'bank_name': 'Wifak Bank', 'online_banking_interface': 'User-friendly', 'mobile_app_usability': 'Functional', 'bill_payments': 'Limited to selected bills', 'e_wallet_integration': 'Islamic finance compliant e-wallets', 'security_features': 'Standard security measures'}
        ]

        
        convert_data = [
            { "to_currency": "USD", "conversion_rate": 0.32 },
            { "to_currency": "EUR", "conversion_rate": 0.30 },
            { "to_currency": "GBP", "conversion_rate": 0.26 },
            { "to_currency": "JPY", "conversion_rate": 3.56 },
            { "to_currency": "CAD", "conversion_rate": 0.38 }
            ]


        special_packages = [
        {'bank_name': 'Société Tunisienne de Banque (STB)', 'package_name': 'Pack Student', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Free debit card, online banking access, free internal transfers', 'eligibility_requirements': 'Students aged 18-29 with proof of enrollment'},
        {'bank_name': 'Banque Nationale Agricole (BNA)', 'package_name': 'Hello Student Pack', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Free student account, mobile banking, SMS alerts', 'eligibility_requirements': 'Students with valid ID and enrollment certificate'},
        {'bank_name': 'Banque de Tunisie', 'package_name': 'BT Etudiants', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Free debit card, access to BTNET and BTMOBILE services', 'eligibility_requirements': 'Students or new graduates with proof of status'},
        {'bank_name': 'Attijari Bank', 'package_name': 'Pack Stud\'In', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Free banking services, credit options for studies', 'eligibility_requirements': 'Students with valid ID and enrollment certificate'},
        {'bank_name': 'Amen Bank', 'package_name': 'Youth Package', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Online banking, debit card, tailored financial solutions', 'eligibility_requirements': 'Students with proof of enrollment'},
        {'bank_name': 'TSB Bank', 'package_name': 'YOUNG Card', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Reloadable card for young users, parental control on spending', 'eligibility_requirements': 'Ages 14-25 with parental consent'},
        {'bank_name': 'Banque de l\'Habitat (BH)', 'package_name': 'Student Account', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Free account management, online banking access', 'eligibility_requirements': 'Students with proof of enrollment'},
        {'bank_name': 'Al Baraka Bank Tunisia', 'package_name': 'Student Package', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Islamic-compliant banking services, free debit card', 'eligibility_requirements': 'Students with proof of enrollment'},
        {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'package_name': 'Student Account', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Free account maintenance, online banking', 'eligibility_requirements': 'Students with valid ID and enrollment certificate'},
        {'bank_name': 'Qatar National Bank (QNB)', 'package_name': 'Young Savers Plan', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Higher interest rates, free debit card, financial literacy workshops', 'eligibility_requirements': 'Students aged 18-25 with proof of enrollment'},
        {'bank_name': 'Bank of Africa - Tunisia', 'package_name': 'Future Stars', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Free online transactions, special student loans, mobile banking', 'eligibility_requirements': 'Students aged 18-30 with valid student ID'},
        {'bank_name': 'Zitouna Bank', 'package_name': 'Shabab Package', 'account_maintenance_fees': 0.0, 'perks_and_benefits': 'Islamic finance compliant savings, free debit card, personalized support', 'eligibility_requirements': 'Students aged 16-30 with valid enrollment certificate'}
    ]


        minimum_balances = [
            {'bank_name': 'Société Tunisienne de Banque (STB)', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 8.00, 'additional_benefits': 'Unlimited withdrawals, no fees for account maintenance'},
            {'bank_name': 'Banque Nationale Agricole (BNA)', 'minimum_balance_requirement': 150.0, 'annual_interest_rate': 8.00, 'additional_benefits': 'Flexible withdrawal options, free online banking services'},
            {'bank_name': 'Banque de l\'Habitat (BH)', 'minimum_balance_requirement': 200.0, 'annual_interest_rate': 7.50, 'additional_benefits': 'Special incentives for housing-related savings'},
            {'bank_name': 'Banque de Financement des Petites et Moyennes Entreprises (BFPME)', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.75, 'additional_benefits': 'No withdrawal limits, tailored services for SMEs'},
            {'bank_name': 'Banque Tunisienne de Solidarité (BTS)', 'minimum_balance_requirement': 50.0, 'annual_interest_rate': 6.50, 'additional_benefits': 'Social initiatives support, flexible terms'},
            {'bank_name': 'Tunisian Solidarity Bank (BS)', 'minimum_balance_requirement': 50.0, 'annual_interest_rate': 6.50, 'additional_benefits': 'Community-focused benefits, no fees for low balances'},
            {'bank_name': 'Banque de Tunisie et des Emirats (BTE)', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 8.00, 'additional_benefits': 'Free transfers between accounts, online banking access'},
            {'bank_name': 'Amen Bank', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.75, 'additional_benefits': 'Cash deposit and withdrawal without limits'},
            {'bank_name': 'Arab Tunisian Bank (ATB)', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.25, 'additional_benefits': 'Attractive loyalty programs for long-term savers'},
            {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 8.00, 'additional_benefits': 'Comprehensive online banking features, free financial advice'},
            {'bank_name': 'Banque Zitouna', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.50, 'additional_benefits': 'Islamic finance products available, community benefits'},
            {'bank_name': 'Citibank', 'minimum_balance_requirement': 500.0, 'annual_interest_rate': 7.75, 'additional_benefits': 'Global banking services, no fees on international transfers'},
            {'bank_name': 'Al Baraka Bank Tunisia', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.00, 'additional_benefits': 'Sharia-compliant savings options, community support'},
            {'bank_name': 'Bank of Africa - Tunisia', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.25, 'additional_benefits': 'Personalized banking services, flexible terms'},
            {'bank_name': 'Attijari Bank', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 8.00, 'additional_benefits': 'Extensive branch network, online banking features'},
            {'bank_name': 'Qatar National Bank (QNB)', 'minimum_balance_requirement': 500.0, 'annual_interest_rate': 7.75, 'additional_benefits': 'International banking services, no fees on certain accounts'},
            {'bank_name': 'Zitouna Bank', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.50, 'additional_benefits': 'Islamic finance compliant savings products'},
            {'bank_name': 'Wifak Bank', 'minimum_balance_requirement': 100.0, 'annual_interest_rate': 7.25, 'additional_benefits': 'Community-focused initiatives, Islamic banking benefits'}
        ]




        loans = [
    {'bank_name': 'Société Tunisienne de Banque (STB)', 'loan_type': 'Personal Loan', 'interest_rates': 7.5, 'loan_terms': '5 years', 'maximum_amount': 20000, 'approval_time': '3 days', 'fees': 50.0, 'eligibility_criteria': 'Minimum income of 1500/month', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Banque Nationale Agricole (BNA)', 'loan_type': 'Home Loan', 'interest_rates': 6.0, 'loan_terms': '15 years', 'maximum_amount': 150000, 'approval_time': '7 days', 'fees': 200.0, 'eligibility_criteria': 'Age between 25 and 60 years', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Qatar National Bank (QNB)', 'loan_type': 'Car Loan', 'interest_rates': 5.2, 'loan_terms': 'Up to 7 years for new cars; 5 years for used cars', 'maximum_amount': 50000, 'approval_time': '5 days', 'fees': 150.0, 'eligibility_criteria': 'Valid driving license and stable income', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Qatar National Bank (QNB)', 'loan_type': 'Personal Loan', 'interest_rates': 8.5, 'loan_terms': 'Typically flexible terms', 'maximum_amount': 30000, 'approval_time': '3 days', 'fees': 80.0, 'eligibility_criteria': 'Minimum 3 months of employment', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Qatar National Bank (QNB)', 'loan_type': 'Mortgage', 'interest_rates': 6.8, 'loan_terms': 'Up to 20 years', 'maximum_amount': 200000, 'approval_time': '10 days', 'fees': 300.0, 'eligibility_criteria': 'Own a property or have a guarantor', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Bank ABC', 'loan_type': 'Car Loan', 'interest_rates': 4.5, 'loan_terms': 'Flexible terms', 'maximum_amount': 50000, 'approval_time': '7 days', 'fees': 100.0, 'eligibility_criteria': 'Minimum age of 21', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Bank ABC', 'loan_type': 'Personal Loan', 'interest_rates': 9.0, 'loan_terms': 'Minimum 3 years; max 15 years', 'maximum_amount': 20000, 'approval_time': '5 days', 'fees': 50.0, 'eligibility_criteria': 'Valid ID and proof of income', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Bank ABC', 'loan_type': 'Mortgage', 'interest_rates': 6.3, 'loan_terms': 'Up to 15 years', 'maximum_amount': 150000, 'approval_time': '12 days', 'fees': 250.0, 'eligibility_criteria': 'Proof of stable income', 'created_at': datetime.datetime.now()},
    {'bank_name': 'TSB Bank', 'loan_type': 'Car Loan', 'interest_rates': 5.0, 'loan_terms': 'Up to 7 years for new; 5 years for used cars', 'maximum_amount': 50000, 'approval_time': '5 days', 'fees': 120.0, 'eligibility_criteria': 'Age between 22 and 55 years', 'created_at': datetime.datetime.now()},
    {'bank_name': 'TSB Bank', 'loan_type': 'Personal Loan', 'interest_rates': 7.0, 'loan_terms': 'Flexible terms', 'maximum_amount': 25000, 'approval_time': '3 days', 'fees': 70.0, 'eligibility_criteria': 'Full-time employee or self-employed', 'created_at': datetime.datetime.now()},
    {'bank_name': 'TSB Bank', 'loan_type': 'Mortgage', 'interest_rates': 5.9, 'loan_terms': 'Generally up to 20 years', 'maximum_amount': 200000, 'approval_time': '10 days', 'fees': 200.0, 'eligibility_criteria': 'Property must be in good condition', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'loan_type': 'Car Loan', 'interest_rates': 4.3, 'loan_terms': 'Flexible terms', 'maximum_amount': 45000, 'approval_time': '4 days', 'fees': 90.0, 'eligibility_criteria': 'At least 1 year of stable employment', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'loan_type': 'Personal Loan', 'interest_rates': 8.0, 'loan_terms': 'Flexible terms', 'maximum_amount': 18000, 'approval_time': '5 days', 'fees': 60.0, 'eligibility_criteria': 'Proof of residence', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'loan_type': 'Mortgage', 'interest_rates': 6.2, 'loan_terms': 'Up to 20 years', 'maximum_amount': 180000, 'approval_time': '12 days', 'fees': 280.0, 'eligibility_criteria': 'Minimum income of 2000/month', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Attijari Bank', 'loan_type': 'Car Loan', 'interest_rates': 4.8, 'loan_terms': 'Flexible terms', 'maximum_amount': 50000, 'approval_time': '3 days', 'fees': 110.0, 'eligibility_criteria': 'Age between 21 and 60', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Attijari Bank', 'loan_type': 'Personal Loan', 'interest_rates': 8.3, 'loan_terms': 'Flexible terms', 'maximum_amount': 22000, 'approval_time': '5 days', 'fees': 90.0, 'eligibility_criteria': 'Valid employment contract', 'created_at': datetime.datetime.now()},
    {'bank_name': 'Attijari Bank', 'loan_type': 'Mortgage', 'interest_rates': 6.5, 'loan_terms': 'Up to 20 years', 'maximum_amount': 200000, 'approval_time': '10 days', 'fees': 230.0, 'eligibility_criteria': 'Property must be insured', 'created_at': datetime.datetime.now()}
]


    

        credit_cards = [
            {'bank_name': 'Société Tunisienne de Banque (STB)', 'annual_fees': 50, 'cashback_rewards': '1% cashback on purchases', 'credit_limits': 10000, 'interest_rates_on_unpaid_balances': 12},
            {'bank_name': 'Banque Nationale Agricole (BNA)', 'annual_fees': 40, 'cashback_rewards': 'Reward points redeemable for gifts', 'credit_limits': 15000, 'interest_rates_on_unpaid_balances': 11},
            {'bank_name': 'Attijari Bank', 'annual_fees': 60, 'cashback_rewards': '2% cashback on fuel and groceries', 'credit_limits': 20000, 'interest_rates_on_unpaid_balances': 13},
            {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'annual_fees': 45, 'cashback_rewards': 'Earn airline miles on purchases', 'credit_limits': 18000, 'interest_rates_on_unpaid_balances': 12.5},
            {'bank_name': 'Qatar National Bank (QNB)', 'annual_fees': 100, 'cashback_rewards': '3% cashback on dining and travel', 'credit_limits': 25000, 'interest_rates_on_unpaid_balances': 14},
            {'bank_name': 'Bank ABC', 'annual_fees': 30, 'cashback_rewards': 'Reward points on every purchase', 'credit_limits': 12000, 'interest_rates_on_unpaid_balances': 10.5},
            {'bank_name': 'TSB Bank', 'annual_fees': 55, 'cashback_rewards': '1.5% cashback on online purchases', 'credit_limits': 15000, 'interest_rates_on_unpaid_balances': 12.8},
            {'bank_name': 'Al Baraka Bank Tunisia', 'annual_fees': 50, 'cashback_rewards': 'Sharia-compliant reward system', 'credit_limits': 14000, 'interest_rates_on_unpaid_balances': 11.5},
            {'bank_name': 'Amen Bank', 'annual_fees': 35, 'cashback_rewards': 'Cashback on utility bill payments', 'credit_limits': 16000, 'interest_rates_on_unpaid_balances': 12},
            {'bank_name': 'Banque de l\'Habitat (BH)', 'annual_fees': 40, 'cashback_rewards': 'Redeemable gift vouchers on spending', 'credit_limits': 15000, 'interest_rates_on_unpaid_balances': 11.8},
            {'bank_name': 'Arab Tunisian Bank (ATB)', 'annual_fees': 65, 'cashback_rewards': '2% cashback on all purchases', 'credit_limits': 22000, 'interest_rates_on_unpaid_balances': 13.5},
            {'bank_name': 'Wifak Bank', 'annual_fees': 50, 'cashback_rewards': 'Flexible reward system for frequent users', 'credit_limits': 14000, 'interest_rates_on_unpaid_balances': 11.3},
            {'bank_name': 'Banque Zitouna', 'annual_fees': 45, 'cashback_rewards': 'Islamic finance rewards', 'credit_limits': 17000, 'interest_rates_on_unpaid_balances': 11.7},
            {'bank_name': 'Banque de Tunisie', 'annual_fees': 70, 'cashback_rewards': '3% cashback on travel bookings', 'credit_limits': 24000, 'interest_rates_on_unpaid_balances': 13.2},
            {'bank_name': 'Citibank', 'annual_fees': 120, 'cashback_rewards': '4% cashback on global purchases', 'credit_limits': 30000, 'interest_rates_on_unpaid_balances': 15},
            {'bank_name': 'Banque Tunisienne de Solidarité (BTS)', 'annual_fees': 25, 'cashback_rewards': 'Basic cashback benefits for local purchases', 'credit_limits': 8000, 'interest_rates_on_unpaid_balances': 10},
            {'bank_name': 'Bank of Africa - Tunisia', 'annual_fees': 55, 'cashback_rewards': '2% cashback on entertainment', 'credit_limits': 20000, 'interest_rates_on_unpaid_balances': 12.5}
        ]


        fees_data = [
        {'bank_name': 'Société Tunisienne de Banque (STB)', 'account_maintenance_fees': 40.0, 'atm_withdrawal_fees': 1.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Banque Nationale Agricole (BNA)', 'account_maintenance_fees': 30.0, 'atm_withdrawal_fees': 1.0, 'international_transfer_fees': 45.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Banque de l\'Habitat (BH)', 'account_maintenance_fees': 20.0, 'atm_withdrawal_fees': 2.0, 'international_transfer_fees': 60.0, 'currency_exchange_fees': 1.5},
        {'bank_name': 'Banque de Financement des Petites et Moyennes Entreprises (BFPME)', 'account_maintenance_fees': 25.0, 'atm_withdrawal_fees': 1.0, 'international_transfer_fees': 55.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Banque Tunisienne de Solidarité (BTS)', 'account_maintenance_fees': 15.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Tunisian Solidarity Bank (BS)', 'account_maintenance_fees': 10.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Banque de Tunisie et des Emirats (BTE)', 'account_maintenance_fees': 40.0, 'atm_withdrawal_fees': 2.0, 'international_transfer_fees': 55.0, 'currency_exchange_fees': 1.5},
        {'bank_name': 'Amen Bank', 'account_maintenance_fees': 30.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Arab Tunisian Bank (ATB)', 'account_maintenance_fees': 35.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 60.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Banque Intercontinentale Arabe de Tunisie (BIAT)', 'account_maintenance_fees': 120.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 70.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Banque Zitouna', 'account_maintenance_fees': 25.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Citibank', 'account_maintenance_fees': 1200.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 100.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Al Baraka Bank Tunisia', 'account_maintenance_fees': 30.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Bank of Africa - Tunisia', 'account_maintenance_fees': 40.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Attijari Bank', 'account_maintenance_fees': 60.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 100.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Qatar National Bank (QNB)', 'account_maintenance_fees': 50.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 100.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Zitouna Bank', 'account_maintenance_fees': 25.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0},
        {'bank_name': 'Wifak Bank', 'account_maintenance_fees': 20.0, 'atm_withdrawal_fees': 0.0, 'international_transfer_fees': 50.0, 'currency_exchange_fees': 1.0}
    ]

        
        finance_news_data = [
    {
        'title': 'Central Bank Of Tunisia Will Hold Policy Rate Through 2025 Due To Sticky Inflation',
        'content': 'Central Bank Of Tunisia Will Hold Policy Rate Through 2025 Due To Sticky Inflation ',
        'source': 'BMI',
        'published_at': datetime.datetime(2025, 1, 16, 9, 0),
        'link': 'https://www.fitchsolutions.com/bmi/banking-financial-services/quick-view-central-bank-tunisia-will-hold-policy-rate-through-2025-due-sticky-inflation-29-11-2024',
        'image_url': 'https://www.fitchsolutions.com/sites/default/files/styles/large/public/articles/gettyimages-1207694989.jpg.webp?VersionId=Mxg2FsImKuxgB6AOnzzJz8gj5qfLt6vw&itok=Rz0VzENo',
        'tags': 'insurance, California, wildfires',
        'author': 'Jane Doe'
    },
    {
        'title': 'Tunisia central bank keeps key rate at 8%',
        'content': 'Tunisia central bank keeps key rate at 8%',
        'source': 'Financial News London',
        'published_at': datetime.datetime(2025, 1, 16, 10, 0),
        'link': 'https://www.cnbcafrica.com/wire/655429/',
        'image_url': 'https://example.com/images/Aboria-Capital.jpg',
        'tags': 'real estate, investment, Europe',
        'author': 'John Smith'
    },
    {
        'title': 'Hays nudges profit forecast lower as recruitment slows',
        'content': 'Hays has adjusted its profit forecast lower due to a global hiring slowdown, citing "ongoing economic uncertainty." The company observed a 12% drop in net fees with a notable 19% decline in permanent hire fees and a 7% decrease in temporary hire fees. The UK and Ireland saw a 14% decline in hiring, with public sector hiring falling by 21%. Hays anticipates half-year operating profits to be around £25 million, at the lower end of previous estimates. Despite this, shares rose by 3.2%, reflecting investor anticipation of a slowdown indicated by similar reports from competitors like Robert Walters and PageGroup. Hays CEO Dirk Hahn emphasized efforts towards company restructuring and operational efficiency amidst challenging markets. The company has also cut costs by reducing its workforce and plans further cuts until the 2027 fiscal year. This trend of cautious hiring is influenced by higher standards for new hires and increased employer national insurance contributions. Other recruitment companies are similarly impacted by low unemployment rates and higher business costs, with fewer companies expanding their workforce.',
        'source': 'The Times',
        'published_at': datetime.datetime(2025, 1, 16, 11, 0),
        'link': 'https://www.thetimes.co.uk/article/hays-warns-on-profit-as-recruitment-slows-zv2s5xx7z',
        'image_url': 'https://example.com/images/Hays-Recruitment.jpg',
        'tags': 'recruitment, profit forecast, economic uncertainty',
        'author': 'Sarah Johnson'
    },
    {
        'title': 'Intel plans to spin out venture-capital arm as part of restructuring',
        'content': 'Intel is planning to spin out its venture-capital arm, Intel Capital, as part of its ongoing restructuring efforts. With over $5 billion in assets, Intel Capital has invested in more than 1,800 companies, generating $170 billion in market value over the past decade. The standalone operation is expected to commence in the second half of the year, under a new name. David Zinsner, Intel\'s interim co-CEO and CFO, described the move as beneficial, allowing the VC arm to access new capital sources while maintaining collaboration with Intel. This step follows Intel\'s announcement of separating its foundry division into an independent subsidiary and comes after the departure of former CEO Pat Gelsinger. Intel\'s stock has decreased by 4% this year and 58% over the past 52 weeks.',
        'source': 'MarketWatch',
        'published_at': datetime.datetime(2025, 1, 16, 12, 0),
        'link': 'https://www.marketwatch.com/story/heres-intels-latest-turnaround-move-547d340e',
        'image_url': 'https://example.com/images/Intel-Capital.jpg',
        'tags': 'Intel, venture capital, restructuring',
        'author': 'David Lee'
    }
]

        
        for data in online_banking_data:
            added_interface = add_online_banking_interface(
                bank_name=data['bank_name'],
                mobile_app_usability=data['mobile_app_usability'],
                bill_payments=data['bill_payments'],
                e_wallet_integration=data['e_wallet_integration'],
                security_features=data['security_features']
            )
            print(f'Added: {added_interface}')

        for data in special_packages:
            added_package = add_special_package(
                bank_name=data['bank_name'],
                package_name=data['package_name'],
                account_maintenance_fees=data['account_maintenance_fees'],
                perks_and_benefits=data['perks_and_benefits'],
                eligibility_requirements=data['eligibility_requirements']
            )
            print(f'Added: {added_package}')

        for data in minimum_balances:
            added_balance = add_minimum_balance(
                bank_name=data['bank_name'],
                minimum_balance_requirement=data['minimum_balance_requirement'],
                annual_interest_rate=data['annual_interest_rate'],
                additional_benefits=data['additional_benefits']
            )
            print(f'Added: {added_balance}')

        for data in loans:
            added_loan = add_loan(
                bank_name=data['bank_name'],
                loan_type=data['loan_type'],
                interest_rate=data['interest_rates'],
                loan_term=data['loan_terms'],
                eligibility_criteria=data['eligibility_criteria']
            )
            print(f'Added: {added_loan}')

        for data in credit_cards:
            added_card = add_credit_card(
                bank_name=data['bank_name'],
                annual_fees=data['annual_fees'],
                cashback_rewards=data['cashback_rewards'],
                credit_limits=data['credit_limits'],
                interest_rates_on_unpaid_balances=data['interest_rates_on_unpaid_balances']
            )
            print(f'Added: {added_card}')

        for data in fees_data:
            added_fees = add_fees(
                bank_name=data['bank_name'],
                account_maintenance_fees=data['account_maintenance_fees'],
                atm_withdrawal_fees=data['atm_withdrawal_fees'],
                international_transfer_fees=data['international_transfer_fees'],
                currency_exchange_fees=data['currency_exchange_fees']
            )
            print(f'Added: {added_fees}')
        for data in finance_news_data:
            added_news = add_news(
                title=data['title'],
                content=data['content'],
                source=data['source'],
                link=data['link']
            )
            print(f"Added: {added_news}")
        for data in convert_data:
            added_convert = add_convert(
                to_currency=data['to_currency'],
                conversion_rate=data['conversion_rate']
            )
            print(f"Added: {added_convert}")
            
            
