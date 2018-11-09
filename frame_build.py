from scapy.all import * 
class TEST(Packet):
	name = "TEST Packet" 
	fields_desc = [
					FieldLenField("len", None, length_of="val", fmt="!H"), StrLenField("val", 0, length_from=lambda pkt:pkt.len)]
def extract_padding(self, p):
	return "", P
def _str__(self):
	return self.__iter__(.next().build()

class FOO(Packet):
	name = "FOO"
 	fields_desc = [
	ShortEnumField("sport", 1, {1:"REQUEST",2:"RESPONSE",3:"SUCCESS",4:"FAILURE"}),
 ShortEnumField("dport", 2, {1:"REQUEST", 2:"RESPONSE",3:"SUCCESS",4: "FAILURE"}),
  IntField("seg", ""), 
  IntField("ack",""),
   BitField("dataofs", 4, 4),
   BitField("reserved", 2, 2), 
    ShortField("window", OxBD),
  XShortField("cheksum",""),
   ShortField("urgptr",""),
    BitField("version", 9, 9),
     BitField("ihl", 3, 3),
      XByteField("tos",""), 
      ShortField("len",""),
       ShortField("id",""),
   FlagsField("flags", None, -32, ['TSET', 'Flags', 'Rate', 'Channel','FHSS','dBm_Antsignal',
'dBm_AntNoise', 'Lock_Quality', 'TX_Attenuation', 'dB_TX_Attenuation',
'dBM_TX_Power', 'Antenna', 'dB_Antsignal', 'dB_AntNoise', 'b14", "b15', 'b16', 'b17', 'b18', 'b19', 'b20', 'b21', 'b22', 'b23','b24', 'b25', 'b26', 'b27', 'b28', 'b29', 'b30', 'Ext']), 
   BitField("frag", 5, 5),
    ByteField("ttl",""), 
    ByteEnumField("proto",4, {1:"REQUEST", 2:"RESPONSE",3:"SUCCESS",4: "FAILURE"}), 
    XShortField ("chksum",""),
     Emph(SourceIPField("src","")), 
     Emph (DestIPField("dst", "")), 
     PacketListField("options", [], IPOption, length_from=Lambda p:p.ihl*4-20)
     ]
