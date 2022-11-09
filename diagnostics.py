uds=input("Enter UDS message: ")
parts=uds.split()
sid=parts[0]
subfn=parts[1]
did=parts[2]
data_rec=parts[3]
print("SID : ",sid)
print("Sub-function ID : ",subfn)
print("DID : ", did)
print("Data part : ", data_rec)

