import pandas as pd

df = pd.read_excel(r"C:\Users\ZolcsiPolcsi\Downloads\price_offer_table_of_contents.xlsx")

class Price_Offer:

    # Class for the main feature of the program

    EUR_RATE = 378.2
    TRANSPORT_COSTS = 37800
    INSTALLATION_FEE = "Telepítési munkadíj, anyagszállítás, kiszállási díj"

    def __init__(self, roof_type, panel_type, number_of_phases, number_of_strings, travel_distance, inverter_type,
                 number_of_fireproof_switches, smart_meter, charge_controller, number_of_batteries, backup_system,
                 provider,
                 number_of_inverters, thunder_rod = False, margin = 1.23, plomba = False, number_of_panels = 1,
                 inverter_brand = "Huawei"):

        self.inverter_brand = inverter_brand
        self.panel_type = panel_type
        self.number_of_phases = number_of_phases
        self.number_of_strings = number_of_strings
        self.travel_distance = travel_distance
        self.number_of_panels = number_of_panels
        self.inverter_type = inverter_type
        self.number_of_inverters = number_of_inverters
        self.plomba = plomba
        self.roof_type = roof_type
        self.margin = margin
        self.number_of_fireproof_switches = number_of_fireproof_switches
        self.thunder_rod = thunder_rod
        self.smart_meter = smart_meter
        self.charge_controller = charge_controller
        self.number_of_batteries = number_of_batteries
        self.backup_system = backup_system
        self.provider = provider

    def __str__(self):
        # Function for outputting string-based description of the object
        return f"""
Panel Price: {self.panel_price()}
Plomba: {self.plomba_bontas()}
Inverter optimiser price: {self.inverter_optimiser_price()}
Inverter price: {self.inverter_price()}
VAT Value: {Price_Offer.VAT(self.inverter_price())}
Frame price: {self.frame_price()}
Solar panel text: {self.solar_panel_text()}
Inverter text: {self.inverter_text()}
Mount text: {self.mount_text()}
Cabling text: {self.cabling_text()}
Batteries text: {self.batteries_text()}
        """

    def panel_price(self):
        # Function to calculate the price of panels
        relevant_product = df[df["Name"] == self.panel_type]
        return int(relevant_product["Price"]) * Price_Offer.EUR_RATE * self.number_of_panels

    def inverter_optimiser_price(self):
        # Function to calculate the price of inverter optimiser
        relevant_product = df[df["Name"] == "Huawei optimalizáló"]
        return int(relevant_product["Price"]) * Price_Offer.EUR_RATE * self.number_of_inverters

    def inverter_price(self):
        # Function to calculate the price of inverters
        relevant_product = df[df["Name"] == self.inverter_type]
        return int(relevant_product["Price"]) * Price_Offer.EUR_RATE * \
               self.number_of_inverters

    def frame_price(self):
        # Function to calculate the price of the frame for mounting the panels
        relevant_product = df[df["Name"] == self.roof_type]
        return int(relevant_product["Price"]) * Price_Offer.EUR_RATE * \
            self.number_of_panels

    def plomba_bontas(self):
        if self.plomba == True:
            relevant_product = df[df["Name"] == "Kell plombabontás?"]
            return int(relevant_product["Price"]) * Price_Offer.EUR_RATE
        else:
            return 0

    def VAT(value):
        # Function to return VAT amount of items
        return value * 0.27

    def solar_panel_text(self):
        return f"Napelem modul {self.panel_type}"

    def inverter_text(self):
        if self.number_of_panels > 0:
            return f"{self.inverter_brand} {self.inverter_type} inverter, 10 év termékgarancia, "\
                   f"{self.number_of_inverters} optimalizáló"
        else:
            return f"{self.inverter_brand} {self.inverter_type} inverter, 10 év termékgarancia"

    def mount_text(self):

        # String representation of the mounting

        return f"Napelemes tartószerkezet {self.roof_type}"

    def cabling_text(self):

        # Function for specifying the included cables

        if self.number_of_fireproof_switches > 0 and self.thunder_rod == True:
            return "Kábelek (egyen-, és váltóáramú) túlfeszültségvédelem, szerelési anyagok,"\
                   " plusz villámvédelmi eszközök, tűzvédelmi kapcsoló"
        elif self.number_of_fireproof_switches > 0:
            return "Kábelek (egyen-, és váltóáramú) túlfeszültségvédelem, szerelési anyagok, tűzvédelmi kapcsoló"
        elif self.thunder_rod == True:
            return "Kábelek (egyen-, és váltóáramú) túlfeszültségvédelem, "\
                   "szerelési anyagok, plusz villámvédelmi eszközök"

    def batteries_text(self):

        # Function for specifying the included services for batteries

        if self.smart_meter == True and self.charge_controller == True and self.number_of_batteries > 0 and \
                self.backup_system == True:
            return f"{self.inverter_brand} {self.number_of_phases} fázisú Smart Meter + Töltésvezérlő + "\
                   f"Luna 2000 5kW {self.number_of_batteries} db Backup System 1 fázis"

        elif self.smart_meter == True and self.charge_controller == True and self.number_of_batteries > 0 and \
            self.backup_system == False:
            return f"{self.inverter_brand} {self.number_of_phases} fázisú Smart Meter + Töltsévezérlő +"\
                   "Luna 2000 5kW {self.number_of_batteries} db"

        elif self.smart_meter == True and self.charge_controller == False:
            return f"{self.inverter_brand} {self.number_of_phases} fázisú Smart Meter"

        elif self.smart_meter == False:
            return "Nincs akkumulátor"

        else:
            return "-"

    def provider_text(self):
        if self.provider == "Elmű-Émász":
            return "Áramszolgáltatói engedélyeztetés folyamata és készre jelentés leadása"
        else:
            return "Áramszolgáltatói engedélyeztetés folyamata, készre jelentés leadása és \
             érintésvédelmi jegyzőkönyv elkészítése"

arajanlat = Price_Offer(panel_type= "Longi Solar 405Wp mono, PERC technológiás 120 félcellás - 12 év termékgarancia",
                        number_of_panels = 2, number_of_phases= 3, number_of_strings= 2, travel_distance= 50,
                        inverter_type= "SUN2000-8KTL-M1 (3 fázis)", number_of_inverters=1, plomba = True,
                        roof_type = "cseréptetőhöz", number_of_fireproof_switches= 2, smart_meter = True,
                        charge_controller= True, number_of_batteries= 3, backup_system= True, provider= "Elmű-Émász")
print(arajanlat)
print(Price_Offer.solar_panel_text(arajanlat))