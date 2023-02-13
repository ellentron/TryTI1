import customtkinter as ctk

from UiSections.uiPowerMeter import UiPowerMeter


class UiSect3(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        ctk.CTkFrame.__init__(self, master, **kwargs)

        # Create 3 Tabs
        self.tabview = ctk.CTkTabview(self, fg_color="lightgray", bg_color="lightgray")
        self.tabview.pack(fill="both", expand=True, padx=(5, 5), pady=(5, 5))
        tab1 = self.tabview.add("Power Meter")
        tab2 = self.tabview.add("Wavelength Meter")
        tab3 = self.tabview.add("Reports and Charts")
        self.tabview.tab("Power Meter").pack_propagate(False)
        self.tabview.tab("Wavelength Meter").pack_propagate(False)
        self.tabview.tab("Reports and Charts").pack_propagate(False)

        # Create "Power Meter" frame and place it on the tab1
        self.power_meter_frame = ctk.CTkFrame(tab1)# Create "Power Meter" frame and place it on the tab1
        self.power_meter_frame.pack(fill="both", expand=True, padx=(5, 5), pady=(0, 5))

        # # Create "Power Meter" label and place it on power_meter_frame
        # self.lbl_power_meter = ctk.CTkLabel(self.power_meter_frame, text="Power Meter", font=ctk.CTkFont(size=16, weight="bold"))
        # self.lbl_power_meter.pack(side="top", anchor="nw", padx=(0, 0), pady=(0, 0))

        # Create UiPowerMeter instance
        self.uipm = UiPowerMeter(self.power_meter_frame)
        self.uipm.pack(fill="both", expand=True, padx=(0, 0), pady=(0, 0))

        # Create "Power Meter" frame and place it on the tab1
        self.wavelength_meter_frame = ctk.CTkFrame(tab2)
        self.wavelength_meter_frame.pack(fill="both", expand=True)

        # Create "Wavelength Meter" label and place it on wavelength_meter_frame
        self.lbl_wavelength_meter = ctk.CTkLabel(self.wavelength_meter_frame, text="Wavelength Meter", font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_wavelength_meter.pack(side="top", anchor="nw", padx=(15, 0))

        # Create "Reports and Charts" frame and place it on the tab3
        self.reports_charts_frame = ctk.CTkFrame(tab3)
        self.reports_charts_frame.pack(fill="both", expand=True)

        # Create "Reports and Charts" label and place it on reports_charts_frame
        self.lbl_reports_charts = ctk.CTkLabel(self.reports_charts_frame, text="Reports and Charts", font=ctk.CTkFont(size=16, weight="bold"))
        self.lbl_reports_charts.pack(side="top", anchor="nw", padx=(15, 0))

