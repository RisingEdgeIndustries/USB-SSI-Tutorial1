# ################################################################
# Project Name:
# USB Bridge - Tutorial1_p1
#
# Author: rvalentine
# Date: 10/19/2023
#
#
# Project Description:
# ----------------------------------------------------------------
# This module (tutorial 1 part1) opens a connection to the USB 
# SSI bridge and reads the descriptor information and the entire
# configuration register space of the bridge. This information
# is printed to the console.
#
#
# Notes:
# ----------------------------------------------------------------
#
#
# ----------------------------------------------------------------
# Disclaimer:
# ----------------------------------------------------------------
# This library is provided strictly as example code. There is no
# expected reliablity of operation from RisingEdgeIndustries and 
# this source code is not to be sold or represented as a 3'd party
# solution for commercial use. The below code is development code
# for example use only supporting customers as they test the bridge
# products from RisingEdgeIndustries. Nothing in this file is allowed
# to be modified or sold in any way. No code below is released with 
# the intention or expectation of reliable operation.
#
# Packing this module with any 3d part code can only be done with 
# the inclusion of this disclaimer and no modifications.
# ################################################################


from USB_SSI_Libs.rei_usb_lib import USB20F_Device



# for logger
log_file_name = "tst_dump-regs"

# open USB lib
usb_dev0 = USB20F_Device(quiet=True, name=log_file_name)
usb_dev0.open_usb()

# read and print all configuration register info
usb_dev0.dump_regspace()

# read and print all USB descriptor info
usb_dev0.dump_descriptors()

# close brige USB library
usb_dev0.close_usb()


