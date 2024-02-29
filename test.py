import os

staging_server = os.environ.get('SERVER_URL')

if staging_server:
  print("server :", staging_server)
else:
  print("No server specified.")

#Added user profile form", "Implemented user profile validation
