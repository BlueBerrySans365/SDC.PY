import nsfkit
import json

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc4MDg3NzQ5MDAxNjIyMzIzMyIsInBlcm1zIjowLCJpYXQiOjE2MTA0NTIxNTF9.z7KY-CW_6vIMknsPupodkeVPT7PzooSAoladP4PyrGA"

test = nsfkit.SD().getRated(DSID="752114880588283964", BDSToken=token)

print(test)