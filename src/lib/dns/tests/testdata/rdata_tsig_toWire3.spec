#
# An artificial TSIG RDATA for toWire test.
#
[custom]
sections: tsig
[tsig]
algorithm: hmac-sha1
time_signed: 1286779327
mac_size: 12
# 0x1402... would be FAKEFAKE... if encoded in BASE64
mac: 0x140284140284140284140284
original_id: 16020
error: 18
other_len: 6
other_data: 0x140284140284
