import usb.core
import usb.util

def main():
    device = usb.core.find(idVendor=0x0b9a, idProduct=0x0800)

    # use the first/default configuration
    device.set_configuration()

    # first endpoint
    endpoint = device[0][(0,0)][0]

    # read a data packet
    data = None
    while True:
        try:
            data = device.read(0x80+endpoint.bEndpointAddress,
                               endpoint.wMaxPacketSize)
            print (data)

        except usb.core.USBError as e:
            data = None
            if e.args == ('Operation timed out',):

                continue

if __name__ == '__main__':
  main()