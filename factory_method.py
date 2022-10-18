class FuelCalculator:
    def calculate(self, fuel_type, amount):
        calculate = self.get_calculator(fuel_type)
        return calculate(amount)

    def get_calculator(self, fuel_type):
        if fuel_type == "Gasoline":
            return self._calculate_for_gasoline
        elif fuel_type == "Ethanol":
            return self._calculate_for_ethanol
        elif fuel_type == "Gas":
            return self._calculate_for_gas
        else:
            raise ValueError(fuel_type)

    def _calculate_for_gasoline(self, amount):
        return amount/4

    def _calculate_for_ethanol(self, amount):
        return amount/2.5

    def _calculate_for_gas(self, amount):
        return amount/2


if __name__ == "__main__":
    amount = 50

    calculator = FuelCalculator()
    gasoline_liters = calculator.calculate("Gasoline", amount)
    print(
        f"Saya bisa membeli {gasoline_liters} liter gasoline dengan Rp{amount} perak")

    ethanol_liters = calculator.calculate("Ethanol", amount)
    print(
        f"Saya bisa membeli {ethanol_liters} liter ethanol dengan Rp{amount} perak")

    gas_cubic_meters = calculator.calculate("Gas", amount)
    print(
        f"Saya bisa membeli {gas_cubic_meters} gas per meter kubik dengan Rp{amount} perak")
