class PropertyROI:
    def __init__(self):
        self.purchase_price = 0.0
        self.down_payment = 0.0
        self.m_rental_income = 0.0
        self.annual_property_taxes = 0.0
        self.annual_property_insurance = 0.0
        self.m_utilities = 0.0
        self.m_maintenance = 0.0
        self.annual_appreciation_rate = 0.0
        self.years_held = 0

    def get_user_inputs(self):
        self.purchase_price = float(input(" Purchase price of the property: $"))
        self.down_payment = float(input(" Down payment amount: $"))
        self.m_rental_income = float(input(" Monthly rental income: $"))
        self.annual_property_taxes = float(input(" annual property taxes: $"))
        self.annual_property_insurance = float(input(" annual property insurance: $"))
        self.m_utilities = float(input(" Monthly utilities cost: $"))
        self.m_maintenance = float(input(" Monthly maintenance cost: $"))
        self.annual_appreciation_rate = float(input("Appreciation rate: "))
        self.years_held = int(input("Years you plan to hold the property: "))

    def calculate_roi(self):
        total_expenses = (
            self.annual_property_taxes + self.annual_property_insurance +
            (self.m_utilities * 12) + (self.m_maintenance * 12)
        )
        
        estment = self.purchase_price - self.down_payment
        annual_cash_flow = (self.m_rental_income * 12) - total_expenses
        property_value_after_years = self.purchase_price * ((1 + (self.annual_appreciation_rate / 100)) ** self.years_held)
        
        roi = ((annual_cash_flow * self.years_held) + (property_value_after_years - self.purchase_price)) / estment * 100

        return roi

    def run(self):
        print("Rental Property ROI Calculator")
        self.get_user_inputs()
        roi = self.calculate_roi()
        print(f"\nYour ROI for the property  {self.years_held}  is: {roi:.2f}%")

if __name__ == "__main__":
    calculator = PropertyROI()
    calculator.run()
