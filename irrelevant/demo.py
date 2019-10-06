import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x0b9a, idProduct=0x0800)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None
print ("EP", ep)

collected = 0
while collected < 10:
    print ("*")
    data = dev.read(ep, ep.wMaxPacketSize)
    print (data)
    
usb.util.release_interface(dev, interface)
#dev.attach_kernel_driver

# write the data
#ep.write('test')