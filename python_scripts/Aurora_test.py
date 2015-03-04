from PyChipsUser import *
AddrTable = AddressTable("./AddrTable.dat")
import os
import time
########################################
# IP address
########################################
f = open('./ipaddr.dat', 'r')
ipaddr = f.readline()
f.close()
board = ChipsBusUdp(AddrTable, ipaddr, 50001)
print
print "--=======================================--"
print "  Opening Board with IP", ipaddr
print "--=======================================--"
########################################
#chipsLog.setLevel(logging.DEBUG)    # Verbose logging (see packets being sent and received)

#testword = 0xaaaa5555

###########################################
#test reg
#print
#print "-> read initial value"
#init = glib.read("my_test_reg") 
#print "-> test reg initial value : ", init

#print
#print "-> test_reg initialize"
#glib.write("my_test_reg",0x00000000, 0) 

#print
#print "-> write test reg"
#glib.write("my_test_reg",0xcafebabe, 0)

#print
#print "-> Read test reg"
#readout = glib.read("my_test_reg")
#print "-> test reg readout :", hex(readout)

#print
#print "-> reg test done"
#print
#print "--=======================================--"
#print 
#print
################################################

data1 = 0x1234abcd
stat1 = 0xffffffff
data2 = 0xdeadbeef
stat2 = 0xffffffff

#print 
#print "reset link..."
#board.write("link_rst",0x00000001,0)
#rst = board.read("link_rst")
#print rst

print
print "-> Set loopback regs"
board.write("loopback_reg_pphi",0x00000000,0)
board.write("loopback_reg_mphi",0x00000000,0)

lbp = board.read("loopback_reg_pphi")
lbm = board.read("loopback_reg_mphi")
print bin(lbp), " ", bin(lbm)

print
print "-> write data to registers:", hex(data1)," ",hex(data2)
board.write("txdata_pphi",data1,0)
board.write("txdata_mphi",data2,0)
board.write("txstat_pphi",stat1,0)
board.write("txstat_mphi",stat2,0)

input1 = board.read("txdata_pphi")
input2 = board.read("txdata_mphi")
input1stat = board.read("txstat_pphi")
input2stat = board.read("txstat_mphi")

print 
print "check input regs: "
print hex(input1)
print hex(input1stat)
print hex(input2)
print hex(input2stat)

#print 
#print "unset link reset..."
#board.write("link_rst",0xfffffffe,0)
#rst = board.read("link_rst")
#print rst

print "-> read aurora plus phi output :"
dataout1 = board.read("rxdata_pphi")
print "-> aurora output :", hex(dataout1)

print
print "-> read aurora plus phi status :"
status11 = board.read("rxstat_pphi")
print "-> aurora status :", bin(status11)
status12 = board.read("live_status_pphi")
print "-> aurora live status :", bin(status12)

print
print "-> read aurora minus phi output :"
dataout2 = board.read("rxdata_mphi")
print "-> aurora output :", hex(dataout2)

print
print "-> read aurora minus phi status :"
status21 = board.read("rxstat_mphi")
print "-> aurora status :", bin(status21)
status22 = board.read("live_status_mphi")
print "-> aurora live status :", bin(status22)

