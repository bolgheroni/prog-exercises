from sources import VGASource, HDMISource
from cables import VGACable, HDMICable
from adapters import HDMIToVGAAdapter, VGAToHDMIAdapter

def main():
    vga_source = VGASource()
    hdmi_source = HDMISource()

    vga_cable = VGACable()
    hdmi_cable = HDMICable()

    vga_cable.connect(vga_source)
    hdmi_cable.connect(hdmi_source)

    vga_signal = vga_cable.get_signal()
    hdmi_signal = hdmi_cable.get_signal()

    print(f"VGA signal: {vga_signal} from VGA source")
    print(f"HDMI signal: {hdmi_signal} from HDMI source")

    hdmi_to_vga_adapter = HDMIToVGAAdapter()
    vga_to_hdmi_adapter = VGAToHDMIAdapter()

    hdmi_to_vga_adapter.connect(hdmi_cable)
    vga_to_hdmi_adapter.connect(vga_cable)

    vga_signal = hdmi_to_vga_adapter.get_signal()
    hdmi_signal = vga_to_hdmi_adapter.get_signal()

    print(f"VGA signal: {vga_signal} from HDMI cable")
    print(f"HDMI signal: {hdmi_signal} from VGA cable")


if __name__ == "__main__":
    main()